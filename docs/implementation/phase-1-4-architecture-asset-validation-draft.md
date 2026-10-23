# Phase 1.4 — Architecture, Assets And Validation Discussion Draft

Status: planning/discussion in progress, updated 2026-10-23. This documentation increment is confirmed
for publication. Accepted identity, ownership, communication, asset/handoff, proxy, performance and learning
contracts are distinguished below from remaining technical decisions; Phase 1.4 is not complete.
No project, folders/assets, code, installation, plugin enablement or Git/LFS configuration is created
by this document. Phase 1.5 and implementation remain unstarted.

Inputs: accepted [Phase 1.2 spatial package](phase-1-2-closeout-proposal.md),
[Phase 1.3 behavior contract](phase-1-3-closeout-audit.md),
[dated host inventory](phase-1-1-host-tooling-readiness.md),
[shared command requirements](../architecture/external-control-automation.md),
[Unreal strategy](../architecture/unreal-strategy.md) and
[editor-automation contract](../architecture/editor-automation.md).
Tool observations are dated; no fresh compatibility/build proof is claimed in this opening pass.
Use the [game development glossary](../development/game-development-glossary.md) for grouped,
plain-language definitions; this plan remains authoritative for choices and experiment scope.

## Scope And Discussion Order

| Requirement | Decision work | Planned discussion order |
| --- | --- | --- |
| Project/layout, C++/Blueprint, map/input/camera | Concrete identity/path and bounded ownership | First |
| Command/query/result lifecycle and reset | Implement accepted local/state/pause rules without competing writers | With ownership |
| Owned/generated/source publication and binary policy | Git versus LFS, editable sources/exports, authoring records | Before first binary commit |
| Proxy/render/performance contract | Source-shaped placeholders, initial settings and native 1440p/60 required, 120 stretch measurement protocol | After project/asset boundaries |
| MCP selection or deferral | Recheck candidates and choose bounded pilots/fallbacks under existing automation contract | Before adoption, no installation now |
| Blender-to-Unreal handoff | Units/orientation/pivots/collision, export recipe and known-size fixture | Before repeated geometry production |
| Validation procedures | Named performer, expected outcomes, evidence and standalone proof for existing VS1 IDs | Before Phase 1.5 gate review |

This draft is not a completed technical plan. The seven implementation-plan checkboxes remain open.
Exact startup behavior stays with 1.3; technology decisions cannot silently remove required dialogue,
machinery, pause, reversible operation or continued exploration merely to simplify the build.

## Initial Project Identity And Folder Layout — Accepted

The accepted internal project/module name is **OutlawStarSim**, with project file planned at
`Unreal/OutlawStarSim/OutlawStarSim.uproject`. This follows the repository's existing Unreal ignore
boundary and avoids mixing engine outputs with documentation/source references. The game's display
title may remain “Outlaw Star XGP Simulator”; internal identifier does not decide branding.
The one-module C++ authority/Blueprint presentation direction is agreed in principle; detailed
ownership/lifecycle/map/asset contracts still need review. No project/folder creation is authorized.

| Accepted planned location | Ownership / role |
| --- | --- |
| `Unreal/OutlawStarSim/Source/OutlawStarSim/` | One initial runtime C++ module; add modules/plugins only for an actual separation need |
| `Unreal/OutlawStarSim/Config/` | Reviewed project configuration; no host credentials/client configuration |
| `Unreal/OutlawStarSim/Content/XGP/` | Owned maps, Blueprints, UI/proxy materials and imported assets; subdivisions and initial prefixes accepted below |
| `assets/` | Project-owned Blender sources, export recipes/manifests and designated handoff assets, separated below |
| `docs/implementation/` | Accepted contracts, validation procedures/results and later handoff records |
| Existing `_source_*` and ignored reference media | Immutable/local-only evidence; not game assets or packaging dependencies |

Plan one opening map containing the hangar and required route, plus small separate validation maps
only where isolation materially helps reproduce a failure. No world streaming/open-world infrastructure
required for this slice. A neutral build fixture still precedes the playable map under Phase 2.
The map organization, folder layout and Blank C++ template are accepted below; exact map names remain to select. No
project initialization is authorized by these planning choices.

### Starting Template — Blank C++ Accepted 2026-10-11

Select the Games **Blank** template with **C++** for the main OutlawStarSim project. Template choice
sets the initial content/behavior; C++ versus Blueprint is a separate starting-code choice. C++ does
not exclude Blueprints, and Blank does not require replacing Unreal's built-in character, movement,
collision or input systems.

Phase 2 creates only the minimal agreed skeleton and neutral fixture, then proves build, editor
startup and standalone packaging. Phase 3.1 adds the shared physical player and both views using
appropriate engine components and reviewed template examples. Low gravity/boots, handholds, ladders,
equipment and seated interactions remain at their planned checkpoints; template selection does not
claim those behaviors are already supplied or tested.

Use Epic's character templates as references rather than adopting their complete starting content
and camera/movement assumptions. Selective mannequin/animation use may be reviewed later with its
dependencies, ownership and fit; it is not mandated by this selection. No separate sample project,
template asset import or Unreal initialization is authorized by recording this decision.
Reference: [Epic template overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-templates-reference).

### Folder Subdivisions And Initial Naming — Accepted 2026-10-11

| Planned path | Contents |
| --- | --- |
| `assets/blender/` | Editable project-owned Blender originals. |
| `assets/exports/` | Designated handoff files imported into Unreal; retain the accepted source/export relationship. |
| `assets/recipes/` | Authored export settings, scripts/recipes and manifests for reproducible handoff. |
| `Unreal/OutlawStarSim/Content/XGP/Maps/` | Playable maps. |
| `Unreal/OutlawStarSim/Content/XGP/Ship/`, `Characters/`, `Props/`, `Materials/`, `UI/`, `Input/` | Content grouped by role; the shortened paths in this row are all under `Content/XGP/`. |
| `Unreal/OutlawStarSim/Content/XGP/Development/` | Test Lab and development-only fixtures; intended to be excluded from the playable distribution. |
| `docs/implementation/validation/` | Authored procedures/results tied to existing VS1 IDs; raw captures/logs remain local working data. |

Development folder placement alone does not enforce package exclusion. Specify the playable map
allowlist/exclusion configuration during authorized package work and verify that runtime references
do not pull test-only assets into the distribution. Reusable content needed by Awakening belongs
outside the development-only folder. The early neutral proof package is intentionally a separate
development artifact, not the final playable distribution.

Use type prefixes and readable names to distinguish cooperating assets:

| Prefix | Type | Illustrative name |
| --- | --- | --- |
| `SM_` | Static mesh | `SM_EngineeringCylinder` |
| `BP_` | Blueprint | `BP_EngineeringCylinder` |
| `M_` | Material | `M_PaintedMetal` |
| `MI_` | Material instance | `MI_PaintedMetal_Red` |
| `IA_` | Input action | `IA_Interact` |

These names illustrate the accepted convention; they do not mandate a particular class or asset
inventory. A Blueprint may reference a mesh and material rather than duplicate them. Extend prefixes
when needed instead of inventing a full asset taxonomy before content exists. General reference:
[Epic asset naming guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects).
No directories, Unreal assets, export files, packaging rules or Git/LFS configuration are created here.

## Accepted Map And Input Organization — Detailed Bindings Pending

Accepted in discussion, 2026-10-10. Start with one Test Lab map for scale, materials/lighting,
mechanisms and player-clearance fixtures, and one continuous Awakening map for the playable hangar
and required ship interiors. Create extra isolated maps only for a reproducibility need. The minimal
Phase 2 engine/build/package fixture still comes first; test-map existence is not validation evidence.
Folder roles are accepted above; exact map names and shipping/package allowlists remain to specify.

Use Unreal Enhanced Input to separate logical actions from physical keys/buttons and organize bindings
by situation. Exploration, grip, ladder, seated interaction, focused laptop/dialogue/menu UI and code
text-entry are logical situations, not a requirement for six mapping assets. Configure mappings and
route requests through accepted authority; contexts do not replace command permission/locality checks.
UI/text focus must explicitly suppress conflicting gameplay actions, release grips/movement on the
accepted menu/focus transitions and require fresh input afterward. Test actual routing rather than
assuming mapping priority alone handles text focus and widgets.

First/third person share the same physical Gene, reach, equipment and permissions. Exact keys/buttons,
camera offsets and transitions remain for discussion/fit proof. Initial required validation remains
keyboard/mouse; Enhanced Input capability is not an expansion to required controller/HOTAS support.

Reference: [Epic Enhanced Input documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine).
No project, mapping asset or input code is created by this accepted planning choice.

### Optional Controller Learning Trial — Accepted Direction

Keyboard/mouse remains the required first proof; preserve device-independent actions and multiple
bindings for later input expansion. An optional controller learning trial is accepted for later authorized work, with
Xbox, DualShock 4/PS4 and Switch Pro as longer-term devices of interest. This is not a promise of
complete support for all devices or console-platform builds in the first slice.

After basic movement/local interaction and focused UI work, trial one available supported controller,
preferably Xbox/XInput on Windows, before widening to other device paths. Record model, wired/Bluetooth
connection, driver/input backend and any translation layer. Enhanced Input handles action mapping;
device recognition/protocol support is a separate compatibility concern. Evaluate native support or
an explicitly selected adapter for other devices; do not assume every controller is plug-and-play.
No input plugin, translation utility or Steam integration is installed/enabled by this decision.

Trial movement/look and stick dead zones, interact/draw/stow/boots, grip plus directional cylinder
movement, ladder/seat/key actions, laptop pointer or focus navigation, the on-screen code keyboard,
dialogue/menu/manual pause and return to keyboard/mouse. Test disconnect/reconnect while gripping or
in UI, clearing held input without changing mechanism progress or creating duplicate actions. Device
prompts must reflect the actual mapping; correct native glyphs are a later presentation decision,
especially when a translation layer reports a different device. Save/report limitations and defer
the pilot if it would block keyboard/mouse slice proof; no controller-only behavior or readiness writer.

Sources checked 2026-10-10: [Steam Input device support](https://partner.steamgames.com/doc/features/steam_controller/device)
lists Xbox, PS4 and Switch Pro families; [Epic RawInput guidance](https://dev.epicgames.com/documentation/unreal-engine/rawinput-plugin-in-unreal-engine)
describes a configurable route for devices not handled by XInput. Neither is selected or verified on
this host. Exact controller bindings, backend and optional execution scope remain to agree later.

Include a controller-routing lesson: physical USB/Bluetooth device, Windows driver/API, optional
translation/virtual controller, Unreal input backend, Enhanced Input mappings and authoritative action.
Compare native and translated routes where available; inspect identity, duplicate input, button-label
differences, dead zones and reconnection behavior. Virtual Xbox-compatible output does not prove that
the physical controller's driver was replaced. Record only inspected host configuration as verified.
The user reports an existing DS4Windows installation and familiarity with Steam Input and custom
adapter setups; versions/driver/routing on this host remain uninspected. GameCube-adapter examples may
help explain the layers, but do not add another required device or authorize driver changes.

Use upstream references for explanations, including [ViGEm's virtual-device model](https://github.com/nefarius/ViGEmBus).
That project is retired; this historical architectural reference is not a recommendation to install
it or evidence that this host uses it. Review the actual installed utility/backend before any trial.

For the adapter lesson, distinguish [Zadig's USB driver assignment](https://zadig.akeo.ie/) from
[vJoy's virtual joystick](https://github.com/shauleiz/vJoy). Either layer may affect the input route;
do not diagnose past conflicts or current installed drivers without inspection. Input/controller
planning additions are confirmed for publication on 2026-10-10; device trials remain unexecuted.

## Accepted Ownership Boundaries — Same Behavior, Clear Responsibilities

Accepted in discussion, 2026-10-10. These are logical responsibilities, not a requirement to create
six large systems or six particular Unreal classes. C++ owns authoritative rules/state; presentation
reads those records and reports real mechanism progress rather than creating independent success.

| Logical owner | Record / responsibility |
| --- | --- |
| Player and equipment | Physical context, assigned/drawn/stowed equipment and current interaction |
| Individual mechanisms | Physical condition and actual motion progress: seals, handle angles, extension, hatch closure and seat endpoints |
| Ship coordinator | Shared services, startup/shutdown sequencing and current prerequisite/readiness checks |
| Narrative progression | Revival, registration and dialogue checkpoints; completed registration does not repeat on ordinary OFF/ON cycles |
| Session control | Simulation time/pause reasons, fresh-run reset and historical startup success distinct from live readiness |
| Presentation | Models, animation, lights, text, sounds and UI reflect authoritative results; Gilliam explains rather than independently decides readiness |

For ignition, the local interaction submits a request. The ship checks current prerequisites including
all four actual cylinder conditions; rejection supplies the same reason to Gilliam and displays.
An accepted request begins the agreed ignition sequence, and moving mechanisms report actual progress
and completion. Historical startup success is recorded only after the required startup conditions
complete; subsequent shutdown changes live readiness without clearing that milestone. The detailed
ordering remains governed by Phase 1.3, not by this illustrative ownership example.

The following implementation boundaries support that accepted division; exact Unreal types and
request/lifecycle mechanics remain for discussion.

| Responsibility | Proposed authority | Presentation/configuration boundary |
| --- | --- | --- |
| Player context/equipment, locality and permitted actions | C++ | One physical body; camera perspective and UI do not grant alternate permissions |
| Ship units/services, navigation, key/seat transitions | C++ | Blueprint assets supply positions, motion paths, durations and visuals; configured motion reports actual progress/endpoints |
| Command validation/results and duplicate/conflict handling | Shared C++ request path | Panels, laptop, dialogue and future adapters submit requests; no direct widget-owned success flags |
| Revival/dialogue step, per-run success and live/departure status | Authoritative C++ state/lifecycle | Data/Blueprint presentation selects authored text/images and reads current state; no LLM required |
| Simulation pause, focus pause and fresh-run/reset | One coordinated C++ lifecycle | Menu button/hotkey share the manual action; local laptop HOLD remains distinct |
| Models, lights, materials, Gilliam face, sounds and UI layout | Blueprint/editor-authored content | Respond to state and configure presentation; cannot independently complete readiness |

No final classes, subsystems, APIs, plugin framework or external schemas are selected here. Keep
pure validation separable from visual mechanisms so appropriate tests can run without pretending
that a pure-state test proves body/occupant clearance. Reset must invalidate old operation callbacks
and restore both authority and presentation under the accepted contract.

## Accepted Communication And Lifecycle Rules

Accepted in discussion, 2026-10-10. Commands request actions, queries read authoritative current
state and events report actual changes/completion. Commands distinguish rejection, accepted/in-progress,
completion and failure after starting. Acceptance alone cannot set readiness or announce success.

- Repeated input cannot start duplicate operations. Repeated ignition input during an active startup
  does not create additional startup sequences; the session/operation identity rules below define
  the agreed tracking boundary without selecting concrete identifier types or APIs.
- Conflicting requests receive clear reasons rather than silently competing for a mechanism. Cylinder
  restow while ON remains disallowed under the accepted Phase 1.3 contract.
- Interruption follows each action's existing contract: released grip preserves partial engineering
  movement, while disconnect cancels an unfinished laptop authentication/override/bootstrap attempt.
  Completed effects and independent revival progression remain governed by Phase 1.3.
- Fresh-run reset invalidates unfinished work and old callbacks. A previous run's timer or animation
  completion cannot mutate the new run; authority and presentation are restored together.
- Reopened controls read current state/checkpoints, including changes while the player was away.
  Events may notify presentation, but missed events cannot leave a reopened panel with stale state.

All callers use the same validation/results path without bypassing physical locality or control-context
requirements. No external transport, network service or voice integration is selected or implemented.
Exact Unreal types, schemas and executable validation procedures remain pending; accepting
these rules does not complete the seven Phase 1.4 checklist items.

### Session And Operation Identity — Accepted 2026-10-11

Use a session identifier for the current fresh run and an operation identifier for each particular
tracked action. Pair the two when attributing asynchronous work/results. Session control owns fresh-run
identity; the authoritative action owner tracks operation state through the shared request/result path.
Concrete identifier formats, C++ types and storage details remain implementation choices.

| Situation | Required outcome |
| --- | --- |
| Repeated ignition input while startup is active | Reference the existing operation/current result or return a clear in-progress reason; do not start a duplicate sequence. |
| Conflicting action on a busy mechanism | Validate through the shared path and report the reason; unrelated allowed operations need not be globally serialized. |
| Reset during seat motion, bootstrap or a timer | Invalidate the old session/work, stop outstanding motion/timers as appropriate and restore starting authority/presentation before accepting new actions. |
| Late callback after reset | Ignore the previous session's callback; it cannot set readiness or change the new run's presentation. |
| Late callback after same-session cancellation/replacement | Check that its operation is still current and permitted to complete; matching the session alone is insufficient. |
| Reopened laptop or dialogue UI | Query current state/checkpoints; missed events cannot leave stale UI. |

Results distinguish rejected, accepted/in-progress, completed and failed, with operation identity and
a reason where appropriate. Accepted is not completed. Interruption retains the Phase 1.3 action
contract: handle release preserves partial extension; disconnect cancels unfinished laptop work;
independent revival and completed effects persist where already agreed. IDs do not turn all releases
into resets or create permission to bypass physical locality.

Use existing VS1-S02 for duplicate/conflict results and VS1-S03/VS1-R03 for reset, interrupted work
and stale-callback/repeated-session proof. These identifiers are internal lifecycle tracking, not
player/account identity, save-game support or a multiplayer/network service. No implementation occurs
in this planning increment.

## Accepted Asset Versioning Policy

Accepted in discussion, 2026-10-10. Ordinary Git tracks authored text: project/source/configuration,
documentation and export recipes/manifests. Git LFS will track project-owned Blender files, Unreal
assets/maps and designated model handoff exports required to reproduce imports. Preserve editable
authoring sources and the actual imported game assets together with their handoff records.

Temporary exports, Blender backups, engine caches and build outputs remain ignored. Existing
immutable sources and generated reference media remain local-only under the current publication
policy. LFS is not an exception to that policy. Source/export folders are accepted in the layout
contract above. The storage/recovery contract below specifies their planned handling; executable
tracking configuration and fresh-checkout/import proof remain unperformed.

Modest paid LFS usage is acceptable in principle; no numeric spending limit has been selected.
Before paid usage, check the repository owner's current allowance/usage, estimate storage including
retained revisions and download bandwidth, and agree a spending cap. Do not enable uncapped billing
or purchase/change account billing on the strength of this planning acceptance. No LFS configuration
or asset upload has occurred.

GitHub's [billing documentation](https://docs.github.com/en/billing/concepts/product-billing/git-lfs),
checked 2026-10-10, lists 10 GiB storage and 10 GiB download bandwidth per billing cycle for Free/Pro
accounts. These are account allowances, not a verified remaining allowance for this repository.
Each changed binary revision stores the whole file again; uploads do not consume download bandwidth.
Recheck pricing/usage before paid adoption rather than treating this dated record as a cost promise.

### Asset Storage And Recovery Contract — Accepted 2026-10-23

| File scope | Planned storage |
| --- | --- |
| Editable project-owned `.blend` files under `assets/blender/` | Git LFS. |
| Designated `.fbx` handoff files under `assets/exports/` | Git LFS; temporary export attempts remain local working data. |
| Owned Unreal `.uasset` and `.umap` files under `Unreal/OutlawStarSim/Content/` | Git LFS, including versioned development fixtures. Development-only packaging exclusion remains a separate concern. |
| C++ source, project descriptors, configuration, recipes, manifests and documentation | Ordinary Git. |
| Temporary exports, Blender backups, engine caches and packaged builds | Ignored/generated working data. |
| Source episodes/settei and generated reference media | Existing immutable-source/local-only exclusions; no publication through LFS. |

Apply repository-local tracking rules before the first authorized binary publication. Review the
eventual `.gitattributes` patterns against these scopes and retain generated-output exclusions;
configuration is Phase 2.2 work, not an action performed by this planning acceptance. Other binary
formats require a scoped policy decision when introduced rather than an unrestricted all-binary rule.

Preserve each asset's editable source, designated export, import recipe/manifest and imported Unreal
asset as one traceable revision set. The handoff record links their paths/revisions and the existing
dimension, orientation, pivot, assembly-offset and collision expectations. An export or cooked asset
does not replace its editable source.

Before a reimport, retain a recoverable known-good revision or local checkpoint of the affected
asset set and recipe. Publication of checkpoints still follows explicit Git confirmation. If a
reimport breaks scale, hinges, references, materials or collision, preserve the failed result/logs
locally and restore only the affected known-good asset set. Preserve unrelated edits. Reproduce and
correct the problem in the small handoff fixture before repeating the recipe across ship assets.
Do not hide conversion errors with arbitrary per-instance scale or pivot adjustments.

Validate retrieval after the first authorized binary publication, before relying on the workflow
for repeated production: a fresh checkout must retrieve the actual LFS payloads rather than unresolved
pointer files; the designated Blender/Unreal test assets must open, and the recorded handoff must
retain expected scale, orientation, pivots and collision. Record the revision, tool/recipe versions,
observed results and remaining untested checks. VS1-T02 owns the repository/storage boundary proof;
the existing handoff fixture owns import/reimport behavior. No fresh checkout or editor test has run.

References: [GitHub LFS overview](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)
and [repository tracking configuration](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage).
This increment changes documentation only. It creates no `.gitattributes`, tracking rules, assets,
exports, backups or clones, and performs no LFS setup, upload, restoration or history migration.

## Accepted Blender To Unreal Handoff Conventions — Fixture Proof Pending

Accepted in discussion, 2026-10-10; not yet tested. Start with rigid machinery/static-mesh handoff;
character skeletons, skinning and detailed animation export remain a later production contract.

- Author real dimensions using metric display in Blender, initially unit scale 1 (one scene unit per
  metre). Unreal dimensions use centimetres: a 1 m fixture must import as 100 cm at unit placement
  scale. Convert in the recorded export/import recipe; do not repair an incorrect handoff by arbitrary
  per-instance rescaling. Blender unit/axis export settings still need installed-version proof.
- Target Unreal local +X forward, +Y right, +Z up. Record source orientation and conversion, and use
  asymmetric front/right/top markers to catch mirrored or rotated output. This asset-local convention
  does not redefine the Phase 1.2 nose-to-aft longitudinal measurement coordinate.
- Export independently moving rigid parts separately, assembled through recorded local offsets.
  Put handle/door pivots on their rotation axes and define cylinder slide axes and assembly anchors.
  Normalize export transforms without destroying the editable source. Preserve a full source assembly
  for fit review, with per-part export origins/pivot behavior proven in the selected importer.
- Use FBX as the initial candidate rigid-mesh interchange format. Prefer one render part plus its
  collision per export, avoiding multi-part collision ambiguity. Pin the actual exporter/importer
  path and settings after the fixture, not from a generic online preset. Materials remain simple
  Unreal-authored proxies initially; Blender shader appearance is not an import acceptance criterion.
- Use explicit simple collision appropriate to the shape, including separate pieces around openings
  so doorway/hatch clearance stays open. Moving-part collision follows the actual moving part.
  Cosmetic detail does not require equally detailed collision. Preserve the accepted demo trunk's
  nonblocking player-collision exception; do not generalize it to hull or machinery.
- Keep a reviewable handoff manifest: owned source/export/imported asset identities and revisions,
  tool versions/settings, expected dimensions/orientation/pivots, local assembly offsets and collision
  intent. On reimport, verify component references, materials, offsets, pivots and collision still agree.

Nominate one disposable handoff fixture before repeated geometry production: a measured 1 m cube
with asymmetric direction markers, a separately exported hinged flap and a simple doorway frame.
It tests 100 cm imported bounds at scale 1, expected orientation, hinge rotation without orbiting,
collision blocking versus open passage, save/reopen and a deliberate source revision/reimport.
Use the actual player fixture for passage proof when available; before that, geometry checks alone
cannot certify player clearance. Failure returns to the recipe/fixture before bulk asset production.
No fixture or model is created by this proposal.

FModel is understood as an optional packaged-content inspection/extraction tool, not an authoring,
export/import or build dependency. Inspect owned editable assets through Blender/Unreal directly.
Do not substitute extracted cooked content for source assets or assume it recovers the complete
original project. Any future use for package inspection needs actual build compatibility proof.
See [FModel's documentation](https://github.com/4sval/FModel/wiki/Getting-Started) and
[Epic's packaging overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-your-project).

Documentation checked: [Epic units](https://dev.epicgames.com/documentation/unreal-engine/units-of-measurement-in-unreal-engine),
[coordinates](https://dev.epicgames.com/documentation/en-us/unreal-engine/coordinate-system-and-spaces-in-unreal-engine)
and [FBX pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine).
Epic documents centimetre defaults, pivots/collision and FBX compatibility requirements; this is not
a compatibility proof for the installed Blender exporter. Version-specific Blender manual fetches
were unavailable in this check; exact Blender export toggles remain unverified pending local proof.

## Accepted Graybox And Proxy Approach

Accepted in discussion, 2026-10-10. The first slice uses recognizable, simplified proxies to evaluate
scale, traversal, machinery fit and operation before detailed art. Exterior retains the XGP silhouette
and agreed envelope; interiors retain source-informed room/passage/opening shapes with simple surfaces.
Machinery has distinct moving parts, usable controls and actual clearance envelopes. Gene/Melfina
placeholders support body/occupant fit and readable posture/entry; screens and Gilliam provide readable
feedback and enough animation to demonstrate accepted behavior. Fine surface detail, polished textures
and elaborate character animation remain deferred.

Test intended dark-hangar reveal, guide lighting, limited-power and full-ignition lighting early:
visibility/navigation and reveal composition are functional design concerns, not only final polish.
Graybox success requires observed fit, movement and interactions; a recognizable appearance alone
cannot prove readiness. Renderer/settings/performance procedure still require separate review.
This accepted production direction creates no assets and does not claim runtime validation.

## Accepted Performance Measurement Contract — Execution Pending

Accepted in discussion, 2026-10-10, with p99 and first-use/cache clarification accepted 2026-10-11;
not executed. Target primary laptop, Win64, keyboard/mouse.
Later discussion revises the original required 120 FPS target to required native 1440p/60 FPS,
with 120 FPS retained as a stretch goal. Use the accepted initial rendering direction below, including
hardware-traced Lumen as the first candidate; this is not an automatic maximum-quality selection or
performance proof. The accepted learning track includes visible technology comparisons. Detailed quality
settings and individual feature adoption still need review and proof; no additional plugin, engine
branch or implementation is authorized.
Use 2560 x 1440 output and native internal resolution for the baseline, with dynamic resolution,
upscaling and frame generation disabled. Native-resolution temporal antialiasing remains compatible
with this baseline. Any later upscaled/frame-generated mode gets separate recorded results and image
quality review, not a replacement labelled native performance.

Test a standalone packaged Development build first for diagnostic access, editor closed; later repeat
in the intended distribution configuration. Record engine/build/commit ID, renderer and all quality
settings, internal/output resolution, window mode, driver, active GPU, display refresh rate, AC power,
power/fan profile and relevant background activity. Use uncapped, VSync-off capacity measurement and
a separate 60 FPS-capped playability check, plus 120 FPS where the stretch target is supported, with
display/sync settings recorded. Profiling captures
are diagnostic evidence with overhead; do not substitute a heavily instrumented run for baseline.

Repeatable session: ten minutes of representative warm-up to expose laptop thermal effects,
then three approximately five-minute route captures under unchanged conditions. Define exact route
checkpoints once playable: hangar reveal, boarding, laptop/dialogue UI, Melfina machinery, engineering,
ignition, full-power exploration and OFF/restart. Report phases separately so dark hangar or UI time
cannot conceal slow full-power scenes. Use documented reset/replay setup; first-use/cold-launch behavior
gets a separate capture, with loading boundaries identified rather than hitches silently discarded.
Exercise the natural 600 s revival path separately for duration/progression and sustained operation.

Required acceptance for each representative route segment in each warm run: average throughput
at least 60 FPS (frames divided by elapsed time); 95th-percentile frame time at most 16.67 ms;
99th-percentile frame time at most 25 ms, accepted 2026-10-11. This allows occasional modest slowdown,
not sustained operation below the average/p95 requirements. Stretch criteria retain average at least 120 FPS,
95th-percentile at most 8.33 ms and 99th-percentile at most 12.5 ms.
Percentiles use recorded frame durations, not an average
of instantaneous FPS counters or an ambiguously defined '1% low'. Log/count maximum spikes and any
active-play frame over 33.3 ms. Recurring or reproducible active-play hitches require diagnosis and
correction or an explicit reviewed exception before a pass; report isolated spikes as well.
These are project targets, not Epic defaults or measured host capability.

Use quick frame/CPU/render/GPU timing counters to locate the limit, and Unreal Insights for targeted
investigation; measure actual frame delivery rather than summing overlapping CPU/GPU work. Record
RAM/VRAM usage and repeated-loop growth as diagnostic evidence; numeric memory limits remain pending
real baseline data. Performance proof does not substitute for readability, interaction correctness
or body/machinery clearance proof. On failure, isolate causes and propose adjustments; do not silently
lower resolution, change lighting/quality, enable generated frames or relax the accepted target.

Reference: [Epic profiling guidance](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine)
and [Unreal Insights](https://dev.epicgames.com/documentation/unreal-engine/unreal-insights-in-unreal-engine).
Exact capture tools/settings and reproducible route remain to specify before execution; no tool is
installed or benchmark run by this contract. Detailed renderer/lighting quality settings remain separate decisions.

### First-Use, Shader/PSO Preparation And Cache Evidence — Accepted 2026-10-11

Keep three complementary measurements against the existing performance/package validation scenarios:

| Check | Required evidence |
| --- | --- |
| First-use gameplay | Capture the first reveal, lighting changes, screens, pod motion, engineering and ignition before the measured route has warmed those combinations. Record encountered stalls and their causes; a smooth later replay does not erase them. |
| Warm sustained performance | Apply the agreed warm-up and three route captures with the average/p95/p99 thresholds above. Record cache conditions as well as thermal/host conditions. |
| Startup preparation | Record shader/pipeline preparation and loading durations separately, with the point at which player control begins. Do not relabel an in-play stall as loading to omit it. |

Unreal prepares shader code during development/cooking, but a packaged game can still incur GPU/driver
pipeline creation costs. A PSO (Pipeline State Object) describes a combination of shaders and graphics
state. This affects both DirectX 12 and Vulkan; shader compilation and PSO preparation are related,
not interchangeable terms. Evaluate Unreal's PSO precaching and, if actual coverage gaps justify it,
bundled-cache workflows within later authorized build work. Enabling precaching alone is not proof
that the first-use route is hitch-free; use diagnostics to identify actual misses/late preparation.

Record build, backend, driver/settings and relevant cache state for each run. Distinguish a fresh
process launch from a cold-cache test: restarting can retain cached work. Any deliberate cache reset
needs a reviewed, project-scoped recipe; do not clear unrelated games' caches or broad driver/global
editor caches. Backend comparisons must report their own preparation/cache conditions. Development
DDC (Derived Data Cache), PSO descriptions and GPU/driver pipeline caches serve different roles.

First-use active-play spikes follow the same reporting and recurring/reproducible-hitch review rule
as warm runs. Startup duration remains reported evidence rather than a newly invented numeric limit.
A warm-run pass alone is not complete slice performance evidence. RAM/VRAM budgets remain deferred
until representative measurements; retain usage and repeated-loop growth as diagnostics.

References: [Epic shader development/cooking](https://dev.epicgames.com/documentation/unreal-engine/shader-development-in-unreal-engine),
[PSO cache overview](https://dev.epicgames.com/documentation/unreal-engine/optimizing-rendering-with-pso-caches-in-unreal-engine),
[PSO precaching](https://dev.epicgames.com/documentation/unreal-engine/pso-precaching-for-unreal-engine)
and [DDC](https://dev.epicgames.com/documentation/unreal-engine/using-derived-data-cache-in-unreal-engine).
No compilation, cache deletion, configuration change or benchmark is performed by this update.

## Accepted Rendering Learning Track — Bounded Experiments Pending

The accepted rendering learning track includes hands-on comparisons as development
progresses: direct/bounced lighting, Lumen, software/hardware ray tracing where supported, path-traced
reference rendering and supported DLSS features (Super Resolution, frame generation, ray reconstruction
and DLAA). Include PBR material/light-response comparisons as part of the same learning approach. Explain
each feature with matched scenes and record settings, visible differences and performance tradeoffs.

This is an accepted learning objective, not a requirement to ship every feature or a present authorization
to install plugins, initialize projects, switch engine branches or implement experiments. Schedule
small experiments within later authorized phases, using owned fixtures and verified compatibility.
Keep native acceptance results separate from upscaled/generated output. Path-traced references do not
prove real-time performance or replace artistic judgment. Laptop hardware offers an evaluation host,
not a guarantee that every feature/configuration meets the agreed frame-time budget.

Use the [Dusklight learning reference](../development/dusklight-learning-reference.md) for concrete
connections to texture replacement, graphics passes and reload/lifecycle concepts. It is an external
technical teaching reference, not XGP evidence or a dependency. RTX Remix belongs in contextual
remastering comparisons; do not assume it is required for Unreal authoring or implemented by Dusklight.

| Planned learning comparison | Owned fixture / expected lesson | Scheduling boundary |
| --- | --- | --- |
| PBR versus color-only surface changes | Same object/light/camera; vary base color, roughness, metallic and normal detail; compare painted/exposed metal, rubber, wood and glass transmission/refraction | Simple material exercise alongside authorized proxy/render work; detailed ship art still deferred |
| Direct light, shadows, AO and bounced lighting | Hangar/cockpit view; isolate each contribution, including dark/guide/limited/full-power states | After representative geometry and controllable lights exist |
| Lumen and supported software/hardware tracing | Matched camera/settings; compare indirect light, reflections, motion artifacts and frame cost | Pin supported engine settings; configuration trials within authorized scope |
| Vulkan versus DirectX 12 | Accepted learning comparison; same fixture/route, resolution and supported features; compare frame times, stability and visible results | DirectX 12 remains the proposed starting backend; verify installed-engine/driver support and separate Vulkan hardware-ray-tracing compatibility before later authorized trials |
| Shadow methods | Accepted exploration scope: conventional shadow maps, Virtual Shadow Maps, per-light hardware ray-traced shadows, distance-field shadows, contact-shadow supplementation and baked lighting/shadows where supported | Accepted learning scope, not a requirement to ship every method; use moving mechanisms, small controls and varied light sizes, restoring the baseline between comparisons |
| Path-traced reference | Fixed view of same geometry/materials/light; compare converged image with gameplay rendering | Optional offline/editor learning capture, not a runtime acceptance requirement |
| DLSS Super Resolution / DLAA | Same route; compare native versus reconstructed output, fine controls/text and motion stability | Verify compatible plugin and separately authorize adoption; record internal/output resolutions |
| Frame generation | Separate base-rendered and displayed rates; examine input feel and moving HUD/control artifacts | Supported integration only; never substitute generated output for native acceptance |
| Ray reconstruction | Supported ray-traced scene; compare noise/detail and stability with documented compatible reconstruction paths | Verify actual support before committing an experiment; no alternate engine branch assumed |
| RTX Remix context | Explain capture/remaster/material replacement in an identified example and contrast with our owned-source Unreal workflow | Teaching/reference topic; no Remix integration or Dusklight feature claim |
| Texture quality, mipmaps and filtering | Matched close/distant/oblique views of panel detail; inspect sharpness, shimmer, transitions and texture memory | Use owned test textures; no adoption of external texture packs |
| Depth of field and motion blur | Same cockpit view and camera/machinery movement with each effect independently off/on; compare focus, readability and motion appearance | Record settings/performance; full player graphics menu remains separately scoped |

Each executed comparison gets source/build/settings identity, matched captures and timings, a short
explanation of the visible result, and an adoption/defer/revisit decision. Change one feature at a time
where possible, restore the baseline afterward, and keep observations separate from expected results.
Unsupported experiments remain explicitly deferred with a reason; requesting exploration is not a
promise that every technology can be enabled together. Raw traces/captures remain local working data
unless publication is specifically reviewed; authored results/settings are trackable text.

Vulkan is a graphics API/backend, not a lighting or shadow technique; it is not assumed faster on this
host. Epic's current [hardware ray tracing documentation](https://dev.epicgames.com/documentation/unreal-engine/hardware-ray-tracing-in-unreal-engine)
describes Vulkan ray tracing on Windows/Linux as experimental. Backend comparisons must identify
feature differences rather than credit a faster result obtained by dropping effects. Baked lighting/
shadows may be demonstrated separately for learning, but do not replace the slice's required changing
lights and moving machinery. [Epic's shadowing overview](https://dev.epicgames.com/documentation/unreal-engine/shadowing-in-unreal-engine)
is the reference for shadow-method selection; compatibility is checked before each experiment.

The accepted first learning fixture comprises painted hull/exposed metal, glass, an emissive
control screen, a doorway/recess, one switchable overhead light and one guide light. Start with matched
direct-light versus Lumen GI/reflection views, then supported tracing comparisons and an optional
path-traced reference. Inspect appearance, lighting-change response and frame cost before testing
representative hangar/cockpit scale. This visual fixture may share the disposable handoff scene where
useful; passing it does not prove full-ship geometry, performance or traversal. Execution remains later.

## Accepted Graphics Quality Invariant And Viewing Preference

Accepted in discussion, 2026-10-10. Lower graphics quality may simplify presentation, but must not
change authoritative simulation rules/state, interaction availability, physical collision/clearance,
machinery endpoints or required controls. Preserve readable readiness feedback and navigable required
openings at every supported quality level. Visual LOD/culling cannot remove necessary controls or
supporting surfaces in their use context. Test essential screens/prompts and moving mechanisms when
quality changes; no lower-quality preset receives a pass solely because it is faster.

Clear gameplay views are the accepted viewing preference. Depth of field and motion blur are
OFF in the accepted initial gameplay baseline; compare both deliberately and independently in the
learning track. Depth of field is focus-related image blur, distinct from view distance or asset streaming.
Later optional player controls and exact menu scope remain for review. Artistic/cinematic experiments
do not silently override that gameplay preference, and quality presets should not unexpectedly
re-enable separately chosen effects.

Inspect texture mip completeness/consistency and close-to-far transitions in owned fixtures. Connect
the lesson to the [Dusklight reference](../development/dusklight-learning-reference.md), distinguishing
documented mip-sidecar support from user-reported texture-pack problems. No defect in a specific
pack/loader is independently diagnosed by this note. Graphics settings, menu implementation and
asset tests remain later execution work; this update records contracts and learning intent only.

## Initial Rendering And Anti-Aliasing Direction — Accepted 2026-10-11

Use DirectX 12 and the desktop deferred renderer as the initial candidate. Evaluate Lumen global
illumination/reflections with hardware ray tracing first on the primary laptop, retaining a matched
software-tracing comparison. Start with Virtual Shadow Maps; Lumen hardware tracing does not imply
that every light uses hardware ray-traced shadows. These are revisable starting choices, not build
compatibility or performance proof.

Start with TSR at 100% primary rendering resolution: internal and output resolution both 2560 × 1440,
dynamic resolution and frame generation disabled for native acceptance. Native rendering can still
use temporal anti-aliasing. Keep depth of field and motion blur OFF as already accepted. Exact quality
levels, tracing/reflection settings and shadow budgets remain to select or tune from measured results.

Accepted anti-aliasing learning comparisons: AA off, FXAA, TAA and native-resolution TSR in the same
deferred fixture; DLAA and DLSS Super Resolution after compatible integration is verified and authorized.
Judge stationary detail, moving detail and GPU cost, using cockpit labels, thin handles, metallic
highlights and extending engineering cylinders. Record shimmer, softness, ghost trails and newly
revealed surfaces rather than choosing from still images alone.

Desktop MSAA requires Unreal's forward renderer, which does not support Lumen. Explore forward/MSAA
in a separate fixture with compatible lighting; it is not a selectable AA mode in the deferred/Lumen
baseline. Vulkan is a separately accepted graphics-backend comparison and does not inherently require
switching from deferred to forward. Keep feature differences explicit when comparing performance.

References: [Epic rendering-path feature comparison](https://dev.epicgames.com/documentation/en-us/unreal-engine/supported-features-by-rendering-path-for-desktop-with-unreal-engine),
[anti-aliasing overview](https://dev.epicgames.com/documentation/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine),
[TSR](https://dev.epicgames.com/documentation/unreal-engine/temporal-super-resolution-in-unreal-engine)
and [NVIDIA DLSS/DLAA](https://developer.nvidia.com/rtx/dlss).
No engine settings, plugins, fixtures or project files are changed by this planning acceptance.

## Remaining Asset And Validation Boundaries

Git LFS policy is accepted, but its repository configuration has not been performed. Existing generated-output exclusions are a starting
boundary, not proof the future project/package excludes every forbidden file.

Proxy production must preserve required silhouette/scale, occupant paths, active machinery and future
reservations. Use own assets; user-supplied screenshots/fan render are reference only. Neither faithful
UI reconstruction nor file presence authorizes shipping source media. Detailed character/art production
is deferred; selected Gene/Melfina/Gilliam presentation still needs readable placeholders.

Performance target is the agreed laptop, Win64, keyboard/mouse and native 1440p/60 FPS required,
120 FPS stretch; it is not a
measured promise. Native measurement and separate optional-mode reporting are accepted; detailed
quality/tracing settings and executable lighting/capture procedures remain
to select. Do not hide settings/host conditions in an FPS claim.

## MCP Evaluation Order And Local Pilots — Accepted 2026-10-11

The accepted evaluation order places Epic's built-in Unreal MCP after the project/build proof, followed by
a Blender pilot at the existing post-3.1/pre-repeated-production checkpoint. Prefer the official
Blender candidate for investigation; adoption is conditional on code/license/client compatibility
and an agreed execution boundary. The accepted direction favors a practical workflow suitable for learning.

Local MCP pilots are the accepted initial direction for both editors; Sandbox/VM work is deferred. The
[editor-automation local pilot contract](../architecture/editor-automation.md#current-local-pilot-contract--accepted-2026-10-11)
owns this current direction: non-admin processes, loopback-only connections, on-demand servers,
reviewed specific tools/scripts, disposable fixtures, checkpoints and observed save/reopen/handoff/
recovery. Blender's bridge and background execution are local under the same reviewed account/scope.
No guest, custom transport relay or virtualization prerequisite remains on the initial path.

The accepted local tradeoff is explicit: generated code has the process account's filesystem/network
permissions. Project folders, backups and loopback listeners are not code containment. Unreal also
needs tool-surface review; its inspected restricted scripting/file tools do not establish blanket
OS isolation. Keep credentials, drivers, installation, unrelated filesystem work and Git publication
outside editor automation. Nothing is installed, enabled or connected by this plan update.

### Earlier Blender Isolation Investigation — Deferred Reference

The following 2026-10-10 investigation is retained history. Its proposed guest/network gates are
superseded by the local contract above and are not current execution prerequisites. Resume only
for a concrete reason with newly agreed scope; findings remain useful independent of adoption.

The [Sandbox pilot design and findings](blender-sandbox-pilot-design.md) now owns the 2026-10-10
read-only source/host investigation and proposed execution stages. Official source was retrieved
through its HTTPS API at pinned revision `dbbf836ad4b1025f14a2b3b504c43903f39e0b04` after browser
fetches failed. It confirms arbitrary Python execution and bypassable limited guardrails, not OS
filesystem/network isolation. Official provenance alone does not establish safe execution.

| Option | Practical benefit | Limit / unresolved proof |
| --- | --- | --- |
| Windows Sandbox pilot | Disposable virtualized Windows environment with configurable folder, clipboard, network and vGPU access | Verify availability, Blender graphics and actual MCP connection; closing discards guest state, while writable shared output survives and remains exposed |
| Persistent VM | Dedicated authoring environment with snapshots and limited guest data; more convenient repeated setup | More administration/storage; ordinary virtualized graphics may not expose the laptop GPU's native capabilities; verify authoring/export rather than assume Cycles/RTX parity |
| Restricted local Windows account | Native host GPU access with separate profile and explicit file permissions | Same OS; shared/public/project files remain reachable according to ACLs, network/credentials need separate controls; weaker boundary than VM and needs deliberate tradeoff review |
| Normal account with reviewed scripts/backups | Lowest friction and deterministic script review/recovery | Review and backups reduce mistakes but do not restrict arbitrary Python's filesystem/network access; not equivalent to isolation |

Recommendation for discussion: evaluate Windows Sandbox as a disposable pilot subject to the
connected-boundary gate in the design; use a persistent VM if required for practical isolation or
repeated setup. WMI confirms Sandbox is currently disabled and a hypervisor is already active.
No BIOS change, enablement or launch was attempted. The pilot record distinguishes those observations
from unavailable administrative servicing checks and unexecuted graphics/connectivity proofs.

A viable isolated pilot contains Blender and its execution-capable server/add-on in the guest, with
no personal profile, browser/Git/cloud credentials, source-media drives or full repository mounted.
Supply owned fixture/tool inputs through a read-only transfer folder and export only into a dedicated
writable disposable-output folder. Do not expose the parent repo, `.git` or home directory. Any writable
share is accessible to guest code; treat it as disposable and preserve originals outside it.

Disable unnecessary clipboard/device sharing. Install/bootstrap vetted dependencies separately, then
restrict network access for execution. Define and test the actual client-to-guest transport: disabling
all networking may prevent a host MCP connection, while a host-only virtual link does not automatically
prevent guest access to host services. A bridge/network rule must allow only the required control path;
do not enable general outbound access merely to make connection succeed. Keep execution in the guest,
not a host-side server with unrestricted local code. Exact network/bridge/isolation settings remain
specified in the pilot design as a preflight decision; source review is complete at its documented
limits, while exact transport/enforcement and executable setup recipes remain unselected. Both
Blender and the official bridge must be inside the guest because the bridge can launch background
Blender on its own machine. Stock HTTP is not an authenticated/restricted network boundary.

The user authorized drafting the Sandbox pilot and recording findings, not setup or execution.
Its offline bootstrap/graphics stage precedes connected access proof and generated geometry. A .wsb
networking toggle cannot express a destination allowlist, and guest-admin firewall rules alone are
not accepted enforcement against guest-generated code. If the restricted connected path is not
practical, revise the isolation choice rather than broadening access. Phase 1.4 remains open.

Pilot acceptance: show fixture input readable but not writable; confirm unrelated host paths absent
and intended network restrictions; discover tools, inspect scene, make one reversible fixture change,
save/reopen, export and stop/reconnect. Review output files before host import, including embedded code
and dependencies; keep Blender file auto-execution disabled for unreviewed output. This setting alone
does not sandbox explicit MCP Python execution. GPU/performance observations in a VM are not native
runtime benchmark results. On failure preserve logs/outputs, stop the pilot and return to reviewed
scripts/editor workflow while revisiting the isolation design; never broaden access silently.

Sources: [Blender Lab](https://www.blender.org/lab/mcp-server/),
[Microsoft Sandbox overview](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/),
[Sandbox configuration](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file)
and [Blender scripting security](https://docs.blender.org/UATEST/manual/en/dev/advanced/scripting/security.html).
No VM, account, firewall rule, driver, connector or application is installed/changed by this investigation.

MCP remains optional development automation. Candidate documents are dated and require verification
before selection/adoption. Pilot authorization, the chosen local permission boundary, license/dependencies, save/reopen recovery
and ordinary-editor/script fallback follow the existing contract. No always-on or packaged server.
Computer Use still requires specific explicit permission; ordinary phase approval does not grant it.

## Accepted Validation Split And Evidence Ownership — 2026-10-11

Use three complementary forms of proof against the existing
[VS1 validation register](vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability):

| Validation type | What it proves | Example |
| --- | --- | --- |
| Code/state checks | Rules, prerequisites, transitions and lifecycle behavior | Ignition rejects a partially stowed cylinder; reset prevents an old callback from changing the new session. |
| In-world checks | Physical interaction, motion, presentation and player experience | The upper engineering handle is reachable, the pod has clearance, and cockpit controls remain readable in both views. |
| Packaged-build checks | The actual build works outside the editor without MCP or source-media dependencies | A standalone build launches and completes its intended scenario with the required project-owned content. |

A passing state check does not establish physical fit or readable presentation. Scenarios that involve
both require both forms of evidence. Keep the early tiny standalone package proof at VS1-T04 before
investing in ship construction; repeat package validation at the later integrated checkpoints.

Each scenario's evidence record must include:

- Starting state, artifact/build identity and relevant settings/configuration.
- Steps and expected outcome.
- Actual outcome, with logs or visual evidence appropriate to the claim.
- Who performed the check, and explicit untested status for any part not executed or observed.

Codex performs appropriate build/state checks through available tools. The user is the main playtest
reviewer for feel, readability and visual fit. Tool success or editor launch alone cannot substitute
for observing the claimed result; any Computer Use observation still requires specific permission.
Reuse the existing scenario IDs and record evidence with them rather than creating a second checklist
or validation framework. The [foundation procedures](validation/foundation-validation-procedures.md)
specify VS1-T01–T04, accepted for planning 2026-10-23: availability versus effective selection, repository/LFS retrieval,
ordinary build/editor reopening and neutral packaged execution. All remain unexecuted. Other
per-scenario procedures remain to be defined at their owning checkpoints.
This acceptance records the validation approach only; no tests, fixtures or builds have been implemented.

## Next Review

Identity, responsibility, communication, asset versioning, handoff, proxies, performance direction and
learning conventions are accepted at the boundaries recorded above. Next review detailed renderer/settings choices, remaining project/map/input
details, exact lifecycle/recipe procedures, local MCP setup/client/tool checks and validation procedures.
Do not treat accepted conventions as executed fixture/build proof. Phase 1.4 completion needs all seven concrete contracts reviewed;
Phase 1.5 remains the separate final gate before authorized Phase 2 work.
