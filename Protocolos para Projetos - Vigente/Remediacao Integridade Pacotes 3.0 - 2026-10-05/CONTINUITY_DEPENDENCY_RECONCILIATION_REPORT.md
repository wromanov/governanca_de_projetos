# Continuity 3.0 Dependency Reconciliation

STATUS = PASS
ACTIVITY_COMPLETION_PERCENT = 100%
STALE_REFERENCE_CLASSIFICATION = METADATA_DEPENDENCY_ALIGNMENT
VERSION_BUMP_REQUIRED = NO
CONTINUITY_VERSION = 3.0 (preserved)
NORMATIVE_CONTENT_CHANGED = NO

## Authority basis

The current `POLICY_REGISTRY.json` declares PM-02 `1.7-R2.6` and PM-03 `1.7-R2.3` as the single canonical active versions; the older versions are marked superseded/historical. Continuity 3.0 resolves governance authorities externally through the configured Matrix/Registry and carries no policy copies. The Matrix states that a compatible subpolicy revision alone does not require a protocol major revision. Therefore only the two `external_dependencies[].version` metadata values were aligned. The remaining dependencies, protocol text, schema, and package version were preserved.

## Integrity

FILES_UPDATED = `Protocolos para Projetos - Vigente/Protocolo Continuidade Projeto Em Andamento Com Novo Agente 3.0/CONTINUITY_MANIFEST.json`
FILES_CREATED = `Protocolos para Projetos - Vigente/Remediacao Integridade Pacotes 3.0 - 2026-10-05/CONTINUITY_3.0-DEPENDENCIES-RECONCILED.zip`, this report
CONTINUITY_PACKAGE_MANIFEST_HASHES_AND_SIZES = 4/4 PASS
ZIP_CRC_AND_EXTRACTION_READ = PASS
JSON_PARSE = PASS
SCHEMA_DRAFT_2020_12 = NOT_AFFECTED (schema unchanged; prior validation evidence remains applicable)
FINAL_ZIP_SHA256 = `46fabb02321aebf6b2e0bf1b7e9382c833f2895a866a4cd23a84427cccfe8bc4`
FINAL_ZIP_SIZE_BYTES = 10039

The old remediated ZIP is preserved as a record of the pre-reconciliation package. The new ZIP contains the updated manifest; the manifest lists four governed package files and excludes itself from its internal hash scope.

## Stale reference check

ACTIVE_STALE_REFERENCES_AFTER = 0
The only active dependency declarations in Continuity 3.0 now resolve to the registry's current PM-02 and PM-03 versions. The remaining textual matches are classified below. No current active dependency declaration uses a superseded version.




## Stale reference inventory

Each textual match in the repository scan is grouped by source and line; all matches in each group receive the listed classification. No stale match was found in current Continuity 3.0 or Opening 3.0 active files. The preserved pre-reconciliation archive contains the stale dependency values as historical package content.

- `Matriz Unificada de Politicas/MATRIX_BUILD_REPORT.md` - lines 64-65, 84, 125 - `EVIDENCE_ONLY`
- `Matriz Unificada de Politicas/MATRIX_BUILD_REPORT.md` - lines 119-120 - `HISTORICAL_REFERENCE`
- `Matriz Unificada de Politicas/POLICY_REGISTRY.json` - lines 55, 84, 227-228, 234, 241, 254-255, 261, 268 - `HISTORICAL_REFERENCE`
- `Matriz Unificada de Politicas/PREWRITE_AUDIT.md` - lines 16, 20, 52, 57, 64, 69, 79-81, 147-148 - `EVIDENCE_ONLY`
- `Matriz Unificada de Politicas/policies/[PM-02 current policy history]` - lines 6-7, 3245 - `HISTORICAL_REFERENCE`
- `Matriz Unificada de Politicas/policies/[PM-03 current policy history]` - lines 9, 34, 2201 - `HISTORICAL_REFERENCE`
- `PERFIL-AGENTE-GOVERNANCA-E-CONTINUIDADE.md` - lines 219-220 - `HISTORICAL_REFERENCE`
- `Protocolos para Projetos - Vigente/Remediacao Integridade Pacotes 3.0 - 2026-10-05/PROTOCOL_INTEGRITY_REMEDIATION_REPORT.md` - lines 5, 59-60 - `EVIDENCE_ONLY`
- `Protocolos para Projetos - Vigente/Remediacao Integridade Pacotes 3.0 - 2026-10-05/draft2020-12-validation-evidence.json` - lines 16, 387-388 - `EVIDENCE_ONLY`
- `Protocolos para Projetos - Vigente/Remediacao Integridade Pacotes 3.0 - 2026-10-05/draft2020-12-validation-report.md` - lines 39 - `EVIDENCE_ONLY`
- `Protocolos para Projetos - Vigente/Remediacao Integridade Pacotes 3.0 - 2026-10-05/protocol-integrity-remediation-evidence.json` - lines 570, 580, 586 - `EVIDENCE_ONLY`
- `Protocolos para Projetos - Vigente/Remediacao Integridade Pacotes 3.0 - 2026-10-05/validate_protocol_json_schemas.py` - lines 270, 320, 357 - `EVIDENCE_ONLY`
- `Quick Policies/Atuais/[PM-02 historical source]` - lines 1, 9, 3157 - `HISTORICAL_REFERENCE`
- `Quick Policies/Atuais/[PM-03 historical source]` - lines 1, 11, 33, 2178, 2188 - `HISTORICAL_REFERENCE`
- `Protocolos para Projetos - Vigente/Remediacao Integridade Pacotes 3.0 - 2026-10-05/CONTINUITY_3.0-REMEDIATED-MANIFEST-MATCHED.zip` - embedded pre-alignment manifest - `HISTORICAL_REFERENCE`
