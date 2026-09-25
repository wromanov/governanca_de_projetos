# Project State

```text
DOCUMENT_ROLE = PROJECT_STATE
STATUS = INITIAL | ACTIVE | BLOCKED | PAUSED | CLOSED
PROJECT_ID = <stable project identifier>
STATE_VERSION = <project-managed version>
LAST_UPDATED = <timestamp with timezone>
PROJECT_ROOT = <verified project root>
CURRENT_BRANCH = <verified value or UNKNOWN>
```

This is the single current factual snapshot for the project. Keep detailed
requirements, decisions, and handoff history in their primary records and link
them here.

## Baseline and current position

- Adopted governance binding:
- Current phase:
- Current delivery unit and identifier, if applicable:
- Current activity:
- Last completed activity:
- Baseline traceability and adopted binding:
- Current project authorities and invariants:
- Last validated integrated baseline:

## Next step

- `NEXT_REQUIRED_ACTIVITY`:
- Readiness: `READY | CONDITIONAL | NOT_READY | UNKNOWN` (explain):
- Implementation authorization state and governing evidence (do not infer):
- Git publication authorization state and governing evidence (do not infer):
- `SAFE_RESUME_POINT`:

## Current authorities and plans

- Active authority map:
- Roadmap:
- Execution plan / delivery-unit plan, if applicable:
- Continuity record:

## Open work

- Open decisions:
- Blockers:
- Known risks:
- Deferred items:
- `EXACT_CURRENT_HEAD`: discover at runtime when Git is available; otherwise
  `UNAVAILABLE` or `UNVERIFIED`.

## Risks, blockers, and open decisions

| Item | Status | Owner / evidence needed | Effect on next step |
|---|---|---|---|

## Continuity and handoff

- Continuity root and entrypoint:
- Last handoff, if applicable:
- Continuity recovery status:
- Known stale or contradictory state:
