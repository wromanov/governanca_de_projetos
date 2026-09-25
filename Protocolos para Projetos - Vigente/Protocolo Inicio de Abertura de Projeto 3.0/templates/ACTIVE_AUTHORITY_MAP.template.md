# Active Authority Map

```text
DOCUMENT_ROLE = ACTIVE_AUTHORITY_MAP
PROJECT_ID = <stable project identifier>
LAST_VERIFIED = <timestamp with timezone>
GOVERNANCE_BINDING = <path to PROJECT_GOVERNANCE_BINDING.json>
```

Map each material concern to its current primary authority and resolution
evidence. The binding is the source for adopted governance pins; this map is a
navigation aid and must not create a second copy of policy rules.

| Concern | Authority ID / version | Canonical location or resolver | SHA-256 / verification evidence | Status |
|---|---|---|---|---|
| Governance matrix | PM-00 / <version> | <external Matrix/Registry> | <hash / evidence> | <state> |
| Project conduct | PM-01 / <version> | <external Matrix/Registry> | <hash / evidence> | <state> |
| Applicable policy | <ID / version> | <external Matrix/Registry> | <hash / evidence> | <state> |
| Operational protocol | <ID / version> | <governed location> | <hash / evidence> | <state> |
| Project decision / contract | <role or ID> | <project canonical location> | <evidence> | <state> |

## Baseline relation

- Project-adopted baseline:
- Current global baseline discovered separately:
- Newer baseline available: `YES | NO | UNKNOWN`:
- Migration state from the binding:
- Migration authorization reference, if applicable:

A newly available global baseline does not change adopted project pins. Update
this map only when the project’s governed migration path authorizes a change.
