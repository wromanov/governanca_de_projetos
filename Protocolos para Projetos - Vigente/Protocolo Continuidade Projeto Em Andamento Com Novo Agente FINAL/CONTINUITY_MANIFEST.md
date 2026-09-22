# Agent Continuity Standard v1.0 — Reconciled Continuity Manifest

MANIFEST_TYPE = CONTINUITY_DISTRIBUTION_AND_INTEGRITY_RECORD
MANIFEST_VERSION = 2.0
DOCUMENT_STATUS = CANONICAL
CONTINUITY_AUTHORITY_CANONICALIZATION = PASS
ACTIVE_POLICY_SET = RECONCILED_TRANSVERSAL_POLICIES
HISTORICAL_FILES_PRESERVED = YES
STALE_AUTHORITY_REFERENCES = 0

The continuity package consumes these active policy files:

| Relative path | SHA256 | Role |
|---|---|---|
| `Agent-Continuity-Standard-v1.0/policies/AGENTS-Multiagente-Generico-v1.7-R2.1-Roteamento-Economico.md` | `1C105615109EDAA5F2130803F68C9625E7DC555E62375E669D10AAE9C333BD43` | CANONICAL_POLICY |
| `Agent-Continuity-Standard-v1.0/policies/Independencia-Analitica-Agente-v1.md` | `D668DE8BDAEEA16403F4909678448B59705F094302BC2FE90203C2F3CC62A94E` | CANONICAL_POLICY |
| `Agent-Continuity-Standard-v1.0/policies/Politica-de-Uso-de-Skills-Codex-Work-v1.1.md` | `3704A9DA77E090980B05127C5760EE6F4B4ACD5EB405074D3ADEA6FF4227D405` | CANONICAL_POLICY |
| `Agent-Continuity-Standard-v1.0/policies/Politica-Prompts-Agente-v1.7-R2.4.md` | `9B08E1F6D7CF4A1A221CA9D5DF1E71574F3E9A5299986AF183B4C93F39D8EF54` | CANONICAL_POLICY |
| `CANONICAL_POLICY_MAP.md` | — | AUTHORITY_MAP |

`Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` and
`Politica-Prompts-Agente-v1.4.md` remain only as historical compatibility
records. R2.3 is superseded by R2.4 and is not an active dependency.
