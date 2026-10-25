# Outlaw Star XGP Simulator

An evidence-driven reconstruction of the XGP-15AII and a planned interactive ship simulation in Unreal Engine 5. The ship is the main experience: enter it, explore physically located equipment, prepare its systems and eventually operate it through consistent shared state.

**The reference/research foundation is substantially complete for implementation purposes within the first slice.** This means enough evidence exists to define a constrained initial build; it does not mean every room, mechanism, translation or performance figure is settled. Unresolved research continues as an [ongoing parallel track](docs/reconstruction/open-questions.md).

Current status: **Phases 1 and 2 and subphase 3.1 complete**. The Blank C++ OutlawStarSim project has been generated at its accepted location; the neutral map is saved and selected for editor/game startup. The [2.2 closeout proposal](docs/implementation/phase-2-2-closeout.md) records the repository review, Android file-server configuration cleanup and scheduled recovery evidence. No modeled ship or playable slice exists. The [implementation plan](docs/implementation/vertical-slice-1-implementation-plan.md) links the accepted earlier contracts and the [Phase 1.4 architecture/asset/validation contract](docs/implementation/phase-1-4-architecture-asset-validation-draft.md). Following the accepted [Phase 1.5 review](docs/implementation/phase-1-5-gate-review.md), scoped owner-run VS installations were verified read-only. [Phase 2.1 closeout](docs/implementation/phase-2-1-closeout.md) was accepted on 2026-10-23, with explicit authorization for guided 2.2 setup. Subsequent explicit authorization covered 2.3 and the selected Unreal MCP pilot; the [2.3 closeout](docs/implementation/phase-2-3-closeout.md) records the results. The authorized [2.4 package and repeat-run proof](docs/implementation/phase-2-4-closeout.md) passed and its closeout is accepted; Phase 3.1 player/scale, Blender handoff and [published asset recovery](docs/implementation/validation/phase-3-1-recovery-results.md) passed; its [closeout](docs/implementation/phase-3-1-closeout.md) is accepted. Phase 3.2A remains unstarted.

## First experience — Awakening the Outlaw Star

The accepted [Phase 1.2 spatial package](docs/implementation/phase-1-2-closeout-proposal.md) owns
provisional layout and clearance reservations. The [Phase 1.3 behavior closeout](docs/implementation/phase-1-3-closeout-audit.md)
owns the current action/service/readiness contract. The accepted
[2026-10-25 route amendment](docs/implementation/phase-1-2-corridor-route-amendment.md) selects a
continuous cockpit-to-engineering corridor with a closed kitchen/dining side-hatch placeholder;
room placement, sizing and interior are deferred. These are planning decisions, not model or runtime validation.

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

The intended engine baseline is **UE 5.8**, with installed candidate **5.8.4**. Intended Windows C++ tooling is **Visual Studio Community 2026 + MSVC 14.50 + Windows SDK 10.0.26100.0**. The [2026-10-23 post-installation check](docs/implementation/phase-2-1-closeout.md) records VS **18.11.1**, installed .NET Desktop/MAUI and matching 14.50 ATL, with the preferred compiler and intended SDK retained. The [earlier preflight](docs/implementation/validation/phase-2-1-tooling-preflight-2026-10-23.md) records Git LFS 3.7.1 and reported Blender 5.2.3 (file metadata confirms the 5.2 family), plus the stale launcher record despite installed 5.8.4. The three identified setup gaps are resolved. [Phase 2.2 repository preparation](docs/development/unreal-project-setup.md) has added scoped LFS rules/local setup; publication and fresh-clone file recovery are verified for `49511af`; recovered-map opening, ordinary compile/repeat editor proof and the selected Unreal MCP pilot passed in 2.3. The neutral Development package and repeated standalone input/exit checks also passed in 2.4; Blender handoff and published recovery passed in 3.1; full-slice/performance validation remains pending.

[Unreal strategy](docs/architecture/unreal-strategy.md) owns the choice/compatibility limits; the preflight and [Phase 1.1 readiness record](docs/implementation/phase-1-1-host-tooling-readiness.md) distinguish current tooling evidence from earlier host observations. Core state/gameplay foundations are planned in C++, with Blueprints for configuration/content/presentation and Blender for reconstruction. Primary proof target is the laptop, Win64, keyboard/mouse, native 1440p/60 FPS required with 120 FPS as a stretch goal, pending measured proof; no initial desktop validation required. Phase 1.4 revises the earlier 120 FPS target and selects Lumen as the preferred lighting candidate for evaluation.

Python/Pillow, FFmpeg/FFprobe and optional ImageMagick have supported the reference workflow. [Tool documentation](tools/reference-extraction/README.md) explains reproducible inventories, metadata checks, targeted frame extraction and subtitle screening. Phase 1.4 selects [local MCP pilots](docs/architecture/editor-automation.md#current-local-pilot-contract--accepted-2026-10-11) for Unreal and Blender; Sandbox/VM work is deferred. The Unreal pilot has passed, including project-user loopback auto-start. The [3.1 Blender pilot](docs/implementation/validation/phase-3-1-blender-mcp-pilot.md) has passed connectivity, reversible edits, save/reopen and stop/reconnect checks; approved interactive auto-start is verified on loopback. Blender-to-Unreal handoff/reimport, owner-run player-fit checks and [published asset recovery](docs/implementation/validation/phase-3-1-recovery-results.md) passed. The [initial rendering direction](docs/implementation/phase-1-4-architecture-asset-validation-draft.md#initial-rendering-and-anti-aliasing-direction--accepted-2026-10-11) is DirectX 12/deferred, Lumen with hardware tracing as the first candidate, Virtual Shadow Maps and native-resolution TSR; Vulkan and other shadow/AA methods are learning comparisons. The [selected Games Blank C++ template](docs/implementation/phase-1-4-architecture-asset-validation-draft.md#starting-template--blank-c-accepted-2026-10-11) has generated the initial skeleton; [setup observations](docs/development/unreal-project-setup.md) distinguish template defaults and incidental creation activity from the subsequent recorded 2.3 neutral build/editor proof. Character templates remain references for later player work. Gameplay external transport and broad gameplay framework remain unselected.

## Evidence and source handling

The [canon policy](docs/canon-policy.md) separates anime observations (A), authenticated production evidence (B), official supplements (C), strong inference (D), reconstruction extrapolation (E) and gameplay adaptation (F). Our scanned production collection remains B candidate pending provenance. **D/E/F are never canon.** Original Japanese, translation confidence and contradictions stay explicit.

`_source_settei/` and `_source_episodes/` are immutable local references. Generated frames, contact sheets, cached HTML and full subtitle copies remain ignored/local-only. Authored Markdown, CSV, JSON provenance and helper scripts are trackable. Individual supplied images may be published when explicitly authorized; that does not authorize source-media publication. Phase 1.4 accepts Git LFS for project-owned Blender files, Unreal assets/maps and designated handoff exports; scoped tracking and local setup are configured. Fresh-clone file recovery and opening the retrieved neutral map passed during Phase 2. Published Blender, FBX and Unreal fixture recovery also passed during [3.1](docs/implementation/validation/phase-3-1-recovery-results.md).

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

The [phased implementation plan](docs/implementation/vertical-slice-1-implementation-plan.md) owns execution sequence, prerequisites, validation, recovery and exit reviews. Phase 1 planning and Phase 2.1–2.2 are complete; the 2.2 closeout is accepted. Explicitly authorized 2.3 build/editor and Unreal MCP work has passed; closeout is accepted. Phase 2.4 closeout is accepted; the [Phase 2 exit gate](docs/implementation/phase-2-exit-review.md) is accepted. Phase 3.1 player/scale work, Blender MCP/handoff and published recovery are complete; its [closeout](docs/implementation/phase-3-1-closeout.md) is accepted. Phase 3.2A and later execution remain unauthorized. Spatial choices remain provisional pending fit proof; behavior contracts require runtime validation.

## Start here

- [Game development glossary](docs/development/game-development-glossary.md) — plain-language graphics, Blender/Unreal, performance, input and tooling terms; expanded as we learn.
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
