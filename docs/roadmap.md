# Roadmap

## Current stage — Phase 3.1 complete; 3.2A unstarted

Phase 0 bootstrap and subsequent user-approved reference increments established source protection, evidence records and a planning foundation. Approval is scoped to the work below; it is not general implementation authorization.

The reference/research foundation is **substantially complete for implementation purposes within Slice 1**. Enough evidence exists to define a bounded initial build; this is not a claim of complete canon verification, final geometry or a tested engine project. Unresolved research continues in [open questions](reconstruction/open-questions.md) as an ongoing parallel track, targeted when it affects concrete choices.

Completed and previously confirmed:

- Repository/bootstrap documentation, source inventories and full 221-scan settei screening.
- User-installed Python/Pillow, FFmpeg/FFprobe and optional ImageMagick verification. Additional installation remains a user discussion.
- Selected interior, identity, variant and propulsion-label reviews; 66 XGP/support records in scope, 22 still lacking a focused individual pass. Full annotation/transcription is unfinished.
- All-26-episode gallery timestamp cache; accepted bounded navigation mappings for selected regions of Episodes 1–4. Direct matches, estimates and unmapped regions remain distinct in the [timing workflow](../reference/indexes/animehistory/README.md).
- User-authorized targeted Episode 4/7/8/11/26 frame reviews and metadata; derivatives remain local-only.
- All-26-episode English full-dialogue subtitle performance screening, 47 curated records and separately classified numerical inferences; Japanese audio and priority visual checks remain open.
- Shared command/state and future external-control compatibility requirements, without adapters, transport or AI implementation.

Evidence/history remain in [reference progress](reconstruction/reference-phase-progress.md), [reference index](reconstruction/xgp-reference-index.md) and [performance audit](../reference/indexes/performance-subtitle-audit.md).

The retrospective [Episode 4 reconciliation](../reference/indexes/episode-04-reconciliation-review.md)
updates the initial survey and its documentation, accepted by the maintainer on 2026-10-29. It adds translated scene
context and bounded timing references, without changing accepted spatial/behavior contracts or
authorizing Phase 3.2A. Its workbook and archive-retention checks are recorded with the findings.

## Reconstruction / Implementation Baseline v1 — documentation approved

The user approved this documentation increment on 2026-10-07. Four deliverables:

1. [Spatial constraint map](reconstruction/baseline-v1/spatial-constraint-map.md): source-backed relationships, provisional region groups, distinct hatch records and unknown connections; not a deck plan.
2. [Motion/clearance envelopes](reconstruction/baseline-v1/motion-clearance-envelopes.md): reserve volumes and later interference checks; no modeled sweeps or invented dimensions.
3. [Operational state baseline](reconstruction/baseline-v1/operational-state-baseline.md): separate commissioning, standby departure, sub-ether and emergency sequences; supported observations versus inferred/TBD dependencies.
4. [Vertical Slice 1 — Awakening the Outlaw Star](reconstruction/baseline-v1/vertical-slice-1.md): dormant entry/startup ending at SHIP READY, scope, observable acceptance criteria and decisions before implementation.

Baseline v1 consolidates the accepted direction into a reviewable planning contract. The user confirmed publication of the baseline and documentation/tooling updates on 2026-10-07. It does not create Unreal content, model geometry or implement systems.

## Engine/toolchain direction — recorded, not build-validated

UE **5.8** is intended unless later testing supplies a reason to revisit it; the preflight identified installed **5.8.4** despite stale launcher metadata. The selected toolchain is **Visual Studio Community 2026 + MSVC 14.50**, with installed **Windows SDK 10.0.26100.0** as the SDK candidate. The [2026-10-23 post-installation check](implementation/phase-2-1-closeout.md) identifies VS **18.11.1** and resolves the three selected .NET Desktop/MAUI/14.50 ATL setup gaps. Patched MSVC 14.50 remains alongside 14.51. [Unreal strategy](architecture/unreal-strategy.md) distinguishes current findings from the [earlier readiness record](implementation/phase-1-1-host-tooling-readiness.md). Phase 2.1 closeout is accepted; effective build selection is not yet proven.

## Phased implementation plan — accepted planning baseline

The user subsequently requested the [expanded Vertical Slice 1 implementation plan](implementation/vertical-slice-1-implementation-plan.md), superseding the prior hold on introducing the planning gate. Baseline v1 remains authoritative. The plan owns decimal subphases, dependencies, validation/evidence, recovery and acceptance checkpoints:

1. Formal planning gate and concrete VS-D01–07 decisions.
2. Approved toolchain preparation and minimal C++ project/build/package proof.
3. Spatial/player graybox and motion reservations.
4. Authoritative state, commands and lifecycle, independently reviewable after Phase 2.
5. Physical interaction, entry and initial services.
6. Placeholder-occupied apparatus, seating and four engineering-cylinder endpoints.
7. Cockpit ignition, derived SHIP READY and repeatable fresh runs.
8. Complete acceptance, measured budgets, standalone package and maintainer handoff.

The user confirmed the plan/MCP additions on 2026-10-07 and subsequently accepted Phases 1.1–1.3.
The dated readiness inventory selects laptop, Win64, keyboard/mouse, no initial desktop validation,
and native 1440p/60 FPS required, with 120 FPS as a stretch goal pending measurement (revised in Phase 1.4). Spatial choices remain provisional pending fit; behavior
contracts are accepted but unimplemented. Phase 1.4 planning closeout is recorded below; later phases require their own scope. Project creation,
installations/modeling and build proof retain their authorization boundaries.

[Blender/Unreal MCP evaluation](architecture/editor-automation.md) is now included in Phase 1.4
tool/asset decisions, an optional Unreal pilot after 2.3 ordinary build/editor proof, and an optional
Blender pilot after 3.1 before repeated geometry production. Both have explicit validation/recovery and
fallbacks; neither is required by the playable slice. No connector installation or activation is authorized
by this documentation addition.

On 2026-10-11 the user selected local MCP pilots for both editors under the
[local editor-automation contract](architecture/editor-automation.md#current-local-pilot-contract--accepted-2026-10-11).
Sandbox/VM work is deferred; its source/host findings remain reference material. This changes the
planning path, not installation/enablement authorization or the pilots' later execution checkpoints.

## Current Planning And Later Execution Boundaries

On 2026-10-10 the user authorized Phase 1.4 planning/discussion. Its
[architecture/asset/validation draft](implementation/phase-1-4-architecture-asset-validation-draft.md)
records accepted architecture, asset/recovery, handoff, proxy, performance, rendering-learning and
validation contracts. Map identifiers and the [deferral schedule](implementation/phase-1-4-closeout-review.md#details-that-remain-later-work)
were accepted on 2026-10-23. All seven planning items have accepted coverage; Phase 1.4 planning
closeout was accepted on 2026-10-23. Slice runtime acceptance remains unexecuted; neutral foundation
build/editor/input and recovery proof have since passed in 2.3. Phase 1.5
[gate review](implementation/phase-1-5-gate-review.md) is accepted, with explicit authorization on
2026-10-23 for the read-only 2.1 tooling preflight. Subsequent scoped owner-run VS installations were
verified read-only; [Phase 2.1 closeout](implementation/phase-2-1-closeout.md) was accepted on 2026-10-23.
Phase 2.2 skeleton/repository setup and its [closeout](implementation/phase-2-2-closeout.md) were accepted
on 2026-10-23. Subsequently authorized 2.3 build/editor and Unreal MCP work is complete, with
[closeout accepted](implementation/phase-2-3-closeout.md). Subsequently authorized 2.4 package and
first/repeat standalone checks passed, with [closeout accepted](implementation/phase-2-4-closeout.md). Later
subphases and modeling/gameplay remain outside that scope. Unreal MCP follows ordinary 2.3 build/editor proof; Blender
MCP follows the 3.1 player/scale fixture, each as a separately scoped optional local pilot.

The [Phase 2 foundation exit](implementation/phase-2-exit-review.md) was accepted on 2026-10-23.
Authorized Phase 3.1 player/scale and local Blender MCP/handoff checks passed on 2026-10-24.
The [3.1 closeout review](implementation/phase-3-1-closeout.md) records acceptance and publication;
[published asset recovery](implementation/validation/phase-3-1-recovery-results.md) passed and its
temporary checkout was deleted. Phase 3.1 is closed. No 3.2A execution is authorized.

The user authorized Phase 1.3 preparation/discussion on 2026-10-07. Its
[action/readiness draft](implementation/phase-1-3-action-readiness-draft.md) prepares service,
player, mechanism and readiness recommendations plus a discussion queue. User-selected directions
now include manual hand-item draw/stow and restoration, independent hatch operation, breathable
hangar, gravity after ignition and continued exploration after startup success. Seal/pressure status
affects represented departure readiness rather than ignition. Remaining art/metric details are deferred.
The user accepted the [Phase 1.3 closeout](implementation/phase-1-3-closeout-audit.md), its five
behavior choices and seven supporting defaults on 2026-10-08. Phase 1.3 planning is complete;
fit/runtime validation remains later work. Phase 1.4 was unstarted at that checkpoint; its planning
has since been authorized as recorded above. Implementation remains unstarted.

The [Phase 1.2 closeout package](implementation/phase-1-2-closeout-proposal.md) was accepted by
the user on 2026-10-07, including local canopy/platform/computer storage, planned MC demonstrations
and the bounded opening contract supplement. Phase 1.2 planning is complete; its actual geometry
tests remain unexecuted. Phase 1.3 has since completed its planning closeout; no implementation followed.

Graybox/Blender reconstruction and UE5 foundations can support the slice under a separately approved implementation scope. Exploration beyond required rooms, actual flight, sub-ether, expanded maintenance, faults/repairs, grapplers, detailed art and crew assistants remain later directions.

Preserve [external control and automation compatibility](architecture/external-control-automation.md) from the first approved simulation increment. In-world controls, future adapters and Gilliam share commands/state while locality remains meaningful. VoiceAttack, protocol selection, peripherals and natural-language orchestration require scoped approval; they are not dependencies of Slice 1.
