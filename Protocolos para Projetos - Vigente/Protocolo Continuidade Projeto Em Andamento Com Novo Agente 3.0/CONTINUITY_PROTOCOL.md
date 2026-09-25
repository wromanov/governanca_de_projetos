# Continuity Protocol 3.0

```text
PROTOCOL_ID = CONTINUITY
VERSION = 3.0
STATUS = CANONICAL
LIFECYCLE = ACTIVE
CANONICALIZATION = YES
PREVIOUS_VERSION = 2.0
GOVERNANCE_CONTRACT_VERSION = 1
USER_REVIEW_REQUIRED = NO
```

## 1. Role and authority boundaries

This is an operational protocol: it specifies how to perform project recovery.
It does not define project conduct policy, project facts, validation policy,
or permission to implement. PM-01 remains the normative owner of project
continuity requirements, `AGENT_HANDOFF_GATE`, `SAFE_RESUME_POINT`, project
state requirements, and advancement/authorization boundaries. This protocol
finds evidence for those requirements and applies an operational
`CONTINUITY_RECOVERY_GATE`; it does not redefine their meaning.

VP-01 remains the validation authority and is `VALIDATION_ONLY`. Invoke the
applicable VP-01 procedure when required. Do not copy its test suite or treat
this protocol as a substitute for it. Governance authorities are resolved
externally by identity and version through the configured Governance Baseline
Matrix/Registry. This package contains no policy copies.

```text
NEXT_REQUIRED_ACTIVITY != EXECUTION_AUTHORIZATION
CONTINUITY_RECOVERY_GATE = PASS != IMPLEMENTATION_AUTHORIZATION
CONTINUITY_RECOVERY_GATE = PASS != GIT_PUBLICATION_AUTHORIZATION
RECOVERED_STATE != USER_APPROVAL_TO_ADVANCE
```

## 2. Inputs and outputs

Inputs are the project repository or governed project root, its
`PROJECT_GOVERNANCE_BINDING.json`, the project's declared continuity root,
available project authorities and state, and the relevant external governance
references. Do not infer missing paths or project state.

The recovery report identifies the selected mode, binding integrity, adopted
baseline, separately derived global baseline relation, authorities checked,
project facts and Git facts verified, missing/unverified items, contradictions,
validation performed, user validation required, operational gate, and the
evidence-based safe resume point. It reports readiness without granting the
next activity's authorization.

## 3. Binding and governance resolution

Use this sequence:

1. Discover the project root from the available workspace/repository context
   and its declared authorities. If the root cannot be established, stop
   recovery and report it as `UNVERIFIED`.
2. Locate `PROJECT_GOVERNANCE_BINDING.json` at the path declared by the
   project. Do not invent a path. A missing binding blocks normal Continuity
   3.0 recovery when the binding is required; handle legacy adoption or
   retrofit only under an explicitly authorized migration/recovery path.
3. Validate binding structure against the binding schema and check the
   governance contract version against versions supported by this execution.
   Derive `BINDING_STATUS = ACTIVE | BLOCKED`; do not persist that result.
4. Resolve every adopted authority by `id + version`, then verify its
   `sha256`. A locator/path/URI is only a resolution hint. A moved file remains
   valid if the same identity and bytes resolve unambiguously. Missing bytes,
   ambiguous identity, or a hash mismatch fail closed; never substitute a
   newer authority silently.
5. Resolve current global governance independently through the configured
   Matrix/Registry. It is for discovery, context, and migration availability;
   it is not the integrity source for the project's adopted pins. Never use
   the current global Registry hash as a project integrity pin.
6. Preserve `PROJECT_ADOPTED_GOVERNANCE` as the baseline for this recovery.
   Derive `GLOBAL_BASELINE_RELATION = CURRENT | NEWER_BASELINE_AVAILABLE |
   UNKNOWN`. If global discovery is unavailable, the relation may be
   `UNKNOWN` while verified adopted pins remain usable. A newer baseline does
   not invalidate the binding or authorize migration.
7. Separately check whether this Continuity execution supports the adopted
   governance contract and whether any explicit, authoritative withdrawal or
   incompatibility rule applies. A changed global contract does not by itself
   make an older adopted contract incompatible with this execution.

The durable identity of each adopted authority is `id + version + sha256`.
`status_at_adoption` is optional historical metadata; current global status
such as `SUPERSEDED` does not alter an intact pin by itself. The adopted
authority list must include all applicable authorities required by the
project's governance contract. The mutable Registry is not a substitute for
that list.

## 4. Project continuity discovery and factual verification

Resolve the project's continuity root from its governed project instructions.
`docs/continuity/` is the default; an equivalent root is acceptable when
explicitly governed. Prefer semantic roles over hardcoded filenames. Locate
and inspect applicable project authorities, including:

- `PROJECT_STATE` for the current reported project state;
- `ACTIVE_AUTHORITY_MAP` for active project documents and authority links;
- `CONTINUITY_RECORD` or the applicable handoff/recovery record;
- `ROADMAP` and `EXECUTION_PLAN` when relevant to the proposed resume point;
- project-specific `START_HERE` and bootstrap instructions when present.

Separate current facts from historical notes and claims. Verify repository
state using Git read-only when available. If Git is unavailable, say so and
mark affected facts `UNVERIFIED`; never claim a branch, HEAD, clean worktree,
or staging state without evidence. Do not write project state as part of
recovery unless a distinct, authorized state update is in scope.

Report each material contradiction, missing authority, hash mismatch, and
unverified fact. Do not reconcile conflicting sources silently. Apply VP-01
when required by the selected mode or the governing authorities; a self-report
of compliance is not validation evidence.

## 5. Continuity modes

### `FIRST_ADOPTION_OR_AGENT_CHANGE`

Use for first adoption, a new agent/chat handoff, or when the prior execution
cannot be trusted as the same intact binding context. Perform full discovery,
validate all adopted pins, verify project state and Git facts when available,
apply the full VP-01 procedure when applicable, and establish
`SAFE_RESUME_POINT` from verified evidence. Request user continuity validation
when PM-01, an unresolved material issue, or the recovery context requires it.

### `SAME_BINDING_RECOVERY`

Delta verification is allowed only after confirming that the same binding is
present, its structure and adopted hashes remain valid, and no material change
or contradiction affects the recovery. Recheck the changed or uncertain facts.
If these conditions cannot be established, use full discovery as
`FIRST_ADOPTION_OR_AGENT_CHANGE`.

### `GOVERNANCE_MIGRATION`

Enter only with explicit authorization recorded in the migration metadata.
Validate the declared scope and target, resolve and verify every target pin,
apply the full VP-01 procedure, reconcile the project's affected state, and
identify a safe boundary. Preserve the existing adopted pins until the target
passes validation and the authorized migration reaches that boundary. If any
precondition fails, keep the old pins and report migration as blocked. A new
global baseline or protocol alone never starts this mode.

## 6. Gate and safe resume point

The protocol may report `CONTINUITY_RECOVERY_GATE = PASS` only after required
binding and pin checks pass, material project facts are verified or explicitly
bounded, contradictions and missing evidence are reported, applicable
validation is complete, and a safe resume point is supported by evidence. If a
material blocker remains, the operational gate does not pass.

`SAFE_RESUME_POINT` is the next factual point from which work could safely
continue under PM-01. State the next required activity separately from its
authorization. After presenting recovery, obtain any user continuity
validation required by PM-01 or the circumstances. A passed recovery gate
never grants implementation, publication, deployment, or phase advancement.

## 7. Recovery report

Report, as applicable:

```text
CONTINUITY_MODE =
BINDING_STATUS = ACTIVE | BLOCKED
ADOPTED_BASELINE =
GLOBAL_BASELINE_RELATION = CURRENT | NEWER_BASELINE_AVAILABLE | UNKNOWN
ADOPTED_CONTRACT_COMPATIBILITY = PASS | FAIL | UNVERIFIED
ADOPTED_AUTHORITIES_RESOLVED =
ADOPTED_PROTOCOLS_RESOLVED =
PROJECT_CONTINUITY_ROOT =
PROJECT_STATE_VERIFICATION =
GIT_FACTUAL_STATE = VERIFIED | UNVERIFIED | UNAVAILABLE
CONTRADICTIONS =
MISSING_OR_UNVERIFIED =
VP01_VALIDATION = PASS | FAIL | NOT_REQUIRED | UNAVAILABLE
SAFE_RESUME_POINT =
NEXT_REQUIRED_ACTIVITY =
USER_CONTINUITY_VALIDATION = REQUIRED | NOT_REQUIRED | PENDING
CONTINUITY_RECOVERY_GATE = PASS | NOT_PASSED
IMPLEMENTATION_AUTHORIZATION = NOT_GRANTED_BY_RECOVERY
GIT_PUBLICATION_AUTHORIZATION = NOT_GRANTED_BY_RECOVERY
```

The runtime-derived fields above are report values, not binding fields. Report
the source and evidence for each status; use `UNKNOWN` or `UNVERIFIED` where
evidence is insufficient.
