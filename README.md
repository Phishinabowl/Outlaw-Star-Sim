# Outlaw Star XGP Simulator

An evidence-driven reconstruction of the XGP-15AII and a planned interactive ship simulation in Unreal Engine 5. The ship is the main experience: enter it, explore physically located equipment, prepare its systems and eventually operate it through consistent shared state.

**The reference/research foundation is substantially complete for implementation purposes within the first slice.** This means enough evidence exists to define a constrained initial build; it does not mean every room, mechanism, translation or performance figure is settled. Unresolved research continues as an [ongoing parallel track](docs/reconstruction/open-questions.md).

Current status: **Phases 1.1–1.3 planning complete; Phase 1.4 unstarted; implementation not started**. No Unreal project, modeled ship or playable build exists yet. The accepted [implementation plan](docs/implementation/vertical-slice-1-implementation-plan.md) links the [Phase 1.1 readiness record](docs/implementation/phase-1-1-host-tooling-readiness.md), [Phase 1.2 packet](docs/implementation/phase-1-2-spatial-motion-decision-packet.md) and [accepted Phase 1.3 closeout](docs/implementation/phase-1-3-closeout-audit.md). Later subphases, Unreal creation, gameplay implementation, modeling and further installations still require their own approved scope.

## First experience — Awakening the Outlaw Star

The accepted [Phase 1.2 spatial package](docs/implementation/phase-1-2-closeout-proposal.md) owns
provisional layout and clearance reservations. The [Phase 1.3 behavior closeout](docs/implementation/phase-1-3-closeout-audit.md)
owns the current action/service/readiness contract. Neither is a model or runtime validation.

The [Vertical Slice 1 contract](docs/reconstruction/baseline-v1/vertical-slice-1.md) defines a supported ship inside an asteroid hangar:

`Hangar reveal → loaded boarding → case revival / laptop bootstrap → Gilliam registration → Melfina link → engineering → key ignition / seat lift → startup milestone → continued exploration`

The ship remains supported inside the hangar. SHIP READY is a startup milestone, not the end of play: leave the seat and continue exploring, including hatch exit/re-entry between active ship gravity and hangar low gravity. Hatch seal/pressure checks affect the represented departure status rather than blocking ignition. Scope includes the required traversal route, physical controls, a placeholder occupant for Melfina's apparatus, four prepared engineering-cylinder endpoints, moving bridge seating and consistent readiness feedback. It excludes free flight, sub-ether travel, combat, damage simulation, full crew AI, Gilliam LLM, every interior room and detailed art.

Accepted demo behavior includes:

- Play as Gene, with manually toggled magnetic boots, a back-carried trunk and a hand-slot laptop with on-demand draw/stow.
- Read Hilda's digital note and unlock the case through the connected laptop. Begin resuscitation explicitly; the 600 s timer has a local shortcut. Melfina waits for your acknowledgement before apparatus entry.
- Bootstrap the ship through the anime-inspired laptop override/countdown/HOLD screens. Gilliam's cockpit pod lights/animates, with text choices, a recovery branch and resumable registration.
- Use local click/grip/turn/pull engineering controls on four units. Early preparation is allowed after registration; Melfina's report reflects actual units. After completed OFF, push in/relock and redeploy without replacement ribbons; restart rechecks current preparation.
- Insert/remove the ignition key separately from OFF/ON. Ignition triggers occupied seat lift and main services/gravity; graceful narrated OFF lowers the seat then returns to limited services. Melfina stays deployed with reduced-power presentation. Startup success persists separately from live operational/departure status.
- Keep simulation running behind the menu unless explicitly paused by button/hotkey. Focus-loss auto-pause defaults ON and resumes only a focus-caused pause. Optionally carry the empty trunk back to a hangar staging spot.

Baseline v1 preserves evidence and assumptions separately:

| Document | Purpose |
|---|---|
| [Spatial constraint map](docs/reconstruction/baseline-v1/spatial-constraint-map.md) | Hull constraints, local room relationships, hatch identities and unknown connections; not a final deck plan. |
| [Motion/clearance envelopes](docs/reconstruction/baseline-v1/motion-clearance-envelopes.md) | Reserve space for machinery motion, operators and future assemblies before placing walls. |
| [Operational states](docs/reconstruction/baseline-v1/operational-state-baseline.md) | Separate commissioning, standby departure, sub-ether and emergency-recovery vocabulary. |
| [Slice scope and acceptance](docs/reconstruction/baseline-v1/vertical-slice-1.md) | Concrete endpoint, exclusions, observable completion criteria and unresolved decisions. |

## What the repository contains

- All **221 settei scans screened**, with **66 XGP/support records** identified. The original focused-pass coverage checkpoint records 44 reviewed and 22 without those structured passes; later targeted spatial/machinery checks are linked in the reference index. Full transcription and production provenance remain open.
- Timestamp metadata cached for **all 26 episodes**, with **9,204 gallery locators**. Web-to-local alignment is still unverified.
- Focused local evidence for Episodes **1, 2, 4, 7, 8, 11 and 26**, covering case revival, commissioning, standby launch, reactor terminology, sub-ether disruption/recovery and Melfina's descent. User-supplied laptop/power-state images and verified English-dub lines retain their separate provenance.
- An [all-episode subtitle audit](reference/indexes/performance-subtitle-audit.md) and [47-record performance register](reference/indexes/performance-metrics.csv), with source/track/hash provenance. English translations, inferred calculations, other ships and special operating conditions are distinguished.
- Future architecture requirements for physical interaction, one physical player with separate camera/control modes, authoritative ship state and reusable commands for consoles, Gilliam and later external clients.

The accepted overall exterior envelope is **72 × 21 × 16 m**, supported by the official profile recorded in the [reference index](docs/reconstruction/xgp-reference-index.md). It does not define usable interior volume, deck count or deployed appendage limits.

## Technology direction and current tooling

The intended engine baseline is **UE 5.8**, with installed candidate **5.8.3**. Intended Windows C++ tooling is **Visual Studio Community 2026 + MSVC 14.50 + Windows SDK 10.0.26100.0**. The dated Phase 1.1 inventory verified MSVC 14.50 installed alongside 14.51, plus Blender 5.2 and Git LFS 3.7.1. No project build/editor/export/MCP proof or LFS asset-policy setup has been performed. Remaining vendor-guidance setup gaps require a later authorized installation scope.

[Unreal strategy](docs/architecture/unreal-strategy.md) owns the choice/compatibility limits; the [Phase 1.1 readiness record](docs/implementation/phase-1-1-host-tooling-readiness.md) owns dated host observations. Core state/gameplay foundations are planned in C++, with Blueprints for configuration/content/presentation and Blender for reconstruction. Primary proof target is the laptop, Win64, keyboard/mouse, 1440p/120 FPS pending measured proof; no initial desktop validation required.

Python/Pillow, FFmpeg/FFprobe and optional ImageMagick have supported the reference workflow. [Tool documentation](tools/reference-extraction/README.md) explains reproducible inventories, metadata checks, targeted frame extraction and subtitle screening. No renderer, project template, external transport or broad gameplay framework has been selected by this update.

## Evidence and source handling

The [canon policy](docs/canon-policy.md) separates anime observations (A), authenticated production evidence (B), official supplements (C), strong inference (D), reconstruction extrapolation (E) and gameplay adaptation (F). Our scanned production collection remains B candidate pending provenance. **D/E/F are never canon.** Original Japanese, translation confidence and contradictions stay explicit.

`_source_settei/` and `_source_episodes/` are immutable local references. Generated frames, contact sheets, cached HTML and full subtitle copies remain ignored/local-only. Authored Markdown, CSV, JSON provenance and helper scripts are trackable. Individual supplied images may be published when explicitly authorized; that does not authorize source-media publication. Git LFS for future project-owned binary assets remains undecided.

## Repository guide

| Location | Contents |
|---|---|
| `docs/` | Vision, policy, roadmap, architecture requirements and reconstruction baseline. |
| `reference/indexes/` | Authored evidence reviews, source/episode manifests, screening data, timestamp indexes and performance records. |
| `tools/reference-extraction/` | Small deterministic reference helpers; no game implementation. |
| `reference/working/`, `reference/extracted-frames/`, `reference/cache/`, `reference/contact-sheets/` | Ignored generated media and working data. |
| `.local/` | Ignored machine-specific notes; not shared project requirements. |

## Research alongside future implementation

Keep hatch/room correspondence, apparatus clearances, remaining mechanical families, Japanese wording, power topology and performance interpretation in [open questions](docs/reconstruction/open-questions.md). Research should be targeted when it could invalidate a chosen slice connection, motion or interaction; broader full-ship archaeology need not hold the entire project indefinitely. Any provisional solution remains explicitly E/F and reviewable.

The [phased implementation plan](docs/implementation/vertical-slice-1-implementation-plan.md) owns execution sequence, prerequisites, validation, recovery and exit reviews. Phase 1 is the formal decision/planning gate; it resolves the existing [slice decisions](docs/reconstruction/baseline-v1/vertical-slice-1.md#decisions-before-the-next-phase) before project creation. Phases 1.1–1.3 planning are complete. Spatial choices remain provisional pending fit proof, and accepted behavior contracts require later runtime validation. Phase 1.4 onward is not authorized.

## Start here

- [Vision](docs/vision.md) and [design pillars](docs/design-pillars.md)
- [Canon policy](docs/canon-policy.md)
- [Todo Tree and working annotation standards](docs/development/work-annotation-standards.md)
- [Roadmap](docs/roadmap.md)
- [Vertical Slice 1 implementation plan](docs/implementation/vertical-slice-1-implementation-plan.md)
- [Accepted Phase 1.3 behavior contract](docs/implementation/phase-1-3-closeout-audit.md)
- [External control and automation requirements](docs/architecture/external-control-automation.md)
- [Reference index](docs/reconstruction/xgp-reference-index.md)
- [Reconstruction / Implementation Baseline v1](docs/reconstruction/baseline-v1/spatial-constraint-map.md) and [Awakening the Outlaw Star slice](docs/reconstruction/baseline-v1/vertical-slice-1.md)
- [Open questions](docs/reconstruction/open-questions.md)
- [Reference workflow](reference/README.md)

See [reference progress](docs/reconstruction/reference-phase-progress.md) for historical increments and the [roadmap](docs/roadmap.md) for current approval boundaries.
