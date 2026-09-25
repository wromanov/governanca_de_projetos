# Project Opening Protocol 3.0

```text
PROTOCOL_ID = PROJECT_OPENING
VERSION = 3.0
STATUS = CANONICAL
LIFECYCLE = ACTIVE
CANONICALIZATION = YES
PREVIOUS_VERSION = 2.0
GOVERNANCE_CONTRACT_VERSION = 1
USER_REVIEW_REQUIRED = NO
```

## 1. Purpose and authority boundary

This is an operational protocol for taking a project from intent to an
approved, documented foundation and a controlled handoff. The distinction is:

```text
POLICY = WHAT MUST BE TRUE
PROTOCOL = HOW TO EXECUTE A PROCESS
PROJECT AUTHORITY = PROJECT-SPECIFIC FACTUAL STATE
```

Governance Baseline V1, its Matrix and Registry, PM-01, other applicable
policies, VP-01 when required, and Continuity 3.0 remain external authorities.
This package resolves and applies them; it does not reproduce them or define a
second owner for their rules. In particular, PM-01 remains the owner of project
conduct, planning, DoR/DoD, incremental integration, frontend-first
applicability, continuity requirements, Agent Handoff Gate, Safe Resume Point,
and authorization boundaries.

Opening 2.0 and Continuity 2.0 are preserved as legacy rollback packages and
are superseded by their respective 3.0 packages. Opening 3.0 and Continuity
3.0 are `CANONICAL / ACTIVE` following the user's GOV-04 canonicalization
approval.

## 2. External authority discovery

Before project-specific decisions:

1. Find the governed governance root and load the current PM-00 Matrix and
   `POLICY_REGISTRY.json`.
2. Resolve PM-01 and other policies by their registered identity, version,
   status, and applicable scope. Load VP-01 only when required by the
   applicable validation authority or procedure.
3. Read the Continuity 3.0 candidate and confirm its supported governance
   contract. Reuse its binding schema; do not make an Opening-owned schema.
4. Record the project’s adopted authorities and protocols in its binding only
   when a real project is being opened. Resolve the adopted bytes by
   `id + version + sha256`, with evidence references where applicable.
5. Keep current global governance discovery separate from project-adopted
   pins. A newly available baseline does not silently migrate a project.

Registry locations and other authorities are resolution inputs, not files to
vendor. If an authority cannot be identified or its bytes cannot be verified,
record the gap and block the affected decision or gate.

## 3. Opening process

The Wizard uses this conceptual sequence, returning to an earlier step when new
evidence changes a material decision:

```text
INTENT
→ DISCOVERY
→ REQUIREMENTS
→ GOVERNANCE
→ ARCHITECTURE
→ ENGINEERING FOUNDATION
→ ROADMAP
→ DELIVERY PLAN
→ DOCUMENTATION
→ PROJECT STATE
→ FOUNDATION REVIEW
→ PROJECT OPENING GATE
→ HANDOFF TO CONTINUITY
```

The sequence is adaptive. It is not a universal form or a mandate to create
every possible document. For each material choice, distinguish fact, evidence,
requirement, constraint, preference, hypothesis, proposal, recommendation,
decision, deferred item, unknown, and not-applicable status as appropriate.
Ask only for information that could change scope, requirements, authority,
architecture, risk, delivery, a gate, or the handoff. Keep project facts in
project-owned records, not in this package.

### Opening stages

- **Intent and discovery:** understand the problem, users or consumers,
  outcomes, constraints, existing assets, risks, and uncertainty. Do not jump
  to a solution or delivery schedule before the need is understood.
- **Requirements:** record material functional and non-functional needs,
  acceptance evidence, dependencies, scope, non-goals, and unresolved items.
- **Governance:** identify decision owners, project authorities, applicable
  global policies, constraints, and permission boundaries. Obtain the user's
  approval for reserved project decisions; a recommendation is not approval.
- **Architecture:** compare viable approaches against requirements, evidence,
  constraints, risks, and reversibility. Persist material decisions in the
  project's own source of truth.
- **Engineering foundation:** decide only the quality, security, safety, data,
  interface, operations, and validation controls that apply to the project.
  Mark non-applicability with a brief rationale.
- **Roadmap and delivery plan:** derive phases, dependencies, increments,
  acceptance, and gates from project value and constraints. Select
  `DELIVERY_UNIT` under PM-01; Sprint is not universal. Use an `EXECUTION_PLAN`
  or sprint artifacts only when applicable.
- **Documentation and state:** create the minimum project-owned records needed
  to communicate approved decisions, current facts, authorities, readiness,
  authorization, and the safe handoff. Opening notes are evidence of the
  opening process, not a second `PROJECT_STATE`.
- **Foundation review and gate:** review material findings and applicable
  gates, obtain explicit user foundation approval, and record the gate result.
  Unresolved material conflicts or missing mandatory evidence block a pass.

## 4. UI/UX and delivery applicability

Assess frontend-first applicability using PM-01; Opening does not define a
parallel rule. For a user-facing project, preserve the PM-01 model of UI/UX
first and incremental front-to-back integration. This does not require
finishing every frontend surface before backend work starts. Backend work may
support a slice when needed, and the user-facing flow is integrated and
validated incrementally.

For headless services, libraries, CLIs, background workers, infrastructure
components, and data pipelines, frontend-first may be `NOT_APPLICABLE` when no
user-facing frontend is required. Record the applicability rationale and
follow PM-01 for any foundational work that must precede a user-facing slice.

Choose the project’s `DELIVERY_UNIT` according to PM-01. A Sprint may remain a
convenient default for conventional software work; it is never required solely
because this opening process is used. Requirements, roadmap, and execution
plan must remain meaningful with a milestone, iteration, continuous flow,
experiment, research campaign, or another PM-01-supported choice.

## 5. Project continuity package

Use the governed project continuity root; the default is `docs/continuity/`.
Create or identify, by semantic role and only where applicable:

- `PROJECT_GOVERNANCE_BINDING`, instantiated as
  `PROJECT_GOVERNANCE_BINDING.json` and validated with the schema in the
  Continuity 3.0 package;
- `PROJECT_STATE`, the single current factual project snapshot;
- `ACTIVE_AUTHORITY_MAP`, mapping active authority by concern and location;
- `CONTINUITY_RECORD`, containing the information needed to recover decisions,
  current work, risks, and unresolved items;
- `NEW_AGENT_BOOTSTRAP`, using the Continuity 3.0 template where useful;
- `ROADMAP` and `EXECUTION_PLAN` (or applicable delivery-unit records);
- `LAST_HANDOFF` when a distinct handoff record is required; and
- an evidence-based `SAFE_RESUME_POINT` plus separate readiness and
  authorization states.

Project instructions must make the continuity root discoverable. Its
`START_HERE` is a navigation page that points to the semantic roles and their
locations; it is not another `PROJECT_STATE`. A project may combine compatible
roles in one canonical record when doing so avoids duplicate facts and still
leaves each required role discoverable. Templates in this package are optional
starting points, not universal document requirements.

The binding records the adopted baseline, applicable authorities and adopted
operational protocols with their `id`, `version`, and exact `sha256`; record
adoption evidence when available and migration state. Do not create a binding
for an actual project as part of building or validating this package.

## 6. Gate, handoff, and authorization

`PROJECT_OPENING_GATE = PASS` means the opening foundation passed its applicable
review, the required project artifacts are discoverable, explicit user
foundation approval is recorded, and the handoff to Continuity 3.0 is ready. It
transfers operational recovery to Continuity; it does not approve the next
activity.

Before handoff, verify the semantic contract end to end:

```text
OPENING 3.0
→ PROJECT OPENING GATE
→ PM-01 HANDOFF REQUIREMENTS
→ PROJECT CONTINUITY PACKAGE
→ CONTINUITY 3.0
→ CONTINUITY RECOVERY
→ SAFE RESUME POINT
```

The receiving Continuity recovery must be able to locate and verify the
binding, adopted authorities and protocols, project state, active authority
map, continuity record, roadmap, applicable execution plan, bootstrap, current
readiness and authorization state, and safe resume point. Missing or
contradictory evidence is reported rather than guessed.

```text
OPENING_GATE_PASS != IMPLEMENTATION_AUTHORIZATION
OPENING_GATE_PASS != GIT_PUBLICATION_AUTHORIZATION
NEXT_REQUIRED_ACTIVITY != EXECUTION_AUTHORIZATION
```

Do not state that implementation, commit, push, deployment, production, or
another reserved activity is authorized merely because Opening Gate passed.
Resolve readiness and authorization under PM-01, project governance, and the
applicable next gate. After successful handoff, Opening need not remain an
active operational pin; preserve its records only as historical evidence when
useful.

## 7. Pause, conflict, and recovery

Keep unresolved material decisions and contradictory evidence visible. Do not
silently choose between competing authorities or facts. Pause at the narrowest
safe boundary, record what remains unverified, who or what must resolve it, and
the next required activity. On resume, reload the project’s durable records
and revalidate changed facts; chat history is not a state source.

## 8. Conformance and package status

This protocol is operational, domain-neutral, and subordinate to applicable
policies. The companion Wizard and templates do not create independent
authority. The package is `CANONICAL / ACTIVE`; GOV-04 records the completed
user review and canonicalization. This status does not claim project adoption
or grant implementation authorization.
