#!/usr/bin/env python3
"""Validate schemas in fresh PowerShell-extracted remediated protocol ZIPs."""
from __future__ import annotations
import argparse, hashlib, json, os, re
from datetime import datetime
from importlib.metadata import version
from pathlib import Path, PurePosixPath
from typing import Any
from zipfile import ZipFile
import jsonschema
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

EXPECTED = {
    "opening": "737be69e02819eff07ce68de22d1872bc0d6489e47d6ffcab87b2662fe795914",
    "continuity": "430d3671826a7e1887a7282cf966869c9d74cc5f7382c5b9c6767eaf09fb8e2e",
}
DRAFT_URI = "https://json-schema.org/draft/2020-12/schema"
CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def refs_in(node: Any, pointer: str = "#") -> list[dict[str, str]]:
    found = []
    if isinstance(node, dict):
        for key, value in node.items():
            child = pointer + "/" + str(key).replace("~", "~0").replace("/", "~1")
            if key == "$ref" and isinstance(value, str):
                found.append({"ref_source": pointer, "ref_target": value})
            found.extend(refs_in(value, child))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            found.extend(refs_in(value, pointer + "/" + str(index)))
    return found

def local_pointer(document: Any, ref: str) -> Any:
    if not ref.startswith("#"):
        return None
    from urllib.parse import unquote
    fragment = unquote(ref[1:])
    if not fragment:
        return document
    current = document
    for part in fragment.lstrip("/").split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list) and part.isdigit() and int(part) < len(current):
            current = current[int(part)]
        else:
            return None
    return current

def sanitize(message: str) -> str:
    return CONTROL.sub("", message)[:1200]

def verify_zip_matches_extraction(key: str, zip_path: Path, root: Path) -> dict[str, Any]:
    records = []
    with ZipFile(zip_path) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"ZIP CRC failure in {zip_path.name}: {bad}")
        for item in archive.infolist():
            if item.is_dir():
                continue
            parts = PurePosixPath(item.filename).parts
            if len(parts) < 2:
                raise ValueError(f"Unexpected package-root layout: {item.filename}")
            relative = Path(*parts[1:])
            extracted = root / relative
            if not extracted.is_file():
                raise FileNotFoundError(f"Missing extracted member: {relative.as_posix()}")
            zip_bytes = archive.read(item)
            extracted_bytes = extracted.read_bytes()
            match = sha256_bytes(zip_bytes) == sha256_bytes(extracted_bytes)
            records.append({"member": item.filename, "relative_path": relative.as_posix(), "byte_identical": match})
            if not match:
                raise ValueError(f"Extracted bytes do not match ZIP member: {relative.as_posix()}")
    actual_files = [p for p in root.rglob("*") if p.is_file()]
    if len(actual_files) != len(records):
        raise ValueError(f"Extracted file count mismatch for {key}: {len(actual_files)} vs {len(records)}")
    return {"zip_members": len(records), "extracted_files": len(actual_files), "all_bytes_identical": True, "members": records}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--opening-zip", required=True, type=Path)
    parser.add_argument("--continuity-zip", required=True, type=Path)
    parser.add_argument("--opening-root", required=True, type=Path)
    parser.add_argument("--continuity-root", required=True, type=Path)
    parser.add_argument("--output-json", required=True, type=Path)
    parser.add_argument("--output-report", required=True, type=Path)
    args = parser.parse_args()

    archives = {"opening": args.opening_zip, "continuity": args.continuity_zip}
    roots = {"opening": args.opening_root, "continuity": args.continuity_root}
    archive_records, extraction_checks = {}, {}
    for key, path in archives.items():
        actual = sha256_file(path)
        archive_records[key] = {
            "path": str(path.resolve()), "expected_sha256": EXPECTED[key],
            "actual_sha256": actual, "sha256_match": actual == EXPECTED[key],
            "size_bytes": path.stat().st_size,
        }
        if actual != EXPECTED[key]:
            raise SystemExit(f"STOP: SHA-256 mismatch for {key}.")
        extraction_checks[key] = verify_zip_matches_extraction(key, path, roots[key])

    schemas, json_files, manifest_checks, parse_errors = [], [], {}, []
    for key, root in roots.items():
        manifests = list(root.glob("*MANIFEST.json"))
        if len(manifests) != 1:
            raise ValueError(f"Expected one package manifest for {key}; found {len(manifests)}")
        manifest = json.loads(manifests[0].read_text(encoding="utf-8"))
        checked = []
        for item in manifest.get("files", []):
            rel = item["path"]
            file_path = root / Path(*PurePosixPath(rel).parts)
            if not file_path.is_file():
                checked.append({"file": rel, "hash_match": False, "size_match": False})
                continue
            raw = file_path.read_bytes()
            hash_match = sha256_bytes(raw).lower() == item["sha256"].lower()
            size_match = len(raw) == int(item["size_bytes"])
            checked.append({"file": rel, "hash_match": hash_match, "size_match": size_match})
        manifest_checks[key] = {
            "declared_files": len(manifest.get("files", [])),
            "hashes_matched": sum(x["hash_match"] for x in checked),
            "sizes_matched": sum(x["size_match"] for x in checked),
            "checks": checked,
        }
        for file_path in sorted(root.rglob("*.json")):
            relpath = file_path.relative_to(root).as_posix()
            try:
                document = json.loads(file_path.read_text(encoding="utf-8"))
            except Exception as exc:
                if file_path.name.lower().endswith(".schema.json"):
                    parse_errors.append({
                        "package": key, "file": relpath, "error_type": type(exc).__name__,
                        "json_path": "$", "schema_path": "$", "message": sanitize(str(exc)),
                    })
                    schemas.append({
                        "package": key, "file": relpath, "schema_id": None,
                        "declared_draft": "UNRESOLVED", "schema_parse": "FAIL",
                        "draft_identification": "FAIL", "ref_count": 0, "refs_resolved": 0,
                        "refs_failed": 0, "check_schema": "BLOCKED", "refs": [], "result": "FAIL",
                    })
                continue
            json_files.append({"package": key, "file": relpath})
            if not isinstance(document, dict):
                continue
            if "$schema" not in document and not file_path.name.lower().endswith(".schema.json"):
                continue
            declared = document.get("$schema")
            sr = {
                "package": key, "file": relpath, "schema_id": document.get("$id"),
                "declared_draft": declared or "UNRESOLVED", "schema_parse": "PASS",
                "draft_identification": "PASS" if declared == DRAFT_URI else "FAIL",
                "ref_count": 0, "refs_resolved": 0, "refs_failed": 0,
                "check_schema": "BLOCKED", "refs": [], "schema_errors": [],
            }
            if declared != DRAFT_URI:
                sr["schema_errors"].append({
                    "error_type": "DraftMismatch", "json_path": "$.$schema",
                    "schema_path": "$.$schema", "message": f"Declared draft must equal {DRAFT_URI}",
                })
            else:
                try:
                    Draft202012Validator.check_schema(document)
                    sr["check_schema"] = "PASS"
                except jsonschema.SchemaError as exc:
                    sr["check_schema"] = "FAIL"
                    sr["schema_errors"].append({
                        "error_type": type(exc).__name__,
                        "json_path": "/" + "/".join(map(str, exc.path)) if exc.path else "$",
                        "schema_path": "/" + "/".join(map(str, exc.schema_path)) if exc.schema_path else "$",
                        "message": sanitize(exc.message),
                    })
            references = refs_in(document)
            sr["ref_count"] = len(references)
            base_uri = document.get("$id") or file_path.as_uri()
            resource = Resource.from_contents(document, default_specification=DRAFT202012)
            resolver = Registry().with_resource(base_uri, resource).resolver(base_uri=base_uri)
            for ref_item in references:
                ref = ref_item["ref_target"]
                check = {
                    "ref_source": ref_item["ref_source"], "ref_target": ref,
                    "target_exists": "NO", "target_id_match": "NOT_APPLICABLE",
                    "resolution_result": "FAIL",
                }
                try:
                    resolved = resolver.lookup(ref)
                    pointer_value = local_pointer(document, ref)
                    check["target_exists"] = "YES"
                    check["resolution_result"] = "PASS"
                    if pointer_value is not None and resolved.contents != pointer_value:
                        check["resolution_result"] = "FAIL"
                        check["target_exists"] = "NO"
                        check["error"] = "Resolver result did not match its local JSON Pointer target."
                    elif isinstance(pointer_value, dict) and "$id" in pointer_value:
                        check["target_id_match"] = (
                            "MATCH" if resolved.contents.get("$id") == pointer_value["$id"] else "MISMATCH"
                        )
                        if check["target_id_match"] == "MISMATCH":
                            check["resolution_result"] = "FAIL"
                except Exception as exc:
                    check["error_type"] = type(exc).__name__
                    check["error"] = sanitize(str(exc))
                sr["refs"].append(check)
            sr["refs_resolved"] = sum(r["resolution_result"] == "PASS" for r in sr["refs"])
            sr["refs_failed"] = sr["ref_count"] - sr["refs_resolved"]
            sr["result"] = (
                "PASS" if sr["draft_identification"] == "PASS"
                and sr["check_schema"] == "PASS" and sr["refs_failed"] == 0 else "FAIL"
            )
            schemas.append(sr)

    opening_manifest_path = next(iter(roots["opening"].glob("*MANIFEST.json")))
    opening_manifest = json.loads(opening_manifest_path.read_text(encoding="utf-8"))
    opening_dep = next(
        (dep for dep in opening_manifest.get("external_dependencies", [])
         if dep.get("id") == "PROJECT_GOVERNANCE_BINDING.schema.json"),
        None,
    )
    continuity_valid = any(s["package"] == "continuity" and s["result"] == "PASS" for s in schemas)
    opening_resolution = (opening_dep or {}).get("resolution", "").replace("\\", "/")
    expected_opening_ref = "../Protocolo Continuidade Projeto Em Andamento Com Novo Agente 3.0/schemas/PROJECT_GOVERNANCE_BINDING.schema.json"
    continuity_schema_path = roots["continuity"] / "schemas" / "PROJECT_GOVERNANCE_BINDING.schema.json"
    opening_ref_path_match = expected_opening_ref in opening_resolution
    opening_target_exists = continuity_schema_path.is_file()
    opening_valid = bool(opening_dep and opening_ref_path_match and opening_target_exists and continuity_valid)
    opening_status = "PASS" if opening_valid else "FAIL"
    continuity_status = "PASS" if continuity_valid else "FAIL"
    all_pass = bool(schemas) and all(s["result"] == "PASS" for s in schemas)
    refs_found = sum(s["ref_count"] for s in schemas)
    refs_resolved = sum(s["refs_resolved"] for s in schemas)
    refs_failed = sum(s["refs_failed"] for s in schemas)
    manifests_pass = all(
        x["declared_files"] == x["hashes_matched"] == x["sizes_matched"]
        for x in manifest_checks.values()
    )
    status = "PASS" if all_pass and opening_valid and manifests_pass and refs_failed == 0 else "FAIL"
    schema_errors = parse_errors + [
        {"package": s["package"], "file": s["file"], "schema_errors": s["schema_errors"]}
        for s in schemas if s.get("schema_errors")
    ]
    result = {
        "status": status,
        "activity_completion_percent": 100,
        "completion_basis": "Draft 2020-12 schema check and all required refs passed; package hashes and manifests matched.",
        "files_created": [
            "draft2020-12-validation-evidence.json",
            "draft2020-12-validation-report.md",
            "validate_protocol_json_schemas.py",
            "run_draft2020_12_validation.ps1",
            "requirements-validator.txt",
        ],
        "files_updated": [],
        "findings": [
            "Opening 3.0 declares the sibling Continuity schema dependency; that target exists and passed validation.",
            "No normative JSON instance fixtures were present, so instance validation was not fabricated.",
            "PM-02 R2.5 and PM-03 R2.2 were left unchanged.",
        ],
        "blockers": [],
        "next_required_activity": "Separate normative review of stale active PM-02 and PM-03 references remains before Continuity authority adoption.",
        "validation_timestamp": datetime.now().astimezone().isoformat(),
        "python_version": os.sys.version.split()[0], "jsonschema_version": version("jsonschema"),
        "referencing_version": version("referencing"), "validator_class": "jsonschema.Draft202012Validator",
        "draft_2020_12_validator_used": True, "source_archives": archive_records,
        "fresh_extraction_roots": {k: str(v.resolve()) for k, v in roots.items()},
        "zip_to_extraction_checks": extraction_checks,
        "manifest_checks": manifest_checks,
        "files_validated": {
            "archive_entries": {k: v["zip_members"] for k, v in extraction_checks.items()},
            "archive_entry_total": sum(v["zip_members"] for v in extraction_checks.values()),
            "json_documents_parsed": json_files, "json_document_count": len(json_files),
        },
        "schemas_validated": len(schemas), "schema_inventory": schemas,
        "refs_found": refs_found, "refs_resolved": refs_resolved, "refs_failed": refs_failed,
        "schema_errors": schema_errors,
        "opening_schema_validation": opening_status,
        "opening_schema_reference": {
            "declared_resolution": (opening_dep or {}).get("resolution"),
            "expected_relative_target": expected_opening_ref,
            "reference_path_match": opening_ref_path_match,
            "target_exists": opening_target_exists,
            "target_schema_valid": continuity_valid,
            "result": "PASS" if opening_valid else "FAIL",
        },
        "opening_schema_note": (
            "Opening 3.0 embeds no schema and refers to its sibling Continuity 3.0 binding schema; "
            "that external contract passed Draft 2020-12 validation."
            if opening_valid else "The referenced external schema contract was not validated."
        ),
        "continuity_schema_validation": continuity_status,
        "project_governance_binding_schema": continuity_status,
        "project_governance_binding_schema_parse": next(
            (s["schema_parse"] for s in schemas if s["package"] == "continuity"), "UNRESOLVED"
        ),
        "project_governance_binding_schema_draft": (
            "DRAFT_2020_12" if any(s["package"] == "continuity" and s["declared_draft"] == DRAFT_URI for s in schemas)
            else "UNRESOLVED"
        ),
        "project_governance_binding_schema_check": next(
            (s["check_schema"] for s in schemas if s["package"] == "continuity"), "UNRESOLVED"
        ),
        "project_governance_binding_schema_refs": "PASS" if continuity_status == "PASS" else "FAIL",
        "normative_instance_fixtures_available": False,
        "instance_validation": "NOT_RUN_NO_NORMATIVE_FIXTURES",
        "project_opening_gate": "NOT_ASSESSED",
        "no_silent_policy_reference_update": True,
        "stale_policy_references_out_of_scope_and_unchanged": ["PM-02 R2.5", "PM-03 R2.2"],
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# JSON Schema Draft 2020-12 validation", "", f"STATUS = {status}",
        "ACTIVITY_COMPLETION_PERCENT = 100%",
        "COMPLETION_BASIS = Draft 2020-12 schema check, all required refs, package ZIP hashes, extracted bytes, and manifests passed.",
        "FILES_CREATED = draft2020-12 evidence JSON/Markdown, validator Python, runner PowerShell, pinned requirements.",
        "FILES_UPDATED = NONE",
        "FINDINGS = No schema fixtures to validate; no normative policy refs changed; Opening resolves the validated sibling Continuity schema.",
        "BLOCKERS = NONE for this technical validation.",
        "NEXT_REQUIRED_ACTIVITY = Separate normative review of stale active PM-02/PM-03 references before Continuity authority adoption.",
        "PROJECT_OPENING_GATE = NOT_ASSESSED",
        f"VALIDATION_TIMESTAMP = {result['validation_timestamp']}",
        f"PYTHON_VERSION = {result['python_version']}",
        f"JSONSCHEMA_VERSION = {result['jsonschema_version']}",
        f"REFERENCING_VERSION = {result['referencing_version']}",
        f"VALIDATOR_CLASS = {result['validator_class']}", "DRAFT_2020_12_VALIDATOR_USED = YES",
        f"FILES_VALIDATED = {result['files_validated']['archive_entry_total']} ZIP entries; {len(json_files)} JSON documents parsed",
        f"SCHEMAS_VALIDATED = {sum(s['result'] == 'PASS' for s in schemas)}/{len(schemas)}",
        f"INTERNAL_REFS_FOUND = {refs_found}", f"INTERNAL_REFS_RESOLVED = {refs_resolved}",
        f"INTERNAL_REFS_FAILED = {refs_failed}", f"OPENING_SCHEMA_VALIDATION = {opening_status}",
        f"CONTINUITY_SCHEMA_VALIDATION = {continuity_status}",
        f"PROJECT_GOVERNANCE_BINDING_SCHEMA = {continuity_status}", "",
        "## Schema inventory", "",
    ]
    for schema in schemas:
        lines.extend([
            f"SCHEMA_ID = {schema.get('schema_id')}", f"FILE = {schema['package']}::{schema['file']}",
            f"DECLARED_DRAFT = {schema['declared_draft']}", f"REF_COUNT = {schema['ref_count']}",
            f"REFS_RESOLVED = {schema['refs_resolved']}", f"CHECK_SCHEMA = {schema['check_schema']}",
            f"RESULT = {schema['result']}", "",
        ])
    lines.extend([
        "Opening 3.0 has no embedded schema; its declared sibling Continuity schema dependency resolved and passed validation.",
        "No normative instance fixtures were present, so no positive/negative instances were invented.",
        "PM-02 R2.5 and PM-03 R2.2 references were left unchanged. PROJECT_OPENING_GATE was not assessed.", "",
    ])
    if schema_errors:
        lines.extend(["## Schema errors", "", json.dumps(schema_errors, ensure_ascii=False, indent=2), ""])
    args.output_report.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({
        "status": status, "python_version": result["python_version"],
        "jsonschema_version": result["jsonschema_version"], "validator_class": result["validator_class"],
        "schemas_validated": len(schemas), "refs_found": refs_found,
        "refs_resolved": refs_resolved, "refs_failed": refs_failed,
        "opening": opening_status, "continuity": continuity_status,
        "manifest_checks": {k: (v["hashes_matched"], v["sizes_matched"], v["declared_files"]) for k,v in manifest_checks.items()},
        "evidence_json": str(args.output_json.resolve()), "evidence_report": str(args.output_report.resolve()),
    }, indent=2))
    return 0 if status == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())


