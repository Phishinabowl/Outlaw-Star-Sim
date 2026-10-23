# State And Lifecycle Validation Procedures — VS1-S01–S03

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Status | Accepted for planning/publication 2026-10-23; all scenarios not executed |
| Scope | Phase 4 authoritative-state fixture, command/results and reset/interruption boundaries |
| Authority | [Scenario register](../vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability), [Phase 1.3 closeout](../phase-1-3-closeout-audit.md), [Phase 1.4 lifecycle rules](../phase-1-4-architecture-asset-validation-draft.md#accepted-communication-and-lifecycle-rules) |
| Execution prerequisite | Phase 2 exit and explicit authorization for the applicable Phase 4 subphase |

These procedures test accepted behavior without selecting C++ classes, identifier formats, numerical
power/gravity models or an external transport. They create no code or fixtures. Phase 1.4 remains
planning in progress; Phase 1.5 and implementation remain unstarted.

## Shared Fixture And Evidence Rules

- Apply the [foundation evidence rules](foundation-validation-procedures.md#shared-execution-and-evidence-rules).
  Codex performs authorized narrow state checks and analyzes before/after records. The repository
  owner observes later world/UI behavior unless another method is specifically authorized; Computer
  Use still requires separate permission.
- Use one authoritative state implementation. A test fixture supplies explicit setup, requests and
  controlled completion/interruption events; it must not implement a second readiness calculator or
  expose setup shortcuts as player actions. Label fixture-injected states and completion events.
- Record session/operation identities, request context, prerequisite state, returned status/reason,
  authoritative before/after values and actual completion source. Identify missing adapters and
  whether results came from a controlled fixture or real mechanism.
- Target meaningful rules and lifecycle risks. No new general test framework, external client,
  multiplayer service, save/load or fault simulation is required. Do not add irrelevant combinations
  merely to enlarge coverage.
- Pure-state passes do not certify reach, collision, camera fit, motion endpoints, text-input routing
  or readable feedback. Repeat relevant checks through real controls in Phases 5–7 and integrated
  acceptance. The [spatial procedures](spatial-validation-procedures.md) own body/route/proxy proof.

## VS1-S01

**Initial domains and single authoritative ownership**

**Owning checkpoint:** 4.1; consumer/adapter review 4.4.

**Starting state:** authorized minimal state fixture at a fresh run. The initial/reset snapshot is
derived from the accepted Phase 1.3 contract, not inferred from default engine actors or UI widgets.

### Planned Steps

1. Record the initial snapshot for player/equipment/context, access/lighting, case/revival, laptop
   connection/bootstrap, registration/dialogue, four independent engineering units, apparatus,
   seat/key, main/limited services, gravity, pause reasons and per-run startup milestone. Reference
   existing requirements for expected values; record unresolved metrics instead of inventing them.
2. Check the logical owner of each domain against the accepted Phase 1.4 ownership table. Confirm
   that stable engineering identities remain distinct and guidance/presentation cannot independently
   mark units, navigation, ignition or overall startup complete.
3. Query state with final ship UI absent. Attach a thin test consumer, detach it, then query again.
   Consumer presence or camera perspective must not create a different authoritative state.
4. Through controlled fixture transitions, compare a successful startup, completed OFF and hatch
   reopening. Keep historical per-run startup success, current operation and represented departure
   status distinct. OFF/hatch reopening must not erase historical success; historical success must
   not substitute for current prerequisites. Label injected setup as fixture evidence only.
5. Check state distinctions important before main ignition: boot switch versus actual contact,
   personnel registration versus navigation availability, awake occupant versus completed apparatus,
   limited services versus main services/gravity. Do not convert qualitative supplies into a new
   numerical electrical simulation.

**Expected outcome / evidence:** the declared baseline and transitions are queryable from one set
of authoritative owners, independently of final presentation. Preserve the requirement-linked snapshot,
ownership review, query/transition records and explicit deferred fields. A widget or fixture success
flag is insufficient. Initial values not yet resolved must be reviewed before accepting that subcheck.

**Recovery:** revise the smallest ownership/state mismatch before downstream adapters depend on it.
Preserve the last working fixture case; do not add a parallel UI state model or broad subsystem tree
to hide inconsistent ownership. No final API or schema is approved solely by this procedure.

## VS1-S02

**Command validation, duplicates/conflicts and result lifecycle**

**Owning checkpoints:** 4.2/4.4; real-control repeats in Phases 5–7.

**Starting state:** S01 baseline and authorized shared command/query fixture. Record the target,
physical/control context and session/operation identity for each case. A simulated local context
tests validation logic; it does not prove the real adapter supplies trustworthy context.

### Planned Steps

1. Submit a valid local action and retain its result. For an asynchronous operation, distinguish
   acceptance/in-progress from completion: a request or animation start cannot set the completed
   endpoint, main-service state or startup milestone.
2. Hold back the fixture's completion event, inspect current state/progress, then supply the correct
   operation's completion. Confirm only its legitimate state transition occurs. Test a bounded
   failure/interruption result without falsely completing the operation; no damage model is implied.
3. Repeat the same request while active and submit an incompatible request to the same mechanism.
   Expect the existing operation/current result or clear rejection/in-progress feedback, with no
   duplicate timers, movement or queued reversal. Unrelated allowed operations need not be serialized.
4. Exercise representative rejected cases: missing registration for ship preparation, one of four
   engineering units incomplete at ignition, invalid local/control context, cylinder stow while ON,
   and key removal during ON/transition. Verify reasons and absence of prohibited changes. Retain
   allowed exploration/case/hatch access before registration and hatch-open ignition when its actual
   prerequisites are met; do not invent an airtightness ignition gate.
5. Compare equivalent requests from the fixture and a thin presentation/control adapter. They must
   use the same validation/state path. After state changes while a consumer is detached, reopen it
   and query current values; missed events cannot leave stale availability/readiness.
6. Repeat current-condition validation after historical startup success: with one unit legitimately
   stowed after completed OFF, a restart must report incomplete preparation rather than reuse the
   prior pass. Full local redeployment permits a new valid attempt without replaying registration.

**Expected outcome / evidence:** valid actions affect only intended state; rejected/conflicting
requests provide reasons without forbidden effects; asynchronous acceptance does not imply success.
Retain request/context/result traces and before/after state for each case, including unit identities
and session/operation correlation. Fixture results require later locality/input and visual repeats.

**Recovery:** fix shared validation or result propagation, not consumer-specific exception flags.
Revisit the behavior contract if an actual ambiguity is found; do not silently change mechanics or
implement a future remote/voice client to test an invalid-locality case.

## VS1-S03

**Interruption, pause, teardown and fresh-run reset**

**Owning checkpoints:** 4.3/4.4; actual-world repeat 7.3 under VS1-R03.

**Starting state:** S01/S02 fixture with controlled timers/progress and recorded initial snapshot.
Use the accepted [session/operation identity contract](../phase-1-4-architecture-asset-validation-draft.md#session-and-operation-identity--accepted-2026-10-11).
No real seat, apparatus rig or full laptop UI is required for this narrow fixture.

### Planned Steps

1. Interrupt representative active work according to its own contract: grip release retains partial
   handle/extension progress; disconnect cancels unfinished laptop work while completed results and
   independent revival persist. Re-grab/reconnect follows existing rules, not a universal reset.
2. Check clock/pause distinctions: laptop HOLD freezes only bootstrap progression; manual simulation
   pause stops simulation timers/motion, including revival; menu opening alone leaves the simulation
   running. Menu/focus input release must not latch grip/movement. Input routing and continuing player
   physics require later world proof, not merely successful timer assertions.
3. Exercise focus-loss auto-pause enabled/disabled and both manual-pause entry points. Focus return
   resumes only a pause caused by focus loss; it cannot clear manual pause. UI remains usable while
   simulation is paused. Exact key bindings and settings persistence remain deferred.
4. Reset during representative unfinished timer, bootstrap and motion/startup fixture cases, and after
   completed startup. Invalidate previous session work and restore the declared player/equipment,
   access, case, dialogue, units, apparatus, key/seats, services and per-run milestone baseline before
   accepting new actions. Compare each reset snapshot with S01; do not confuse reset with normal OFF.
5. Deliver delayed success/failure/progress callbacks from the previous session. Verify no new-run
   state, readiness, notifications or locks change. In the same session, cancel/replace an operation
   and deliver its old callback; matching session identity alone must not make it current.
6. Tear down the fixture with pending work, then recreate it and repeat a valid action. Old timers,
   callbacks, consumers and temporary locks must not influence the new instance. Repeating a reset
   must not multiply work or leave stale locks. No application save/reload feature is implied.

**Expected outcome / evidence:** action-specific partial/persistent state survives where required;
manual/focus/local pauses remain distinct; reset restores the baseline and rejects stale work.
Retain clock/progress traces, pause reasons, operation/session identities and baseline comparisons,
including negative assertions for old callbacks. Real machinery locks/obstructions, actual input
release, physics and returning UI remain pending until their owning integration checks run.

**Recovery:** preserve and replay the failing narrow case, correct lifecycle ownership and rerun
dependent cases before real machinery adapters. Do not mask late callbacks by marking work complete,
freezing only the player, suppressing all notifications or discarding legitimate partial progress.

## Completion Boundary

These procedures are accepted for planning on 2026-10-23, not executable tests or run results. Phase 4 exit requires its
existing evidence/acceptance review. Actual-world operation, feel, collision and final readiness remain
with VS1-I/M/R/A checks. No implementation, installation, editor launch or phase advancement occurs
in this documentation increment.
