# Project Opening Gate Record

```text
DOCUMENT_ROLE = PROJECT_OPENING_GATE_RECORD
PROJECT_ID = <stable project identifier>
PROJECT_OPENING_GATE = PASS | CONDITIONAL | BLOCKED | FAIL
RECORDED_AT = <timestamp with timezone>
OPENING_PROTOCOL = Project Opening 3.0 / CANONICAL / ACTIVE
```

## Evidence and conditions

- Foundation review:
- User foundation approval evidence:
- Project state and continuity root:
- Binding schema validation result and evidence:
- Active authority map:
- Roadmap and selected delivery unit:
- PM-01 handoff requirements:
- Continuity 3.0 recovery result:
- Unresolved blockers or explicit conditions:

## Separate status fields

- `NEXT_REQUIRED_ACTIVITY`:
- Readiness for that activity and evidence:
- Authorization for that activity and its authority (do not infer):
- `SAFE_RESUME_POINT`:
- `OPENING_CONTINUITY_HANDOFF = PASS | NOT_PASSED`:

```text
OPENING_GATE_PASS != IMPLEMENTATION_AUTHORIZATION
OPENING_GATE_PASS != GIT_PUBLICATION_AUTHORIZATION
NEXT_REQUIRED_ACTIVITY != EXECUTION_AUTHORIZATION
```

The gate record does not authorize implementation, commit, push, deployment,
production, or another reserved action.
