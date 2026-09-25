# Continuity 3.0 — Entry Point

```text
VERSION = 3.0
STATUS = CANONICAL
LIFECYCLE = ACTIVE
CANONICALIZATION = YES
GOVERNANCE_CONTRACT_VERSION = 1
USER_REVIEW_REQUIRED = NO
```

This package defines an operational recovery process. It does not contain
project state or copies of governance policies. PM-01 owns project continuity
requirements, handoff requirements, `SAFE_RESUME_POINT`, and authorization
boundaries. Continuity operationalizes those requirements; it does not replace
their normative owner.

For a project recovery:

1. Read the project's `AGENTS.md` and resolve its governed continuity root.
   The default is `docs/continuity/`; use an explicitly governed equivalent
   when the project declares one.
2. Locate and validate `PROJECT_GOVERNANCE_BINDING.json` using
   `schemas/PROJECT_GOVERNANCE_BINDING.schema.json`.
3. Follow `CONTINUITY_PROTOCOL.md` to resolve the adopted authorities and
   project artifacts by their semantic roles, including `PROJECT_STATE`,
   `ACTIVE_AUTHORITY_MAP`, `CONTINUITY_RECORD`, `ROADMAP`, and
   `EXECUTION_PLAN` when present and applicable.
4. Treat the binding's adopted governance as the project's execution baseline.
   Resolve current global governance separately; a newer global version does
   not silently replace a project's pins.
5. Use `templates/NEW_AGENT_BOOTSTRAP.template.md` when a project needs a
   history-independent recovery prompt.

Missing or ambiguous authorities remain `MISSING` or `UNVERIFIED`. This
canonical and active package does not claim project adoption or implementation
authorization. Consult the global Governance Baseline V1 references through
its configured Matrix/Registry; this package does not vendor PM-00 through
PM-05 or VP-01.
