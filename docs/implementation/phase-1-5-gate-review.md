# Phase 1.5 — Formal Gate Review And First Execution Proposal

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Review baseline | `main` at `12d8a30`; Phase 1.4 closeout and visual-planning additions published |
| Status | Accepted for planning/publication 2026-10-23; read-only 2.1 preflight explicitly authorized |
| Authority | [Implementation plan](vertical-slice-1-implementation-plan.md#phase-15-formal-gate-review-and-first-execution-scope), [Baseline v1](../reconstruction/baseline-v1/vertical-slice-1.md), [Phase 1.4 closeout](phase-1-4-closeout-review.md) |

This review reconciles existing decisions and proposes bounded next work. It performs no new host
inventory, installs, LFS configuration, project creation, engine launch, art generation or implementation.
All runtime scenarios remain unexecuted. Phase 1 planning exit is accepted for the explicitly authorized
read-only 2.1 preflight only. Installation, configuration, initialization and later execution remain
outside that authorization; documentation confirmation alone does not grant those scopes.

## Decision Reconciliation

| Decision | Accepted planning input | Gate assessment / remaining proof |
| --- | --- | --- |
| VS-D01 — entry | [Phase 1.2 closeout](phase-1-2-closeout-proposal.md), [Phase 1.3 behavior](phase-1-3-closeout-audit.md) | Selected hatch/route and independent panel/handhold/boarding behavior are sufficient for the bounded slice. H04/H05 source correspondence remains unresolved; adopted connections remain E. Physical entry proof belongs to G02/I02. |
| VS-D02 — placement/route | Phase 1.2 accepted provisional layout, required route and minimal common-area shell | Sufficient to propose grayboxing; not a final deck plan. Actual room/hull fit and source conflicts remain 3.2–3.4 work. |
| VS-D03 — machinery space | Phase 1.2 cockpit/engineering/reservation package | Cavity, seat, all-four engineering and future reservations are specified provisionally. G03, applicable MC checks and M01–M03 distinguish proxy fit from actual occupied motion. |
| VS-D04 — initial services | Phase 1.3 bounded commissioning contract | Guide lighting and laptop-triggered bootstrap precede full ignition; main ship gravity waits for ignition. No calibrated battery/reactor model is required. S/I/R checks own actual service proof. |
| VS-D05 — occupant/engineering | Phase 1.3 revival, witnessed transfer, independent four-unit preparation and reverse operation | Accepted F adaptations remain in scope. No full crew AI, fluid simulation, resealing ribbons or emergency cutoff is introduced. M/R checks own actual completion and repeatability. |
| VS-D06 — results/locality | Phase 1.3 behavior and Phase 1.4 authority/command/lifecycle contract | One authority, accepted/in-progress/completed outcomes, physical locality, stale-work rejection and current/milestone/departure separation are specified. Types/API details follow the accepted deferral schedule; S/I/M/R procedures supply proof requirements. |
| VS-D07 — tools/assets/authorization | [Phase 1.4 contracts](phase-1-4-architecture-asset-validation-draft.md), [dated inventory](phase-1-1-host-tooling-readiness.md) | Engine/toolchain direction, host, asset policy and validation are accepted planning inputs. Read-only 2.1 preflight is explicitly authorized; effective build selection is unproven. No installation/project/binary-publication permission is inferred. |

No gameplay or canonical requirement needs amendment. Baseline v1's decision-status paragraph is
reconciled with accepted Phase 1.4 contracts and the bounded 2.1 authorization, preserving all acceptance criteria.
This is a status reconciliation, not a new interpretation of source material.

## Validation And Visual-Development Coverage

- T01–T04 cover tooling, storage/retrieval, ordinary C++ build/editor proof and an early neutral package.
- G/S/I/M/R/A procedures cover spatial fit, state/lifecycle, interaction, machinery, ignition/readiness,
  full acceptance, measured performance and exact standalone reproduction. The
  [scenario register](vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability)
  remains the single ID register; approval of procedures establishes no passing results.
- Phase 3.2A supplies bounded reconstruction sheets and selected iterative concept views after the
  player/scale fixture and before room grayboxing. Targeted pre-Phase 6 refinements use observed
  layout/clearance results. These additions change neither slice scope nor source authority and do
  not block neutral Phase 2 foundation proof. No images are generated during this gate review.
- Physical fit, readability and playtest feel require observed evidence with the performer identified;
  source/configuration checks cannot certify them. Computer Use retains separate explicit permission.

## Proposed Phase 2 Operations — Separately Bounded

| Checkpoint | Proposed operation | Authorization / proof boundary |
| --- | --- | --- |
| First increment: 2.1 read-only preflight | Refresh intended engine/VS/toolset/SDK/runtime component availability and installed engine version policy; report discrepancies and candidate remedies | Recommended first scope below. No installers, defaults/configuration edits, project generation or engine launch. Availability only; T01's effective build-selection proof remains later. |
| Remaining 2.1 preparation, only if needed | Review and perform specifically agreed missing component changes | New installer scope must name components and account for dependency/storage impact. Keep side-by-side tools; do not remove 14.51 or globally force 14.50. |
| 2.2 skeleton/storage | Create the planned Blank C++ project and `L_NeutralProof`; apply repository-local owned-binary/generated policy | Requires explicit project/configuration scope and later confirmation for publication. Review exact LFS patterns/staged files, source exclusions and any paid-use cap before applicable publication/usage. No ship/player/gameplay work. |
| 2.3 ordinary build/editor | Fresh non-Live-Coding build, effective compiler/SDK evidence, observed neutral editor launch and repeat after restart | Requires scoped execution and named observation method. Do not substitute file presence for launch proof or assume foreground-control permission. |
| Optional Unreal MCP after 2.3 | Bounded neutral fixture pilot under the accepted local contract | Separate setup/enablement scope, current pinned/client/tool review and fallback; neither pilot nor Blender is needed for the first inventory increment. |
| 2.4 neutral package | Build/cook/package `L_NeutralProof`, run outside editor and repeat launch | Requires scoped build/run work. Package output stays generated/local; successful documentation publication does not authorize a public binary release. |

The table reviews the existing Phase 2 path; it does not authorize running all of it as one batch.
Phase 2 exit still requires actual T01–T04 evidence and acceptance before spatial work begins.

## Accepted First Execution Scope — Read-Only Preflight

**Purpose:** establish current availability before proposing mutations, using the primary laptop,
Win64 and the accepted UE 5.8 / VS 2026 / MSVC 14.50 / Windows SDK 10.0.26100.0 direction.

**Authorized actions:** read installed version/configuration metadata, component inventory
and representative tool/header/library availability; use bounded read-only version/component queries
where needed. Compare the current engine's preferred/banned compiler policy and report side-by-side
selection risks. Record actual commands, observations and access limits in a dated T01 preflight result.
Inspect paths on this host rather than assuming the October 7 paths or tool versions remain current.

**Explicit exclusions:** no installations/downloads, workload selection changes, compiler-default or
environment edits, LFS setup/upload, project or asset creation, builds, editor/Blender launch, MCP
registration/enablement, cache clearing, art generation or desktop control. No broad unrelated
software inventory or automatic continuation into 2.2.

**Expected deliverable:** an authored discrepancy/availability record with current versus dated
evidence distinguished, the smallest justified proposed corrections and any required decisions.
Report unavailable inspection evidence as unknown. A successful preflight cannot certify compilation.

**Recovery:** preserve installations and settings. If inspection is blocked, retain partial findings
and identify the specific missing observation; do not change permissions or installations to force
an inventory pass. Review any proposed remedy before mutation.

## Remaining Gate Items And Permitted Deferrals

| Item | Disposition / owner |
| --- | --- |
| Accept this gate reconciliation and authorize the exact first increment | Accepted 2026-10-23, with explicit authorization for the read-only 2.1 preflight only. |
| Dated .NET Desktop/MAUI and matching 14.50 ATL setup gaps | Recheck before proposing an installer selection. These are historical candidate gaps, not verified current missing components or automatic blockers. The absent engine-installer component did not prove the engine was missing. |
| Actual compiler/SDK choice, launch, package and storage retrieval | T01–T04 execution proof at Phase 2 checkpoints, not prewritten results or reasons to initialize now. |
| Source correspondence, Japanese terminology, full-ship geometry and detailed performance modeling | Parallel research; reopen only affected reconstruction decisions if new evidence conflicts. No general research restart is required for neutral foundation proof. |
| Bindings/camera tuning, classes/types, exact export/capture settings and optional controller/render/MCP trials | Retain [accepted checkpoint assignments](phase-1-4-closeout-review.md#details-that-remain-later-work). These do not authorize implementation or silently expand required acceptance. |

**Gate outcome:** Phase 1.5 planning review and Phase 1 planning exit are accepted on 2026-10-23 for
the read-only 2.1 preflight as the next independent increment. Review its findings before agreeing
any installations, configuration changes or project initialization. No later subphase starts automatically.
