# New Agent Bootstrap — Project Continuity

This template is generic. It contains no project state and does not grant
implementation authority. It must work without access to chat history.

```text
FIRST_RESPONSE_MODE = READ_ONLY_RECOVERY
CONTINUITY_MODE = FIRST_ADOPTION_OR_AGENT_CHANGE
CONTINUITY_RECOVERY_GATE = NOT_PASSED
USER_CONTINUITY_VALIDATION = PENDING
IMPLEMENTATION_AUTHORIZATION = NOT_GRANTED_BY_RECOVERY
GIT_PUBLICATION_AUTHORIZATION = NOT_GRANTED_BY_RECOVERY
```

Begin by discovering facts from the current project workspace and its declared
authorities. Read the project's `AGENTS.md` when present; resolve its declared
repository and continuity root. Do not infer paths from this template. The
default continuity root is `docs/continuity/`; use a governed equivalent when
the project explicitly declares one.

Locate `PROJECT_GOVERNANCE_BINDING.json` at the project-declared location and
validate it with the applicable binding schema. Resolve the project's adopted
baseline and operational protocol pins by `id + version`, verify each SHA-256,
and use paths only as resolution hints. Treat current global governance as a
separate discovery result. Do not replace the project's adopted baseline or
protocol with a newer global version. Report binding failures, unresolved
authorities, missing evidence, and unknown facts explicitly.

Read `START_HERE.md` and follow the adopted Continuity Protocol. Discover
project authorities by their semantic roles, including `PROJECT_STATE`,
`ACTIVE_AUTHORITY_MAP`, `CONTINUITY_RECORD`, `ROADMAP`, and `EXECUTION_PLAN`
when present and applicable. Verify current facts; use Git read-only when
available and mark unverifiable repository facts as `UNVERIFIED`. Resolve
external governance references through the global Matrix/Registry and PM-01;
do not copy governance policies into this project bootstrap.

For the first response, explain the recovered state, evidence, outstanding
blockers, contradictions, missing or unverified facts, and proposed
`SAFE_RESUME_POINT`. Apply the full validation procedure required by the
adopted protocol and invoke VP-01 when applicable. Request user validation
when required. Do not implement, edit project state, advance phases, or publish
Git changes under this recovery prompt.

Keep these distinctions explicit:

```text
NEXT_REQUIRED_ACTIVITY != EXECUTION_AUTHORIZATION
CONTINUITY_RECOVERY_GATE = PASS != IMPLEMENTATION_AUTHORIZATION
CONTINUITY_RECOVERY_GATE = PASS != GIT_PUBLICATION_AUTHORIZATION
RECOVERED_STATE != USER_APPROVAL_TO_ADVANCE
```
