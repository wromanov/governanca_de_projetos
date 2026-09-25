# Continuity Record

```text
DOCUMENT_ROLE = CONTINUITY_RECORD
PROJECT_ID = <stable project identifier>
LAST_UPDATED = <timestamp with timezone>
PROJECT_GOVERNANCE_BINDING = <path to binding>
PROJECT_STATE = <path to the single current state record>
```

Keep only recovery context not already authoritative elsewhere. Link to the
project state, active authority map, roadmap, execution plan, and durable
decisions instead of copying their contents.

## Recovery context

- Current project objective and relevant boundary:
- Last completed material activity and evidence:
- Current material activity and status:
- Decisions that remain in force and their canonical records:
- Open decisions, risks, blockers, and deferred items:

## Last handoff

- Latest handoff record: <canonical path, or this record if that role is
  intentionally combined>:
- Handoff date and participants or agents by role:
- Material changes since prior handoff:

## Safe resume point

- Canonical `SAFE_RESUME_POINT` location in `PROJECT_STATE`:
- Last verified point and evidence reference:
- Required preflights, approvals, or gates reference:

Do not repeat the current state, next activity, readiness, authorization, or
safe resume point already recorded in `PROJECT_STATE`; link to its canonical
location above.

## Verification

- Project governance binding and adopted pin integrity:
- Active authority map and current policy resolution:
- Project state freshness:
- Git facts, if available, with read-only evidence:
- Contradictions or unverified facts:
