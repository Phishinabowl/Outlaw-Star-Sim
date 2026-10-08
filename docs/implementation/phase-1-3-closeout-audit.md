# Phase 1.3 — Closeout Audit And Review Packet

2026-10-08. Status: **accepted planning closeout; Phase 1.3 complete**. The user accepted C13-01–05
and all seven supporting defaults. No implementation, modeling, installation or Phase 1.4 is
authorized by this acceptance. Runtime/fit checks remain unexecuted; E/F choices remain non-canonical.

Review update: the user accepted C13-01–05, including revised C13-04 reverse unit travel/relocking
only after completed OFF/shutdown, without replacement ribbons. Restart revalidates actual unit
preparation and reports incomplete units; prior success never bypasses current prerequisites.
The supporting defaults are also user-selected. This packet is the current consolidated behavior
contract; the linked discussion draft preserves history and detailed selected interaction rules.

The [discussion draft](phase-1-3-action-readiness-draft.md) preserves decisions and evidence.
Use this packet with the [slice contract](../reconstruction/baseline-v1/vertical-slice-1.md),
[operational vocabulary](../reconstruction/baseline-v1/operational-state-baseline.md) and
[spatial package](phase-1-2-closeout-proposal.md). No new source or runtime verification.

## Five Requirement Coverage Checks

| Phase 1.3 requirement | Covered | Accepted closure / later proof |
| --- | --- | --- |
| Initial services/player initialization | Gene, carried trunk/drawn laptop, breathable low-gravity hangar, guide lighting on entry, laptop bootstrap without ship gravity | Qualitative supply/boot defaults accepted; no circuit model. |
| Occupant/cap/seating/four-unit adaptation | Witnessed transfer/automatic apparatus, per-unit click seals/grip-turn/backward pull, ignition-triggered seat lift and reversible OFF, early engineering after registration | Cap closure and retained partial turn accepted; reverse push/relock after OFF. Actual reach/fit later. |
| Actions/locality/results/dependencies | Local controls, progress versus completion, cancellation/duplicates, resumable registration, key transition exclusion | Post-disconnect and deferred visible-Melfina beat accepted. Exact APIs/bindings later. |
| Eight readiness conditions/guidance | Actual ignition/lift/gravity completion, ongoing exploration, milestone versus current operation/departure warning | Automatic bounded seal check accepted; no launch implementation. |
| Safe interruption/collision | Partial-pull retention, apparatus obstruction, seat lock, ladder endpoints, manual/menu/focus pause and reset | Mid-turn/input-release/resumption defaults accepted; physical checks later. |

The five planning items are complete. Exact dialogue polish, animation and measured geometry remain
later work; this is neither a runnable build nor a fit pass.

## Reconciled Normal Route And Alternatives

1. Facility door/lights → low-gravity jump/handhold → independently open/enter ship hatch → loaded
   internal ladder ascent with directional control and temporary hand-item stow.
2. Stage case → Hilda's laptop note/local connection/code → open case → explicit revival start.
   Natural 600 s or local shortcut; neither completes other ship work.
3. Ship laptop connection → clicked scripted override → activation/countdown with HOLD toggle →
   Gilliam/limited services. Registration proceeds through pod dialogue/photo beats; recovery branch
   fails and rejoins, or hold-off preserves the conversation while exploration continues.
4. Awake Melfina waits for local acknowledgement after registration → Gilliam opens cap → she
   enters → automatic apparatus stages/link → engine-preparation check.
5. Normal guidance directs engineering after her report. Optional early engineering after registration
   remains available; all-four/partial preparation gets the appropriate acknowledgement/remaining work.
6. Each required unit: click seals, mouse-hold grip/turn, continued grip plus backward movement pulls.
   Pause/let-go retains extension; re-grab to finish. Only full endpoints count.
7. Sit low → insert key/click ON → occupied lift and actual main-service/gravity completion →
   startup milestone. Hatch status does not block ignition; success does not end play.
8. Continue exploring/exiting/re-entering. OFF lowers seat with gravity/services retained, then
   withdraws gravity and settles to Gilliam/limited lighting. Melfina stays deployed/linked with
   reduced-power presentation. Preparation/registration/per-run success persist; key removal waits
   for completed shutdown. Restart does not replay the introduction.

After completed OFF, grip/forward can stow units and the inserted handle can relock without new
ribbons. Leaving a prepared endpoint clears its live prepared status; every restart rechecks all four.
Redeploy locally before a valid restart, while retaining the historical successful-startup milestone.

Optional cleanup: after Melfina leaves, close/back-carry the empty trunk and place it at a marked
hangar spot. Test the loaded return route; no deletion or new cargo room. Normal guidance is not
a chronology lock. No promise that other tasks fill all 600 s, and no new chores to do so.

## Five Accepted Behavior Choices

| ID | Gap | Accepted rule | Boundary |
| --- | --- | --- | --- |
| C13-01 | Laptop after disconnect | Explicit Disconnect leaves focused screen open, Notes available/device controls disabled. Walking beyond cable reach closes focused view but keeps laptop drawn. Stow performs agreed disconnect/close/holster. | Three different intentions; no surprise unequip or stale target connection. |
| C13-02 | Registration if trunk still closed | Complete Gene's registration independently; defer Melfina's local photo/recognition beat until visible in open case. Run once whether revival running/complete. Transfer waits for her personnel beat plus normal awake/local conditions. | No scanning an occluded occupant or forced case-first order; Gene can still prepare engineering early after registration. |
| C13-03 | Cap closure across unseen transition | Once Melfina descends clear of aperture, close cap before cylinder rise; obstructed sweep waits/resumes under existing no-damage rule. | Concrete F choreography, not a verified uninterrupted anime cycle. |
| C13-04 | Releasing grip and reverse engineering operation | User-selected: retain partial turn/re-grip; grip + backward pulls, grip + forward pushes on same path; fully inserted handle turns back to locked. Stow/relock only after main engines OFF/shutdown complete; no replacement ribbons. | Reverse operator-path/handle fit still required. Revalidate all units on every startup; partial/stowed units fail preparation with Gilliam/status feedback. Historical success persists. |
| C13-05 | Bounded seal/pressure check | Actual exterior-hatch closure plus limited services starts a short indicated check automatically. Represent that seal and acceptable breathable cabin condition; other out-of-slice exterior openings stay static/assumed closed. Reopen invalidates affected departure result. | No ignition gate, extra pressure task, universal hatch merger or full leak/room network. Clearing this check is not complete launch certification. |

C13-01–05 are user-selected, including the revised reverse-operation rule. These close
bounded behavior gaps. C13-02 is a deferred photo/dialogue beat, not autonomous crew behavior.

## Seven Accepted Supporting Defaults

1. Initial boot switch ON, with actual attachment determined by suitable foot contact.
2. Qualitative independent operating supplies for boots/laptop/case and facility controls; guide/limited
   ship services support agreed pre-main actions. E/F continuity, not verified wiring, numeric power,
   charging task or additional generator simulation.
3. Contextual clicks on ordinary panels, with specific holds/climb/pull/key controls as selected.
   Exact bindings/ranges remain 1.4/tuning; typing focus suppresses gameplay hotkeys.
4. Menu/focus entry releases active movement/grip input; require fresh input on return. If sim keeps
   running, automatic motion and existing physics continue without a secret player-only freeze or
   invulnerability. Menu input cannot move Gene; seat/ladder attachment still supports him.
5. Suspended dialogue resumes the saved prompt/line from the start of that incomplete line; preserve
   completed branches/results without repeated recovery/photo/registration completion.
6. Notifications remain available/readable after menu or focus return so completed events are not
   silently missed. Exact display/pacing remains tunable.
7. Fresh reset invalidates callbacks/timers, restores initial player/equipment/access/case/dialogue/
   unit/apparatus/key/services and clears the per-run milestone. ON/OFF remains different from reset;
   no save/load. Exact ownership/APIs belong to 1.4/4.3.

## Three Distinct Results

| Result | Meaning | After success |
| --- | --- | --- |
| Per-run startup milestone | All eight completion conditions actually achieved once | Retained through OFF/seat exit/hatch reopening; cleared on fresh run/reset. |
| Current operational state | Actual services, machinery, navigation capability, gravity and transition progress | Updates on OFF/ON; cannot say engines running merely because milestone achieved. |
| Represented departure status | Bounded hatch-seal/cabin-pressure warning plus no-launch slice limitation | Reopening invalidates check without shutting down engines/gravity; clearing warning is not full future flight certification. |

Physical key use and protected motion require seated Gene, not permanent seat occupancy after success.
Raised seat completes after key initiation, never a circular ignition prerequisite. Laptop countdown,
revival completion, Melfina's attempted activation, Easter egg and narration cannot replace actual results.

## Deferrals And Validation Ownership

Defer bindings, click/hold durations, cable/climb/jump/gravity parameters, field blend/boundary,
colors/fonts/layout, exact animation/audio, pose/brightness, most dialogue polish and stage durations.
Preserve exact user-selected dub lines and starting joke wording. Source alignment, original audio/
Japanese, quarter-turn reconciliation, missing hull sections and production provenance remain parallel
research. They may invalidate an affected E/F choice but do not require a new general research phase.

Roof/cavity, loaded return route, four-unit retreat/upper reach and Gilliam housing still need actual
Phase 3/6 fit. Startup/shutdown report scripts need state-consistent drafting before implementation;
no exact reversed canonical shutdown claimed. Emergency cutoff, full crew, flight, damage/repair,
general inventory, free manipulation, adapters/LLM remain deferred. Accepted bounded additions remain
in scope: animated pod, laptop screens, registration branch, reversible operation, pause and cleanup.

VS-D04–06 now have accepted bounded F contracts: initialization/services, occupant/all-four handling,
and shared action/readiness/locality results. Runtime API, asset and measurement choices remain later.

| Validation scope | Existing owners / scenarios |
| --- | --- |
| Loaded entry/ladder, boots/gravity, equipment and optional return cleanup | 3.1–3.4, 5.2/5.4, 8.1/8.2; VS1-G01–G03/I01–I03, MC-01–08 where applicable |
| Laptop/code/connection/HOLD, direct/recovery/held registration and notifications | 4.1–4.3, 5.1/5.3/5.4; VS1-S01–S03/I01/I03; actual presentation repeat 8.1/8.2 |
| Natural/shortcut revival, witnessed transfer, cap closure and obstruction | 6.1/6.4; VS1-M01, MC-01/02/04; no false completion or automatic unseen transfer |
| Normal/early/partial engineering and reverse stow/redeploy | 6.3/6.4, restart 7.1; VS1-M03/S02/R01, MC-03/04; all-four actual states govern reports |
| Key ON/OFF, occupied lift/lowering, gravity and current/milestone/departure status | 6.2, 7.1/7.2; VS1-M02/R01/R02, MC-01/04; no emergency cutoff or launch required |
| Menu/hotkey/focus pause, interruption, fresh reset and post-success exploration | 4.3, 7.3, 8.1/8.2; VS1-S03/R03/A01 and VS-07–09; no stale callbacks/locks/results |

All scenarios are planned, not executed tests or delivered gameplay. Phase 1.4 still requires
explicit authorization; the Phase 1 exit precedes project creation/modeling/installations.
Publication remains separately confirmed by the user.
