# Interaction Validation Procedures — VS1-I01–I03

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Status | Accepted for planning/publication 2026-10-23; all scenarios not executed |
| Scope | Phase 5 physical interaction, boarding and limited-service initialization; later integrated repeats remain required |
| Authority | [Scenario register](../vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability), [Phase 1.3 closeout](../phase-1-3-closeout-audit.md), [detailed interaction record](../phase-1-3-action-readiness-draft.md) |
| Execution prerequisite | Phases 3 and 4 accepted, plus authorization for the applicable Phase 5 subphase |

These procedures validate selected controls and feedback without introducing new mechanics, bindings,
reach distances or visual styles. They add no implementation. Phase 1.4 remains planning in progress;
Phase 1.5 and implementation remain unstarted.

## Shared Setup And Evidence

- Apply the [foundation evidence rules](foundation-validation-procedures.md#shared-execution-and-evidence-rules).
  Codex checks authorized logs/state/configuration; the repository owner observes input, readability
  and collision/feel unless another method is specifically authorized. Computer Use retains its
  separate permission requirement.
- Use the [G01–G03 spatial fixture](spatial-validation-procedures.md) and
  [S01–S03 shared state path](state-lifecycle-validation-procedures.md). Record actual body, camera,
  equipment, local range, movement/boot/gravity settings, input mappings and mechanism setup.
  Tunable values are run settings, not new canonical measurements.
- Run the required cases in both views over the same physical player. Observe prompt/target/input
  behavior and correlate it with actual request context, operation progress and authoritative state.
  A correct screen alone cannot prove physical locality or completion.
- Use normal player actions for positive interaction proof. Label any diagnostic setup separately;
  a debug bypass cannot establish that boarding, bootstrap or registration was completed by play.
- Record absent later machinery/full-power states as untested, with their owning repeat checkpoint.
  Do not implement later phases merely to remove a pending validation label.

## VS1-I01

**Physical targeting, equipment, text focus and result feedback**

**Owning checkpoints:** 5.1/5.4; actual machinery controls repeat in Phase 6 and integrated acceptance.

**Starting state:** accepted body/route and state fixture with authorized local controls, case/laptop
interaction and context adapters. No polished UI, controller integration or general inventory is required.

### Planned Steps

1. Approach ordinary controls from valid and invalid positions, including a third-person camera view
   that can see a control the body cannot reach. Verify target selection, readable prompt and shared
   validation use actual player context. Record selected range/occlusion behavior rather than inventing
   a universal reach value. Guidance cannot remotely perform the required work.
2. Request valid, unavailable and already-active actions. Prompts and results must distinguish missing
   prerequisites, in-progress and completed states without false success or consequential duplicates.
   Reopen a control after state changes while away; its availability must be current.
3. Draw/stow the laptop on demand in allowed contexts. Preserve hand-slot assignment and separate HUD
   drawn/stowed status. Hands-required actions temporarily stow as needed and restore the prior draw
   state only when allowed; a manually stowed item stays stowed.
4. Open Notes disconnected, then approach each supported connector with the laptop drawn. Proximity
   alone must not connect or start work. Explicit Connect must establish the actual target/workspace
   before enabling Connected Device, with no stale case/ship target retained.
5. Compare screen close, explicit Disconnect, walk-away and stow. Closing preserves the connection;
   explicit Disconnect leaves focused Notes available with device controls disabled; crossing cable
   reach safely disconnects before departure and closes focus while retaining drawn state; stow
   disconnects/closes/holsters while preserving slot assignment. Record cable/workspace fit limits.
6. On the case screen, compare typed and clickable input with the same code validation. Test wrong
   code and `VSDO2C`, visible characters, editing and submission. Typing suppresses gameplay hotkeys;
   Enter submits, Backspace edits and Escape first releases typing focus without disconnecting or
   closing the device. Case opening does not automatically begin resuscitation.
7. Open the menu or lose focus while movement/grip input is held. Check input release and fresh-input
   return, continued or paused simulation according to the accepted settings, usable UI during manual
   pause, and suppression of gameplay input while typing/menu focus owns it. Apply S03's pause-reason
   rules; actual machinery grip behavior repeats when those controls exist.

**Expected outcome / evidence:** controls are usable and readable in both views, with physical context,
equipment, focus and shared state in agreement. Retain input/target traces and observed positive and
denied actions, plus notes on prompt/readability problems. Later unit manipulation, seat locks and
apparatus controls cannot be passed through placeholder interactions alone.

**Recovery:** adjust only affected targeting, input routing, camera/UI or equipment adapters. Do not
weaken authoritative permissions, teleport cables/items or put debug class names into gameplay UI.
Rerun affected S/G checks when locality, body or geometry changes.

## VS1-I02

**Independent hatch actions, loaded boarding and interior ascent**

**Owning checkpoints:** 5.2/5.4; active-ship gravity exit/re-entry repeats at later integration.

**Starting state:** accepted supported hull/boarding route, same physical player, loaded equipment and
actual chosen hatch/panels, handhold and ladder. The hangar is breathable/pressurized and low gravity;
ship main services/gravity are initially unavailable. Record the selected tuning before testing.

### Planned Steps

1. Approach the entry through the supported hangar route. Toggle boots and distinguish enabled state
   from actual attachment/contact. Jump/reach the handhold and operate the exterior panel using the
   same body/equipment. Evaluate steadiness and reachable panel use without prescribing final metrics.
2. Open the hatch while holding position. Opening must not pull/teleport Gene inside. Allow remaining
   at the panel, releasing toward entry, or returning to the hangar with the hatch left open. Return
   later and board through that same opening; no one-shot assisted-entry trigger.
3. Observe hatch motion, collision and actual traversability. Test an obstructed closure under the
   accepted safe interaction rules: no false closed/sealed result, player damage or clipping through
   the obstruction. Preserve separate request, travel, closed-endpoint and check-completion states.
4. Enter and turn to use the interior closure control. Guide lighting can follow entry access, but
   Gilliam must not bootstrap from hatch opening. Keep the exterior opening, H03 internal ascent and
   cockpit emergency hatch identities distinct.
5. Ascend/descend the internal ladder with the back-carried trunk and accounted-for laptop. Local
   interaction grabs the ladder; forward/backward climbs, release stops and endpoints permit the
   selected assisted step-off. No midway jump-off. Temporary auto-stow/restoration follows I01 and
   must not hide carried clearance failures. Repeat in both views.
6. When limited services are available, observe the bounded seal/cabin check after actual exterior
   closure. Reopen to invalidate that departure result. The breathable-hangar premise must not turn
   this into filling a vacuum, a full leak network or an ignition interlock.
7. At later full-power integration, repeat exit/re-entry across ship gravity and hangar low gravity,
   preserving the same body/equipment and permitted hatch access. Record this as pending in Phase 5;
   neither startup success nor door opening is proof of the gravity boundary.

**Expected outcome / evidence:** independent open/board/close actions and loaded route work physically
in both views, with correct progress/access feedback and bounded departure-only seal status. Record
collision/approach observations, input and hatch/check state, source/identity references and relevant
MC-05/06 results. G02 static route proof alone cannot close this operating-entry scenario.

**Recovery:** preserve the accepted route; fix affected hatch, handhold, ladder or equipment integration.
Repeat dependent G/MC checks after a geometry change. Revisit an E placement if fit fails; do not merge
hatches, shrink carried props or add unreviewed pressure/decompression behavior to make entry work.

## VS1-I03

**Limited services, laptop bootstrap and deterministic guidance**

**Owning checkpoints:** 5.3/5.4; occupied apparatus/main ignition repeats in Phases 6–7.

**Starting state:** functioning I01/I02 route/adapters and shared state, main services/gravity OFF,
apparatus stowed and four units not yet prepared. The initial independent operating supplies remain
qualitative E/F assumptions; no numeric battery, circuit or endurance model is required.

### Planned Steps

1. Verify guide lighting supports the entry-to-cockpit route without Gilliam or main power being
   falsely online. Facility controls, boots, laptop and case retain their accepted pre-main use.
2. Connect the laptop at the selected local bridge workspace. Explicitly activate the scripted
   override on the initial grid screen; connection alone must not run it. After actual override
   completion, activate the source-informed activation/countdown sequence. Use owned presentation
   assets derived under the evidence policy, not source-media packaging dependencies.
3. Pause/resume bootstrap with HOLD, checking progress and a readable indicator beyond color alone.
   It must not pause independent case revival or the whole simulation. Keep KEY presentation inactive
   as selected, without inventing another usable control. Cancel via the shared disconnect pathways
   while running/held; no stale callback may later complete the attempt. Reconnect/retry and retain
   already completed effects under the accepted contract.
4. On actual bootstrap completion, observe limited lighting/services and Gilliam's ceiling pod/text
   presentation. Main engines, artificial gravity and startup milestone remain unavailable/incomplete.
   Request unavailable work and compare status/guidance with the authoritative missing prerequisites.
5. Exercise Gene registration through the direct and failed-recovery branches plus hold-off/resume.
   Preserve completed steps while exploration continues; resume the incomplete line/checkpoint
   without repeated completion. With the case closed, Gene can register while Melfina's visible
   recognition beat remains deferred. Keep personnel state distinct from navigation availability.
6. Check available preparation guidance after registration without auto-operating equipment. Where
   case revival exists, its explicit start/independent progress must coexist with bootstrap/registration;
   completion leaves the occupant waiting for the agreed local transfer rather than deploying her.
   Actual transfer, engine manipulation and their completion remain Phase 6 proof.
7. Reset from incomplete and completed bootstrap/registration states and query reopened UI. Restore
   the accepted initial snapshot without stale limited-service success, dialogue steps or notifications;
   an ordinary later OFF/ON cycle must not replay the introduction. Use S03 for controlled callback
   cases and repeat with actual machinery during integrated lifecycle validation.

**Expected outcome / evidence:** the real laptop/control path creates only the intended limited
services; controls, Gilliam guidance and registration reflect shared state. Retain visible sequence
and branch observations, operation/context/progress records, main-service/gravity negative checks,
and cancellation/reset evidence. Text and pod presentation do not certify full navigation/ignition.

**Recovery:** correct the narrow connection, bootstrap, dialogue or service adapter. If accepted
early-service assumptions cause a deadlock or conflict with evidence, review that premise rather than
inventing power hardware or automatically completing missing work. Preserve authored dub lines and
branch behavior; wording polish, visual timing and numeric parameters remain their existing deferrals.

## Completion Boundary

These procedures are accepted for planning on 2026-10-23, not implemented interactions or test results. Phase 5 acceptance requires
its existing exit review and observed evidence. Machinery, restart/readiness, integrated timing and
packaged acceptance remain with VS1-M/R/A scenarios. No engine launch, installation, asset import,
modeling or gameplay implementation occurs in this documentation increment.
