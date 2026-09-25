# Project Opening 3.0 — Entry Point

```text
VERSION = 3.0
STATUS = CANONICAL
LIFECYCLE = ACTIVE
CANONICALIZATION = YES
PREVIOUS_VERSION = 2.0
GOVERNANCE_CONTRACT_VERSION = 1
USER_REVIEW_REQUIRED = NO
```

This package operationalizes project opening. It does not own project conduct
rules, governance policies, validation policy, project-specific facts, or
authorization. Resolve those authorities externally and follow
`OPENING_PROTOCOL.md` and `OPENING_WIZARD.md`.

## Read and resolve authorities

1. Resolve the active Governance Baseline Matrix and `POLICY_REGISTRY.json` at
   the governed governance root. In this workspace they are under
   `../../Matriz Unificada de Políticas/`.
2. Load PM-00, PM-01, and every other policy applicable to the project through
   the current registry. Use VP-01 only when the governing process requires
   validation.
3. Read the separate Continuity 3.0 candidate at
   `../Protocolo Continuidade Projeto Em Andamento Com Novo Agente 3.0/`.
   Reuse its `schemas/PROJECT_GOVERNANCE_BINDING.schema.json` and its bootstrap
   template when applicable; do not copy them into this package.
4. Read the project’s own instructions and factual sources. Do not infer its
   identity, paths, authority, state, or permissions from this package.

The governance root and authority files must be resolved unambiguously. Missing
or conflicting material authority stays `UNVERIFIED` or `BLOCKED`; do not
substitute a newer global version for a project’s adopted pins without an
explicitly authorized migration.

## Operate the opening

- Start with the user’s intent and discover only material gaps.
- Follow the sequence in the Wizard, adapting questions and artifacts to the
  project’s domain and risk.
- Use PM-01 as the owner for project conduct, planning, delivery units,
  integration, frontend-first applicability, continuity, handoff, and
  authorization boundaries.
- Materialize only artifacts that apply. The continuity root defaults to
  `docs/continuity/` unless project governance declares an equivalent.
- Validate the foundation, obtain explicit user foundation approval, pass the
  Project Opening Gate, then hand off to Continuity 3.0.

`PROJECT_OPENING_GATE = PASS` does not authorize implementation, Git
publication, deployment, production, or another reserved action. A listed
`NEXT_REQUIRED_ACTIVITY` is not execution authorization. Opening may remain as
historical evidence; it need not remain an active operational protocol after
handoff.

## Package contents

- `OPENING_PROTOCOL.md` — scope, boundaries, and opening-to-continuity contract.
- `OPENING_WIZARD.md` — executable conversational sequence.
- `templates/` — small, conditional project-artifact templates.
- `OPENING_MANIFEST.json` — package metadata, external dependencies, and
  package hashes (the manifest excludes its own hash).
- `VALIDATION_EVIDENCE.md` — package checks and requested documentary dry-runs.

Opening 2.0 is preserved as a legacy rollback package and is superseded by
this canonical and active 3.0 package.
