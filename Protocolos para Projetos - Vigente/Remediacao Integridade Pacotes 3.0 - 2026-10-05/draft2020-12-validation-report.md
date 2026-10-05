# JSON Schema Draft 2020-12 validation

STATUS = PASS
ACTIVITY_COMPLETION_PERCENT = 100%
COMPLETION_BASIS = Draft 2020-12 schema check, all required refs, package ZIP hashes, extracted bytes, and manifests passed.
FILES_CREATED = draft2020-12 evidence JSON/Markdown, validator Python, runner PowerShell, pinned requirements.
FILES_UPDATED = NONE
FINDINGS = No schema fixtures to validate; no normative policy refs changed; Opening resolves the validated sibling Continuity schema.
BLOCKERS = NONE for this technical validation.
NEXT_REQUIRED_ACTIVITY = Separate normative review of stale active PM-02/PM-03 references before Continuity authority adoption.
PROJECT_OPENING_GATE = NOT_ASSESSED
VALIDATION_TIMESTAMP = 2026-10-05T18:19:48.530511-03:00
PYTHON_VERSION = 3.13.1
JSONSCHEMA_VERSION = 4.26.0
REFERENCING_VERSION = 0.37.0
VALIDATOR_CLASS = jsonschema.Draft202012Validator
DRAFT_2020_12_VALIDATOR_USED = YES
FILES_VALIDATED = 19 ZIP entries; 3 JSON documents parsed
SCHEMAS_VALIDATED = 1/1
INTERNAL_REFS_FOUND = 9
INTERNAL_REFS_RESOLVED = 9
INTERNAL_REFS_FAILED = 0
OPENING_SCHEMA_VALIDATION = PASS
CONTINUITY_SCHEMA_VALIDATION = PASS
PROJECT_GOVERNANCE_BINDING_SCHEMA = PASS

## Schema inventory

SCHEMA_ID = PROJECT_GOVERNANCE_BINDING.schema.json
FILE = continuity::schemas/PROJECT_GOVERNANCE_BINDING.schema.json
DECLARED_DRAFT = https://json-schema.org/draft/2020-12/schema
REF_COUNT = 9
REFS_RESOLVED = 9
CHECK_SCHEMA = PASS
RESULT = PASS

Opening 3.0 has no embedded schema; its declared sibling Continuity schema dependency resolved and passed validation.
No normative instance fixtures were present, so no positive/negative instances were invented.
PM-02 R2.5 and PM-03 R2.2 references were left unchanged. PROJECT_OPENING_GATE was not assessed.
