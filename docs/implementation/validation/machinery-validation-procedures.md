# Machinery Validation Procedures — VS1-M01–M03

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Status | Accepted for planning/publication 2026-10-23; all scenarios not executed |
| Scope | Phase 6 actual occupied apparatus, seat/control lift and four engineering units; Phase 7 integration repeats |
| Authority | [Scenario register](../vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability), [Phase 1.3 closeout](../phase-1-3-closeout-audit.md), [detailed behavior record](../phase-1-3-action-readiness-draft.md) |
| Execution prerequisite | Phase 5 exit and authorization for the applicable Phase 6 subphase; Phase 7 cases require their later authorization |

These are procedures for real moving mechanisms and shared state, not new gameplay requirements or
modeling authorization. Phase 1.4 remains planning in progress; Phase 1.5 and implementation remain
unstarted. No mechanism, fixture or test is created or executed by this document.

## Shared Setup And Evidence

- Apply the [foundation evidence rules](foundation-validation-procedures.md#shared-execution-and-evidence-rules).
  Codex reviews authorized state/progress/asset evidence; the repository owner observes motion,
  reach, collision and readable feedback unless another method is explicitly authorized. Computer
  Use still needs its separate permission.
- Carry forward [spatial](spatial-validation-procedures.md), [state/lifecycle](state-lifecycle-validation-procedures.md)
  and [interaction](interaction-validation-procedures.md) checks. Record source references, E/F choices,
  dimensions, camera/body/occupant/equipment state, input/timing parameters and actual moving collision.
  Proxy fit or a successful request cannot replace actual occupied travel and completion evidence.
- Observe both camera views over the same player, including approach, intermediate motion, endpoints
  and departure/return paths. Retain existing MC-01–08 evidence ownership and explicit future-space
  limitations rather than claiming all reserved mechanisms operate.
- Label isolated diagnostic state/motion setup. It can prove a mechanism path, not normal player
  startup or shutdown. Integrated key, services/gravity, restart and milestone cases repeat under
  VS1-R01–R03; absent later systems remain pending rather than forcing early implementation.
- Preserve selected dialogue and source/adaptation boundaries. Animation timing, exact bindings,
  numeric gravity, appearance and unresolved source measurements remain tunable/reviewable within
  their existing scope; they are not silently settled by these procedures.

## VS1-M01

**Revival, witnessed transfer and occupied navigation apparatus**

**Owning checkpoints:** 6.1/6.4; service/readiness integration in Phase 7.

**Starting state:** functional case/laptop/registration path, selected cockpit staging and actual
apparatus with placeholder occupant. Main ignition/gravity remains OFF during normal preparation;
the transfer must account for that low-gravity premise. Full companion AI or fluid simulation is not required.

### Planned Steps

1. Open the case through the accepted local workflow. Begin resuscitation explicitly and test the
   natural 600 s simulation-time path separately from its local remaining-time shortcut. Neither
   opening nor the shortcut completes registration, apparatus deployment or engine preparation.
   Verify duplicate requests and simulation pause use the existing state contract.
2. Let revival finish while Gene is away or registration is suspended. Observe notification and an
   awake waiting occupant, not automatic transfer. Keep the deferred visible recognition/personnel
   beat distinct from Gene's completed registration and navigation availability.
3. Return locally with registration/personnel and awake conditions satisfied; acknowledge to begin
   the coordinated sequence. Gilliam opens the cap, Melfina enters and descends, the cap closes once
   she clears its aperture, then cylinder rise and lateral cover stages proceed. Retain source-linked
   visible stages and label joined closure/timing as E/F, not one continuously verified anime cycle.
4. Observe occupant support, cap hinge/sweep, below-floor travel, rise/covers and surrounding seat,
   controls, trunk/lid, doorway, canopy and rail reservations throughout motion. Navigation availability
   must follow actual required stage completion, not acknowledgement or an animation-start flag.
   Gene may look around without a forced camera lock/cut.
5. Block the opening/sweep with Gene before a stage and enter an unrelated obstruction during motion.
   Verify the affected stage waits/pauses, Gilliam requests clearance and visible state reports the
   block. Clearing permits continuation from preserved progress without crushing, teleporting,
   restarting revival or skipping endpoints. Intended occupant entry is not an unrelated obstruction.
6. Exercise menu/manual/focus pause and fresh reset during representative stages. Check continued
   automatic motion when simulation runs, true pause when requested, and no stale completion after
   reset. Repeat the route around the deployed apparatus in both views; record MC-01/02/04 evidence.
7. At later integrated OFF/restart, verify the apparatus remains deployed/linked, with subdued dimmer
   illumination/closed eyes/relaxed hands rather than a fully black pod or collapsed occupant.
   Restore the normal presentation as main services return without repeating revival/registration.
   Linkage and full operating availability remain distinct; this is not an emergency-cutoff simulation.

**Expected outcome / evidence:** natural/shortcut revival, local acknowledgement and actual occupied
stages remain distinct, with usable routes, correct obstruction recovery and authoritative progress.
Retain timer/context/state traces, source/stage references and observed intermediate/collision views.
Case completion or a deployed proxy alone is insufficient. Mark later OFF/restart portions pending
until their actual service integration exists.

**Recovery:** retain known-good source/rig states and revise one affected stage or local E allocation.
Repeat dependent MC/I/S cases; refer ordering or structural conflicts for review. Do not bypass fit
with invisible occupants, relaxed hull collision, forced camera cuts or new autonomous crew behavior.

## VS1-M02

**Occupied bridge seat/control lift and reversible transitions**

**Owning checkpoints:** 6.2/6.4 isolated mechanism; actual ignition/shutdown coordination in 7.1.

**Starting state:** selected low-seat access and occupied apparatus fit with the same physical Gene,
accounted-for laptop/cable and actual moving seat/control assembly. Record the source-shaped controls,
canopy/rail constraints and chosen collision/camera setup.

### Planned Steps

1. Enter the low seat through its local interaction. Sitting alone must not raise it. Verify the
   computer/cable is clear under the accepted equipment contract before protected movement.
2. Exercise lift travel with occupied player/cameras in the isolated mechanism fixture, labelling
   diagnostic triggers. Observe the full assembly and controls, headroom, apparatus, doorway and
   rail coexistence at intermediate points and endpoints; no player duplication or teleporting.
3. During lift/lowering, attempt seat exit and conflicting interaction/camera changes. Preserve
   occupied support and the temporary exit lock; changing perspective must not bypass it. Restore
   exit at the actual motion endpoint, without making seat occupancy a permanent post-startup rule.
4. Test simulation pause/menu/focus and reset during movement. Continuing simulation retains normal
   automatic motion/support; pause preserves progress. Reset releases stale operation/seat locks
   and old callbacks cannot reposition Gene or complete a new transition.
5. During later normal-route integration, insert the key locally and click OFF→ON from the low seat.
   Valid ignition initiates lift; the raised endpoint is a completion result, not an acceptance
   prerequisite. Duplicate/toggle requests during a transition report progress without queued reversal.
6. After completed startup, exit/re-enter the seat and continue play. Request normal ON→OFF while
   seated: lower with services/gravity retained, then withdraw ship gravity and settle to limited
   operation. Key removal waits for completed shutdown, not merely the low-seat endpoint. Test
   restart through the same assembly without replaying the introduction. Record integration pending
   during isolated Phase 6 proof rather than inventing an early player raise button.

**Expected outcome / evidence:** one supported body and valid controls/cameras coexist with actual
seat travel and nearby geometry. Retain occupancy/lock/operation evidence and observed path/endpoints,
including MC-01/04. Full ignition/shutdown timing and services require later R01 evidence; an isolated
lift pass cannot certify them or overall SHIP READY.

**Recovery:** revise affected lift/camera/attachment or local E geometry, preserving body scale and
working apparatus. Recheck dependent paths/MC evidence. Do not remove equipment from the scene,
allow clipping or change key/seat ordering merely to make the sweep pass.

## VS1-M03

**All-four engineering seals, release, extension and reverse operation**

**Owning checkpoints:** 6.3/6.4; actual OFF/restart repeats in 7.1/7.3.

**Starting state:** four distinct 2×2 units, actual controls/collision, chosen operator platform and
usable return route. Gene registration and applicable limited services permit preparation. Retain
the reviewed one-unit source anchor; repeating its manual procedure on the other three and reversible
demo operation are F adaptations. Project IDs do not establish exterior-engine mapping.

### Planned Steps

1. For each of the four units, approach locally and click to remove its ribbon seals in a quick action.
   Seal removal alone must not release/extend the unit or mark it prepared. Reject duplicate removal
   without resetting progress or spawning replacement ribbons.
2. Hold the interaction to grip/turn the handle, retaining partial turn on release and continuing on
   re-grip. Check the selected horizontal-to-vertical 90° clockwise gameplay presentation; keep the
   reported source rotation/quarter-turn reconciliation distinct from independently measured canon.
   Backward input cannot pull before the release rotation is complete.
3. Continue holding grip and move backward to pull the unit outward, with the same Gene moving along
   the operator path. Mouse hold alone must not automatically extend it. Release backward input while
   retaining grip to stop travel; release grip to disengage with partial extension retained. Re-engage
   locally and finish without snapping, redoing completed seals or automatic completion.
4. Check actual extension endpoints and per-unit readiness. One unit or partial travel cannot prepare
   the whole bank. Exercise duplicate/conflicting requests and invalid locality through the real
   controls; Gilliam/panels must report the same remaining work as shared state.
5. Observe upper/lower handle reach, grip/turn/pull body/feet/cameras, moving collision and accommodation
   with one and all-four units extended. Traverse the operator/return path in both views; record
   MC-03/04. No remote prepare-all shortcut, blanket stand-clear rule for the pulling operator or
   collision exemption can replace occupied travel. Exercise the accepted obstruction/interruption
   behavior; unresolved physical handling requires review, not a false endpoint or forced movement.
6. Compare normal Melfina-linked engine discovery with early preparation after Gene registration.
   Partial early work remains retained and receives remaining-work feedback; only actual all-four
   preparation earns the selected acknowledgement. Preserve the approved wording in its owning
   behavior record. Dialogue does not prepare units, complete navigation or bypass key ignition.
7. Once later integrated OFF/shutdown has completed, grip plus forward input pushes a unit inward on
   the same occupied path. Stop/release/re-grab to preserve partial travel. Fully insert before turning
   the handle back to locked. Do not replace seals. Reject stow/relock while main engines run or the
   required shutdown transition is incomplete. During Phase 6, label any isolated OFF setup as fixture
   evidence; repeat the real shutdown workflow at Phase 7.
8. Leaving a full prepared endpoint clears that unit's live preparation. Try a later restart with
   one or more units partially/stowed: reject it with consistent Gilliam/status feedback and no
   ignition/lift, even if the historical startup milestone remains true. Redeploy each affected unit
   locally without new ribbons or renewed registration/revival, then verify current all-four checks
   permit a valid attempt. Repeat occupied reverse/deployment access, not only state assertions.
9. Exercise menu/focus release and simulation pause during grip/turn/pull. Fresh input is required
   after return; no latched input continues manual extension. Reset restores initial seals/handles/
   extensions and clears old operation effects, whereas ordinary OFF preserves preparation and the
   historical milestone. Repeat affected S02/S03 cases through actual units.

**Expected outcome / evidence:** every unit supports the complete local seal→release→pull workflow
with distinct progress and actual full-endpoint preparation. Reverse push/relock and redeployment
respect completed shutdown and current readiness. Retain per-unit input/operation/angle/extension
records, observed operator paths/collision and normal/early/partial feedback. All-four success cannot
be inferred from one demonstrated unit. Later real OFF/restart proof remains explicitly pending until run.

**Recovery:** restore/revise the affected unit adapter/asset or local bank/platform proposal, then
repeat bank-wide reach/retreat and dependent I/S/R checks. Do not hide upper reach failures, shrink
Gene or grant through-wall control. Preserve unrelated working mechanisms; exterior-engine motion,
free dragging, damage/repair, replacement seals and a full reactor model remain out of scope.

## Completion Boundary

These procedures are accepted for planning on 2026-10-23, not rigged mechanisms or test results. Phase 6 acceptance retains its
existing occupied coexistence review and MC evidence; Phase 7 owns real key/service/readiness/restart
integration. No installation, modeling, engine launch, asset import, implementation or test execution
occurs in this increment. Confirmation of procedures does not advance execution phases.
