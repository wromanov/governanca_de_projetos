# Project Opening Wizard 3.0

```text
VERSION = 3.0
STATUS = CANONICAL
LIFECYCLE = ACTIVE
CANONICALIZATION = YES
GOVERNANCE_CONTRACT_VERSION = 1
USER_REVIEW_REQUIRED = NO
```

This is an adaptive conversational procedure. Follow the operational
boundaries in `OPENING_PROTOCOL.md`; PM-01 owns project conduct and continuity
requirements. Do not turn these steps into a fixed questionnaire or request
information the user has already supplied unless new evidence creates a
material gap.

## 0. Load the external baseline

Resolve the project root and governed governance root. Read PM-00 and the
current Registry, PM-01, policies applicable to the project, and the separate
Continuity 3.0. Consult VP-01 when required. Record identities and
resolution evidence. Do not copy the policies, Continuity protocol, or binding
schema into a project or this package. Keep global baseline discovery distinct
from project-adopted pins. A newer global baseline is not a migration.

**Gate:** authority and contract versions resolve unambiguously; otherwise
record `UNVERIFIED`/`BLOCKED` and stop the affected decision.

## 1. Capture intent and discover the problem

Reflect back the user’s intended outcome, audience or consumers, problem,
known constraints, existing work, and success evidence. Identify only material
gaps. Keep solution preferences separate from requirements and avoid choosing
architecture or cadence prematurely.

**Gate:** purpose and initial boundaries are sufficiently clear to specify
requirements. Carry uncertainty forward explicitly when it does not block.

## 2. Define requirements and scope

Record material requirements with an identifier, source, priority, acceptance
evidence, dependencies, and status. Define in-scope, out-of-scope, conditional,
future, and non-goal items. Ask about gaps that could change value, boundaries,
risk, or acceptance.

**Gate:** the intended first value can be described and no material hidden scope
conflict remains.

## 3. Resolve governance and decision boundaries

Identify project decision owners, approval needs, project-specific authorities,
applicable policies, operational protocols, and constraints. Map each concern
to its authority. Obtain explicit user approval for reserved project
decisions; do not infer permission from user preference, tool availability, or
an agent recommendation.

**Gate:** authority and approval boundaries are clear enough for architecture
and planning. Material policy conflict blocks progression.

## 4. Establish architecture and engineering foundations

Compare plausible architecture choices against requirements, evidence,
constraints, trade-offs, risks, and reversibility. Record material decisions
once in their project-owned source of truth. Decide applicable engineering,
quality, security, safety, data, integration, and operations controls
proportionally. Do not create an ADR, policy, or technical artifact without a
real need.

Assess user-facing applicability under PM-01. For user-facing projects, plan
UI/UX first and incremental front-to-back integration; do not postpone all
backend work until a complete frontend is finished. For headless, CLI, library,
background-worker, infrastructure, or data-pipeline projects, record
`NOT_APPLICABLE` with a short rationale when there is no user-facing frontend.

**Gate:** the first meaningful increment can be built without inventing a
critical boundary, contract, or invariant, and material risks have proportionate
controls.

## 5. Set the roadmap and delivery plan

Define direction, phases, dependencies, milestones, and expected outcomes.
Select the appropriate `DELIVERY_UNIT` under PM-01. Sprint is not a universal
requirement. Plan slices or activities with purpose, prerequisites, output,
acceptance, validation, and applicable gates. Keep an unselected future
increment separate from readiness or authorization.

**Gate:** roadmap and execution model are defined and support the project’s
actual delivery unit.

## 6. Materialize project documents and continuity

Use the smallest set of project-owned records that makes approved decisions,
project state, authorities, risks, plans, and handoff discoverable. Select
templates conditionally. At minimum, prepare the applicable continuity
semantic roles under the governed root (default `docs/continuity/`):

- governance binding, validated against the Continuity 3.0 schema;
- project state, active authority map, continuity record, and roadmap;
- execution plan or delivery-unit records when applicable;
- bootstrap and last handoff when needed; and
- a factual safe resume point with readiness and authorization states.

`START_HERE` is navigation. Keep current factual project state in one primary
`PROJECT_STATE`, never in an opening status page or a duplicate continuity
record. Instantiate the binding only for a real project; GOV-03 builds no
project binding.

**Gate:** materialized files exist at governed canonical targets, are
discoverable, and agree with the evidence. Proposed writes or a ready-to-write
state do not count as persisted project state.

## 7. Review, approval, and Project Opening Gate

Review purpose, scope, requirements, governance, architecture, engineering,
quality and risk controls, roadmap, delivery unit, documentation, continuity,
project state, external authorities, and unresolved items. Use VP-01 where
required. Fix local, bounded findings and repeat the affected review; a
material change requires proportional rereview.

Present the foundation and remaining non-blocking items to the user. Obtain
explicit foundation approval and record the evidence. Silence is not approval.
Then determine the Opening Gate using applicable project and PM-01 conditions.

`PROJECT_OPENING_GATE = PASS` does not grant implementation, Git publication,
deployment, production, or other reserved action. Report readiness separately
from authorization. `NEXT_REQUIRED_ACTIVITY` is not execution authorization.

## 8. Handoff to Continuity 3.0

Before handoff, validate PM-01 handoff requirements by semantic role, confirm
the binding uses the Continuity 3.0 schema, and confirm project artifacts are
independently recoverable without this chat. Open Continuity 3.0 recovery and
verify that it can resolve the adopted authorities, factual project state,
current roadmap and execution plan when applicable, current authorization
state, and safe resume point.

Record missing or conflicting evidence as a failed or blocked handoff. On
`OPENING_CONTINUITY_HANDOFF = PASS`, Continuity becomes the active operational
recovery process. Opening may be retained as historical evidence and need not
remain an operational protocol pin by default.

## 9. Resume and close

On pause or new-agent transition before handoff, save the opening record,
current phase, completed gates, approved decisions, open items, contradictions,
evidence, and next required activity to durable project artifacts. On resume,
read those artifacts and verify current facts; do not depend on chat history.

Close the opening only after state is persisted, the applicable Opening Gate
has a recorded outcome, explicit user foundation approval is evidenced, and
the Continuity handoff is accepted. Preserve remaining authorization as
ungranted unless a separate authority explicitly grants it.
