# Phase 1.3 — Player Actions And Readiness Discussion Draft

Status: authorized preparation in progress, 2026-10-07. The user asked for independent draft work
and a prepared discussion queue while away. New recommendations below are **not accepted**.
No implementation, installation or model is authorized by this preparation. The user confirmed
publication of the current discussion checkpoint; that does not accept the remaining recommendations
or complete Phase 1.3.

Inputs: accepted [Phase 1.2 closeout](phase-1-2-closeout-proposal.md), its
[discussion record](phase-1-2-spatial-motion-decision-packet.md),
[slice contract](../reconstruction/baseline-v1/vertical-slice-1.md),
[operational vocabulary](../reconstruction/baseline-v1/operational-state-baseline.md),
[interaction](../architecture/interaction-system.md),
[player/camera](../architecture/player-camera-control.md) and
[shared-command requirements](../architecture/external-control-automation.md).
Evidence remains owned by those source-linked records. No new episode/audio or Japanese review.
All new action rules, interlocks and service assumptions are E/F proposals, not canon.

## Established Constraints

- One physical player and shared ship state across both camera perspectives. Camera changes do
  not change local permissions, progress, carried equipment or occupant state.
- Start inside the facility airlock, doors closed, trunk secured on the back and closed computer
  carried in one hand. Dark hangar, ordered lighting reveal, rectangular lower entry and H03 ascent
  lead to the cockpit; no direct cockpit boarding.
- Manual switchable magnetic boots with mode/contact distinction, a stabilized hatch approach
  and notification when ship gravity becomes available after completed main ignition. Numeric gravity
  and transition tuning remain open.
- Entering-right trunk staging; placed case is player-nonblocking for this demo. Its visible geometry,
  moving machinery, occupant and ordinary route still need fit checks.
- Case code lead `VSDO2C`, reference-inspired revival with a 600 s default and a local second
  interaction to skip remaining revival time. Code interpretation remains track/source-qualified.
- Computer bootstrap at the pilot workspace, basic registration/status, deterministic Gilliam guidance.
  Disconnect/close/stow before seat lift; Gilliam remains available afterward under the agreed adaptation.
- Preparation can overlap revival. All four engineering endpoints, occupied navigation apparatus,
  operating seat position and completed ignition are still required for SHIP READY.
- Guidance cannot complete required local engineering work. No flight, crew AI, damage model,
  numerical power model, general inventory UI or generated dialogue is needed.

## Minimal State And Ownership Proposal

### Exterior Hatch — User-Selected Independent Actions

During Phase 1.3 discussion the user selected independent exterior opening, boarding and interior
closure rather than an assisted entrance triggered by opening the hatch:

- Jump to a handhold beside the exterior keypad/panel and steady there to operate it.
- Panel interaction opens the hatch without pulling the player inside. The player can remain,
  release toward the opening, or return to the hangar floor while leaving the hatch open.
- An open hatch remains available for a later jump/entry; opening is not a one-shot boarding trigger.
- Once inside, turn back to an interior control to close the hatch. This proposed interior panel
  and its placement are E/F, not newly verified source hardware.
- The user wants closure to contribute to a startup airtightness/pressurization requirement.
  This extends the prior no-required-pressure-check direction; exact service dependencies,
  pressure representation and readiness gating remain for discussion before adopting the contract.

Recommended boundary: track hatch motion/closed endpoint separately from seal-check completion
and any selected pressurization result. A close request is not closure; closure alone does not
prove all ship openings sealed. Do not assume H02/H03/future branches are exterior leaks or silently
implement a whole-ship pressure network. Reopening must invalidate the affected seal/ready result.
No assisted pull-in is selected; low-gravity control, landing support and optional entry-edge
assistance still need fit/feel discussion. Holding the ship during panel use does not require boarding.

The user agreed the separate closed → seal verified → pressure-ready results and reopening
invalidation. They selected an already pressurized, breathable hangar for the opening. The user
cites EP-04's later remote opening of the large facility exterior door to eject attacking pirates
as supporting evidence. This is a user-supplied episode lead, not a newly inspected frame/audio
observation; exact interval and pressure implications still need targeted verification. No new
decompression scene or remote facility-door gameplay is added to the slice.

Under the selected demo premise, the ship's boarded spaces are initially breathable through the
open connection to the hangar. Closing the hatch establishes an independent boundary; do not
portray it as filling an initially evacuated cabin. Recommend the later startup step verify the
seal and acceptable cabin pressure, with conditioning/top-up presentation only if selected.
Numerical pressure, gas transfer and leak simulation remain deferred. Startup gating and the
response to reopening remain D13-09 decisions; reopening into this pressurized hangar does not
automatically mean decompression or immediate engine shutdown.

The user agreed bootstrap and available preparation can proceed with the ship hatch open.
They subsequently revised the earlier seal-before-ignition rule: hatch sealing/pressure readiness
constrains departure readiness, not engine ignition or the startup milestone. Hatch opening supplies
guide lighting only; Gilliam boots exclusively through the bridge laptop connection/bootstrap action.
Once available, Gilliam may report the open hatch and direct the player to its interior panel.
The player may close it immediately, return later, or complete startup with it open. Reopening
invalidates affected seal/departure results without shutting down engines or ship gravity in this
pressurized-hangar demo. Check execution/services and other represented boundaries remain open.

### Startup Milestone And Continued Exploration — User-Selected Direction

SHIP READY means the slice's startup milestone, not a launch clearance or an end-of-demo trigger.
After completed startup the player can leave the captain's seat, walk the included rooms, reopen
the boarding hatch, exit to the hangar and re-enter. No forced ending screen, reset or input lock.
Leaving the seat does not undo the completed seat/lift action or turn off running services.

Keep startup completion distinct from departure readiness. An open hatch or outstanding seal/pressure
check may produce “startup complete; departure readiness incomplete” in cockpit/Gilliam status.
No launch command or full departure checklist is implemented merely to display that bounded warning;
clearing it does not certify all future flight requirements. Other unfinished startup prerequisites
still prevent ignition under the selected contract.

After ignition, gravity applies in the selected ship interior region. Crossing the hatch into the
hangar returns the same player to hangar low gravity; crossing back restores the ship's active field.
An open hatch does not turn off the field throughout the ship. Preserve movement/equipment across
the boundary, including falling/jumping/climbing and magnetic-boot contact. Exact field boundary,
blend and acceleration remain E/F graybox tuning; do not assume a doorway opening changes pressure
or gravity identically. No sudden velocity reset, respawn or mandatory boot-mode change is selected.

### Hand Slot And Draw/Stow — User-Selected Direction

The user selected this F equipment behavior during Phase 1.3 discussion on 2026-10-07:

- Keep the item assigned to a hand slot distinct from whether it is drawn in the hand. The portable
  computer can remain the equipped hand item while physically stowed in its agreed holster.
- Provide an on-demand draw/stow hotkey during ordinary play, without opening an inventory menu,
  unassigning the slot or requiring a contextual interaction point. Exact binding remains undecided.
- Keep the assigned item's HUD icon visible while stowed; separately indicate drawn/stowed status.
  Temporary hands-required restrictions must not look like the item was unequipped or lost.
- Actions needing both hands may temporarily auto-stow the drawn item. Retain its slot assignment
  and account for its physical storage throughout climbing or other protected transitions.
- This distinction should support future hand items, including weapons; it does not add weapons,
  multiple equipment slots, item swapping or a full inventory UI to this slice.

Workspace/connected computer use remains a distinct physical context: the draw/stow hotkey must
not teleport a connected computer or cable into the holster. Disconnect/close/stow handling and
feedback for unavailable draw requests during protected actions still need discussion.
The user also selected restoration of the pre-action draw state: after a hands-required action,
automatically redraw an item that was drawn before temporary auto-stow; leave a manually stowed
item stowed. Restore only when the current physical context permits drawing, without bypassing
another hands-required action or a connected/workspace state. HUD styling and transition timing
remain proposals.

These are descriptive fields, not C++ names, APIs or a universal simulation framework. Exact
implementation ownership and presentation technology belong to Phase 1.4.

| Domain | Minimum information to distinguish | Initial draft condition / boundary |
| --- | --- | --- |
| Player context | Physical location, exploration/climb/station/seated context; assigned hand item, drawn/stowed status and temporary hands-required restriction | Exploration; trunk back-carried, computer assigned and drawn. Initial boot mode ON is recommended, contact requires a suitable surface. |
| Player condition | Supported initial healthy condition | No damage, numerical health, oxygen, stamina or equipment battery drain introduced. |
| Environment | Facility lighting sequence, local gravity availability, suitable contact surfaces, bounded atmosphere status | Facility lights off; pressurized/breathable hangar selected; low-gravity premise. Stable walk is F boot-assisted tuning, not boots generating gravity. |
| Access | Each chosen door/hatch state and traversability; selected hatch closure and prospective seal-check result kept separate | Facility doors closed; selected ship entry closed. Independent opening/boarding/interior closure agreed; startup pressure contract pending. Keep unrelated hatch identities distinct. |
| Trunk/occupant | Carried/placed, locked/open, revival not started/running/complete, occupant transfer/apparatus location | Locked, inactive occupant. These states do not equal navigation availability. |
| Computer/Gilliam | Held/stowed/workspace, cable connected, bootstrap progress, Gilliam available, registration progress | No live ship session. Computer's independent operating supply is qualitative E; no capacity model. |
| Ship services | Guide lighting, limited bridge services, machinery-service availability, gravity availability, main-service startup/available | Main services unavailable. Initial guide-light and pre-main machinery source are proposed below, not verified wiring. |
| Apparatus/seat | Supported physical stages and actual completion | Apparatus stowed; seat group low. Occupant, cap, cylinder and covers tracked separately rather than one instant boolean. |
| Engineering | Each of four units' wrapping/release/extension/prepared progress | Banded/closed. Project IDs do not establish exterior-engine mapping or canonical numbering. |
| Readiness | Required conditions met/missing, ignition pending/running/complete, aggregate ready | Preparing/incomplete; never a separately editable UI flag. |

The HUD reads player condition, boot mode/contact, assigned hand item and distinct drawn/stowed status, plus relevant action/result
feedback. Gilliam reads the same services/mechanisms/readiness. Neither maintains a competing state.

## Initial Services And Gravity — Recommendation For Discussion

Use a bounded commissioning-service assumption, separate from main engine ignition. Facility controls,
personal boots, the portable computer and the revival case can operate without the ship's main engines.
Opening the ship entry makes low-level guide lighting available. Computer bootstrap then enables
limited bridge interaction and the service capability needed to prepare machinery. This explains
pre-main access without inventing battery chemistry, wattage or canonical bus names.

**User-selected gravity milestone:** ship gravity stays offline throughout preparation and becomes
available after completed main ignition, announced by Gilliam. Laptop bootstrap enables limited
services, not gravity. Use boots for controlled grounded preparation; boots-off movement can drift
in low gravity. Facility/hangar remain low gravity. Boots stay manually controllable; do not silently
change their switch setting when gravity comes online. Enabled boots attach only on suitable contact.

The user corrected their scene citation to EP-04, 10:05–10:07 and 11:54–12:00, describing Jim's
low-gravity movement through the ship. These are user-supplied visual leads pending a targeted
motion review; the subtitle cache aligns the latter with engineering work but cannot prove drifting.
Keep the original EP-03 citation superseded. Reactor/main-power support for artificial gravity is
an E/F reconstruction rationale, not a verified canonical power requirement. The earlier proposal
to enable gravity at bootstrap is rejected. Melfina's short pre-ignition transfer must also account
for low gravity; do not silently supply normal gravity only for her animation.

Boundary transitions must preserve the same player and equipment. Recommend a brief controlled
gravity blend, with stable footing before station interactions; exact blend and numeric jump/gravity
tuning are later graybox parameters. No new required gravity-generator button or pressure simulation.

## Draft Normal-Path Action Table

“Local” requires the relevant physical actor/context; an on-screen prompt alone cannot grant access.
Rows marked with D13 refer to the unresolved discussion queue. Completion is an actual state/motion
endpoint, not merely an accepted request. Order permits the stated parallel preparation branch.

| ID / action | Local context and proposed prerequisites | Completion / feedback | Open choice |
| --- | --- | --- | --- |
| A13-01 Inner facility door | At door control, exploration, no obstructed door sweep | Door reaches traversable endpoint; outer door remains closed | D13-02 interaction style; no pressure check added |
| A13-02 Hangar lights | At nearby switch; facility supply assumed available | Near-to-far overhead sequence then ambient lights; progress remains readable while walking | Reveal pacing later tuning, not a camera lock |
| A13-03 Boot toggle | Player equipment action; cannot detach during a protected climb/handhold transition | Mode change reported separately from attached/no contact | D13-02 timing/binding; numeric locomotion deferred |
| A13-04 Jump/steady at ship entry | Boots disengaged for jump; reachable handhold; loaded body fits | Stable hatch-control context; release/return to hangar or enter separately | D13-02 movement/entry feel; opening never auto-boards |
| A13-05 Exterior hatch | Local exterior panel while supported by handhold/stance; clear sweep | Opening complete; remains open for independent later entry; guide lighting available under service proposal | D13-01 supply assumption; exact hatch path remains E |
| A13-05b Interior hatch closure | At proposed interior panel; hatch sweep clear; player has independently entered | Actual closed endpoint; separate seal/pressure check may clear the represented departure warning | D13-09 check/service behavior; closure does not gate ignition |
| A13-06 H03 ascent | Local ladder/access; loaded route fit; drawn computer may auto-stow before hands-required climb | Same player/trunk reaches upper landing; computer remains assigned/accounted for; restore its prior draw state when permitted | D13-02 climb feel and protected-transition handling |
| A13-07 Place trunk | At designated cockpit marker, carrying closed case | Case placed in agreed orientation; back mount clear | Re-pickup during revival recommended unavailable; D13-04 |
| A13-08 Unlock/open case | Local case panel; placed; valid code | Lock released and lid reaches open endpoint; invalid code gives readable feedback | D13-04 code delivery and input format |
| A13-09 Start revival | Local case control; placed/open; occupant inactive | Running 600 s progress; completion makes occupant awake, not navigation ready | D13-04 automatic on opening versus explicit start |
| A13-10 Revival shortcut | Local case control only while running | Remaining time skipped; same completion/transfer path, other prerequisites unchanged | Clear demo label; no instant all-systems completion |
| A13-11 Computer setup/connect | At pilot workspace; computer available; connection area reachable | Workspace/cable established; separate from bootstrap completion | D13-02 one contextual setup versus several small actions |
| A13-12 Bootstrap/register | Local bridge computer session; connected; ship hatch need not be closed | Laptop bootstrap makes Gilliam and limited services available, without ship gravity; registration result reported distinctly | D13-03 registration scope; hatch opening alone never boots Gilliam |
| A13-13 Disconnect/close/stow | At workspace; bootstrap complete; no active session requiring connection | Cable clear and computer secured; Gilliam persists | Approved spatial holster; D13-02 interaction granularity |
| A13-14 Engineering wrapping/release | At each required unit's controls; service prerequisites according to selected contract | Individual wrapping/release progress; no prepared flag yet | D13-06 repeated steps and interaction feel |
| A13-15 Engineering extension | Local unit, released, powered if required, operator/sweep clear | Actual extended/prepared endpoint; all-four aggregate derived | D13-06 mechanical adaptation; D13-08 obstruction behavior |
| A13-16 Occupant transfer | Revival complete, open apparatus approach clear; Gilliam/services as selected | Short scripted movement to apparatus, readable pending if blocked | D13-05 automatic versus player acknowledgement |
| A13-17 Apparatus deployment | Occupant staged, required services, clear cap/descent/cylinder/cover volumes | Supported stages reach available endpoint; closure bridge explicitly F | D13-05 trigger/closure and D13-08 interruption |
| A13-18 Take station/seat lift | Computer/cable stowed, occupant/machinery coordination valid, lift volume clear | Same player occupies operating station; actual raised endpoint | D13-07 one station action or separate raise control |
| A13-19 Ignition | At pilot key, required navigation/all-four/seat/service preparation complete; hatch closure/seal/pressure result is not an ignition prerequisite | Startup in progress then actual main-services/gravity availability | D13-07 key action and timing; no canonical full bus topology |
| A13-20 Ready report | Derived query after actual ignition completion and all eight conditions | SHIP READY startup milestone; keep playing, leave seat and explore/exit/re-enter; separate departure warning if hatch open/check outstanding | Actual startup and departure results remain distinct; no launch action required |

Engineering preparation and available cockpit work may run while revival progresses. A13-16/17
wait for revival; A13-19 waits for the selected preparation predicates. Navigation completion must
not be implied by timer completion. This is a partial-order experience, not one global ship state ladder.

```mermaid
flowchart TD
  A[Loaded arrival and physical boarding] --> B[Place and open case]
  B --> C[Revival running: 600 s or local shortcut]
  B --> D[Computer bootstrap / Gilliam / initial services]
  D --> E[Local engineering and available cockpit work]
  D --> F[Disconnect and stow computer]
  C --> G[Occupant transfer and apparatus deployment]
  D --> G
  G --> H[Operating station / lift]
  F --> H
  E --> I[Ignition request]
  H --> I
  I --> J[Actual ignition completion and readiness query]
```

Diagram shows recommended dependencies for discussion, not accepted interlocks. Starting revival
before bootstrap is supported by the proposed independent case supply, not a discovered canonical
power circuit. Whether engineering extension specifically needs initial services is still a choice.

## Request, Progress And Recovery Rules — Draft Defaults

- Validate target, local context, equipment, prerequisites and occupied sweep before beginning an
  action. Report rejected/unavailable with the actual reason; do not advance state on rejection.
- Repeating an already completed request reports its existing result without repeating motion,
  removing wrapping twice or duplicating registration/occupants. Repeating a running request reports
  progress rather than starting another operation. Exact result/API names remain for 1.4.
- Serialize conflicting actions on the same mechanism. Parallel independent revival and preparation
  is allowed; key ignition cannot race missing preparation into a ready result.
- Recommend single-press initiation for most controls, with progress until a real endpoint.
  Walking away closes optional UI but does not automatically reverse a started mechanism or pause
  revival. Hold-to-work and deliberate mechanical gestures remain D13-02/06 discussion choices.
- Before motion, block a start if the relevant sweep is occupied. During motion, recommend a
  non-damaging pause with “clear the mechanism” feedback, preserving intermediate state and
  resuming only when clear. No crushing, health damage, repair or arbitrary teleportation. Exact
  behavior for carried player/occupant inside a supported motion is separate from an obstruction.
- Climb, station lift and occupant transfer need a defined protected transition/cancel boundary;
  no mid-shaft drop or automatic camera-mode workaround. Camera changes cannot bypass it.
- Revival keeps progressing after the player leaves, and cannot be canceled/restarted through a
  duplicate activation. Recommend preventing case carry/closure while running; this is a usability
  rule to discuss, not a general canonical medical model.
- Recommend measuring revival in active play time: it continues while walking away, but a deliberate
  full-game pause freezes it with other simulation progress. No background wall-clock completion
  while the demo is closed. Pause/time semantics remain D13-04 discussion input, not a selected engine timer.
- On a fresh run/reset, restore doors, lights, equipment, case lock/timer/occupant, computer session,
  services/gravity, four units, apparatus, seats, ignition and ready result. Prior callbacks cannot
  complete new operations. Save/load, checkpoints and universal shutdown remain deferred.

## Eight Readiness Conditions — Observable Draft Mapping

| Baseline condition | Required observable result | Must not count as completion |
| --- | --- | --- |
| 1 Entry and route | Selected physical entry completed; required bridge/engineering route usable | A remote command or marker claiming the player boarded |
| 2 Initial services | Selected bootstrap/service result completed and usable | Connected cable alone or a highlighted switch |
| 3 Navigation apparatus | Actual occupied deployed/available apparatus endpoint | Case open, timer finished or Melfina awake alone |
| 4 Engineering | All four independent prepared endpoints complete | One demonstrated unit, all-four request acceptance or guidance text |
| 5 Seat/control cluster | Operating endpoint complete with valid context during startup; afterward the player may leave the seat without undoing completion | Entering seat UI while lift still moving; requiring permanent seat occupancy after success |
| 6 Ignition | Key/startup action completes and main-service/engine/gravity presentation agrees | Key press or start of animation; hatch-open departure warning treated as failed ignition |
| 7 Consistent report | HUD, Gilliam and status query read the same completed aggregate | UI-owned ready flag or scripted congratulation bypass |
| 8 Supported endpoint | Ship remains supported in hangar; startup success leaves exploration and exit/re-entry available | A launch command, forced demo ending or countdown needed to finish |

Readiness is F and does not certify future weapons, flight or sub-ether capability. Health/boot mode
is not another arbitrary ignition prerequisite. Required stow and local access protect the chosen
operation, not an invented universal ship safety regulation.
Route usability and the supported hangar pose are spatial acceptance invariants as well as operating
constraints; do not invent a runtime “geometry passed” switch to replace actual traversal evidence.

## Discussion Queue For The User's Return

Discuss these in experience order; recommendations are starting points, not choices already made.
Exact key bindings, art style, timings and metric locomotion can follow the behavioral decisions.

| ID / topic | Recommendation to discuss | Material alternative / effect |
| --- | --- | --- |
| D13-01 Initial services and gravity | User selected low gravity throughout preparation, ship gravity available after completed main ignition and Gilliam notification; boots stay manually toggled. Laptop bootstrap supplies limited services without gravity. | Qualitative supply assumptions, exact gravity blend/tuning and low-gravity occupant-transfer staging remain to resolve. EP-04 motion leads are recorded, not yet visually verified. |
| D13-02 Boarding and everyday actions | User selected assigned hand slot, on-demand draw/stow hotkey, separate HUD drawn status, temporary auto-stow and restoration of the prior draw state afterward. Guided physical ascent/local interact remain recommendations. | Protected-action feedback, climb feel and connect/disconnect granularity still need discussion. |
| D13-03 Gilliam registration | Brief local scripted acknowledgement and fixed demo operator role; registration completes without a character creator, followed by text guidance/status. | A name entry or several questions can personalize the opening; scope/identity/wording must be selected. |
| D13-04 Case and code | Code available as a readable starting note; enter it locally; opening and “begin revival” are separate deliberate actions. Running case cannot be moved/closed. Shortcut clearly labeled; timer uses active play time and freezes on full-game pause. | Known-code prompt or automatic revival on opening reduces actions; discovery/puzzle format needs a source of the code and cannot block the demo unintentionally. Confirm pause semantics with pacing. |
| D13-05 Melfina and apparatus | On revival completion, notify player; local acknowledgement initiates short transfer and a staged deployment. Keep cap closure an explicit provisional transition. | Automatic transfer/deployment lets prep continue but may make the player miss the central machinery sequence. Separate apparatus controls offer more hands-on staging. |
| D13-06 All-four engineering workflow | Repeat a short local unseal/release/extend workflow per unit, preserving distinct completion and source order; describe three repetitions as F. | One local bank-wide command after physical releases is shorter; fully gestural handles/wrapping is more tactile and requires additional motion/input fit. |
| D13-07 Seat and ignition | Explicit take-station action triggers protected seat lift after stow/navigation; separate key interaction starts ignition after all-four prep, with visible progress. | Separate seat-raise control is more manual. Ignition should remain a distinct deliberate action under either option. |
| D13-08 Interruptions and presentation | No-damage obstruction pause/retry; case timer continues while away; concise text instruction/status, persistent equipment HUD and contextual prompts. | Hold-to-work, reversible mechanisms, dialogue acknowledgement and presentation style may change pacing. Do not add failure/damage systems to get recovery behavior. |
| D13-09 Hatch sealing and pressurization | Independent opening/entry/interior closure and seal/pressure results agreed. Hangar breathable. Hatch/check results gate represented departure readiness, not ignition; reopening updates that warning without shutting down engines/gravity. Startup success allows continued exploration and ship/hangar gravity transitions. | Decide check execution/services, represented boundaries and status wording. No whole-ship pressure network, launch system or exact gravity-field shape selected. |

First discussion recommendation: boarding/control feel and gravity, then case/registration/Melfina,
then engineering and final station/key. The dependent rows remain drafts until those choices are made.
Resolve D13-09 with initial-service dependencies before freezing the ignition/readiness contract.

## Validation To Specify After Discussion

Planned scenarios, not executed tests: boot ON/no contact versus attached; loaded boarding in both
views; open hatch without boarding, return to hangar and later re-entry, interior closure and blocked
closure, separate seal/pressure completion and invalidation on reopening;
computer physically accounted for through climb/stow; manual draw/stow keeps slot assignment
and HUD icon, temporary auto-stow preserves assignment and respects connection/context restrictions;
post-action restoration redraws a previously drawn item but leaves a manually stowed item stowed;
wrong code; duplicate start/skip;
600 s natural completion and separate shortcut; prep overlapping revival; all-four local completion;
blocked transfer/sweep and clear/resume; no ignition while prerequisites incomplete; consistent
in-progress/completed readiness; fresh reset during timer/motion/ignition with no stale completion.
Also verify successful ignition with hatch open, separate departure warning, seat exit after startup,
continued traversal, hatch reopen/close and exit/re-entry through the active-ship/low-gravity-hangar
boundary in both views. Startup completion must not end play or make the seat permanently occupied.

Use existing VS/VS1 validation owners in the implementation plan; Phase 1.4 will set concrete
procedures and manual/automated evidence arrangements. No checklist is complete from these drafts.
VS-D04–06 remain open for discussion. Phase 1.4 is not started automatically.
