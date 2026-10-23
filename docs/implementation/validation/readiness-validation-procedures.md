# Ignition, Readiness And Repeatability Procedures — VS1-R01–R03

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Status | Accepted for planning/publication 2026-10-23; all scenarios not executed |
| Scope | Phase 7 actual key/service transitions, startup milestone, guidance and repeated runs |
| Authority | [Scenario register](../vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability), [slice completion criteria](../../reconstruction/baseline-v1/vertical-slice-1.md#ship-ready-definition), [Phase 1.3 closeout](../phase-1-3-closeout-audit.md) |
| Execution prerequisite | Phase 6 exit and authorization for the applicable Phase 7 subphase |

These procedures integrate accepted physical and shared-state behavior. They add no ignition gates,
flight controls, emergency cutoff, pressure/power simulation, saved achievements or save/load system.
Phase 1.4 remains planning in progress; Phase 1.5 and implementation remain unstarted.

## Shared Setup And Evidence

- Apply the [foundation evidence rules](foundation-validation-procedures.md#shared-execution-and-evidence-rules).
  Codex checks authorized state/log/configuration evidence; the repository owner observes actual
  controls, service presentation, movement and feedback unless another method is specifically
  authorized. Computer Use retains its separate permission requirement.
- Carry forward [state/lifecycle](state-lifecycle-validation-procedures.md),
  [interaction](interaction-validation-procedures.md) and [machinery](machinery-validation-procedures.md)
  cases. Record the real player, context, session/operation IDs, all-four unit conditions, apparatus,
  key/seat state, service/gravity progress and relevant camera/input settings.
- Positive completion uses the actual player route, local controls and real machinery. Label any
  diagnostic setup for negative-case isolation; a seeded ready flag cannot prove SHIP READY.
- Keep historical per-run startup success, current operating state and represented departure status
  separate in evidence. Route fit and the supported hangar pose also require physical observations;
  do not create a runtime geometry-pass switch to stand in for those checks.
- Full packaged acceptance and measured host budgets remain VS1-A02/A03. An integrated editor run
  does not establish either. These procedures reuse existing acceptance criteria and introduce no
  numerical timing, gravity or visual-quality thresholds.

## VS1-R01

**Physical key, ignition, shutdown and current-condition restart**

**Owning checkpoint:** 7.1, with actual M02/M03 coordination repeated.

**Starting state:** actual low captain's seat, local key interaction and machinery/service adapters.
For the positive case, registration, limited services, occupied navigation apparatus, all-four
engineering preparation and computer/cable clearance satisfy the accepted prerequisites. Record
individual prerequisite states rather than treating this description as proof.

### Planned Steps

1. Sit in the low seat and insert the key using the selected local action. Key presence, OFF/ON
   position and sequence progress are distinct. Sitting or insertion alone must not raise the seat,
   run the engines or set startup success.
2. Try representative invalid attempts: wrong physical/control context, missing preparation or an
   incomplete apparatus/unit. Check rejection and consistent reasons without ignition/lift. Separate
   actual input/locality tests from any diagnostic negative-state setup. An open exterior hatch in
   the breathable hangar is not an ignition blocker when real prerequisites are satisfied.
3. Click OFF→ON in valid context. Observe accepted/in-progress state, occupied lift and actual
   main-service/engine/gravity transitions. Raised seating is a completed result, not a prerequisite
   for starting lift. The key click, sound, narration or animation start must not announce completion.
4. Request duplicate/conflicting toggles, key removal and seat exit during startup. Keep the active
   sequence without queued reversal, duplicate motion or early removal/exit. Preserve the same body
   in either view; actual lift endpoint restores exit and all declared startup results must complete
   before the per-run milestone is recorded.
5. After completed startup, leave/re-enter the seat and request normal ON→OFF locally. Observe
   state-consistent shutdown narration, occupied lowering while services/gravity support it, then
   gravity withdrawal and limited-service/Gilliam operation. Final shutdown completion, not merely
   a low-seat animation frame, permits key removal. No emergency incident or damage is added.
6. Verify registration, removed ribbons and prepared units persist through ordinary OFF unless
   separately manipulated. Melfina stays deployed/linked with the selected reduced-power presentation;
   current operation reflects OFF while the historical startup milestone remains achieved.
7. After completed shutdown, stow/relock one or more units through M03 and attempt restart. Current
   all-four validation must reject it with remaining-work feedback and no ignition/lift. Redeploy
   locally and retry successfully without renewed ribbons, revival or registration. Repeat actual
   seat/service transitions and restore normal occupant presentation.

**Expected outcome / evidence:** local key use coordinates real machinery/services in the accepted
order; incomplete/duplicate requests cannot fake success, and every restart uses current preparation.
Retain prerequisite/request/result traces plus observed seat, service, gravity and occupant states.
Key position or an isolated lift test alone is insufficient.

**Recovery:** isolate state-contract, key/seat adapter or service-presentation failures and return to
the owning S/I/M checkpoint. Preserve unrelated working mechanisms. Do not add hidden safety gates,
auto-prepare units, force a player into the seat or weaken completion to make ignition pass.

## VS1-R02

**Eight-condition startup, consistent reports and continued exploration**

**Owning checkpoint:** 7.2; full acceptance repeats in Phase 8.

**Starting state:** R01 integration available and the same supported ship/hangar. Complete the normal
route through real controls; compare early/partial engineering alternatives where relevant. The
existing baseline remains the requirement owner; the table below identifies evidence for its eight
conditions rather than defining a new readiness registry.

| Condition | Required observation / state evidence |
| --- | --- |
| Entry and route | Actual selected entry and usable bridge/engineering route, not a boarding marker or teleport. |
| Initial services | Completed laptop/bootstrap service result with usable feedback, not connection alone. |
| Navigation apparatus | Actual occupied deployed/available result, not case opening, revival or acknowledgement alone. |
| Engineering | Each of four independent full prepared endpoints, not one demonstrated unit or dialogue. |
| Seat/control cluster | Actual operating endpoint during startup; subsequent seat exit does not revoke the completed transition. |
| Ignition | Actual completed main-service/engine/gravity result rather than key press or motion start. |
| Consistent report | Gilliam, HUD/screens and queries read shared actual progress/results without independent success flags. |
| Supported endpoint | Ship stays in the hangar and continued exploration/exit/re-entry remains available; no launch or forced demo ending. |

### Planned Steps

1. Record the normal physical route and evidence for each condition. During intermediate stages,
   inspect queries and displays for missing/in-progress feedback. Do not wait until a congratulation
   screen to discover that an earlier condition was only assumed complete.
2. Compare Gilliam/status feedback before registration, during bootstrap/transfer, with partial
   engineering and after actual all-four preparation. Guidance must identify real remaining work,
   preserve early preparation and selected branches, and never operate equipment remotely.
3. Complete startup once, then compare the historical milestone and current operating report. Leave
   the seat and explore the required route in both views. No finish screen, permanent seat lock,
   forced camera change, launch timer or future feature is required to continue.
4. Complete startup with the hatch open; close/check/reopen it and compare departure warnings.
   Reopening invalidates the bounded seal result without clearing historical success or switching
   off engines/gravity. A cleared seal warning still does not certify or enable launch.
5. Exit/re-enter across ship gravity and hangar low gravity with the same body/equipment. Observe
   actual boundary movement/contact and continued route usability, using the selected tunable
   parameters; no global gravity toggle or player replacement may hide a boundary failure.
6. Perform normal OFF, restow/redeploy and restart. Compare all report surfaces with current state
   rather than the retained milestone. Reopen UI or return from menu/focus after progress completes;
   current values and notifications must remain readable without replaying completed story beats.

**Expected outcome / evidence:** all eight completion conditions are demonstrated, reports agree,
and post-success play remains available in the supported ship. Retain a criterion-to-evidence
mapping, actual state/query comparisons and observed route/gravity behavior. No numerical reactor
model, flight, crew AI or external controller is needed. Runtime status cannot certify untested fit.

**Recovery:** correct the smallest state/guidance/route or gravity adapter issue, preserving accepted
creative pacing and dialogue. Repeat dependent scenarios. Do not simplify away continued exploration,
reinterpret departure warnings as ignition gates or hide unavailable operation behind historical success.

## VS1-R03

**Fresh-run reset and repeatable integrated startup**

**Owning checkpoint:** 7.3; fresh-process packaged repeat remains Phase 8.3.

**Starting state:** integrated R01/R02 route with actual mechanisms, accepted initial/reset snapshot
and controlled access to the existing reset operation. No save/checkpoint-loading feature is required.

### Planned Steps

1. Begin an ordinary new run and record its initial snapshot/session identity. Progress through a
   representative incomplete sequence, including unfinished revival/bootstrap or occupied machinery
   motion. Reset using the existing lifecycle path, labelling reset as setup rather than player success.
2. Compare restored player/equipment, doors/lights, case/timer/occupant, laptop/registration, apparatus,
   seat/key, four units, services/gravity and per-run milestone with the declared baseline. Record
   pause/input state and retain configuration-setting deferrals; do not reset unrelated host settings.
3. Deliver or wait for old real-operation callbacks/timers after reset, using the bounded S03 method.
   Confirm they cannot change new-run positions, readiness, dialogue, notifications or temporary locks.
   Check same-session cancellation/replacement against actual adapters where applicable.
4. Complete a new dormant→ready run through physical actions and continue exploring. Then reset after
   that completed run and repeat the route again, checking the milestone is genuinely earned anew.
   Old prepared states, ribbon removal, registration or key transitions cannot carry over as shortcuts.
5. Within a run, compare normal OFF/ON with fresh reset: OFF retains accepted story/preparation and
   historical success; fresh reset restores the initial sequence. Include pause/menu/focus and view
   switching at representative active/blocked stages, with fresh input and no stale occupied locks.
6. Record repeat outcomes and any progressive accumulation of timers, duplicate event responses or
   retained state. Run existing focused S/I/M regressions for observed failures. Fresh-process and
   packaged repetitions remain explicit later proof, not assumptions based on this in-process check.

**Expected outcome / evidence:** both incomplete-run and completed-run resets restore the baseline,
invalidate old work and permit repeat physical completion. Retain before/after snapshots, session/
operation traces and observed repeated route/machinery results. Reset success does not establish save
persistence, cold-cache performance or a packaged runtime pass.

**Recovery:** preserve a reproducible failing sequence, identify its owning lifecycle/adapter and fix
only affected resources. Repeat the relevant reset and startup cases before accepting repeatability;
do not clear readiness alone while leaving mechanisms, occupant or temporary input locks stale.

## Completion Boundary

These procedures are accepted for planning on 2026-10-23, not gameplay delivery or test results. Phase 7 exit requires its
existing integrated-functionality review; Phase 8 owns full acceptance, host budgets, exact package
and handoff. No installation, modeling, engine execution, implementation or phase advancement occurs
in this documentation increment.
