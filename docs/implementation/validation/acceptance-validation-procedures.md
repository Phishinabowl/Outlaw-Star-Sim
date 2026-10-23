# Final Acceptance, Performance And Package Procedures — VS1-A01–A04

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Status | Accepted for planning/publication 2026-10-23; all scenarios not executed |
| Scope | Phase 8 complete slice acceptance, primary-host budgets, standalone reproduction and handoff |
| Authority | [Scenario register](../vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability), [slice acceptance](../../reconstruction/baseline-v1/vertical-slice-1.md#acceptance-review-for-the-later-implementation), [Phase 1.3 closeout](../phase-1-3-closeout-audit.md), [performance contract](../phase-1-4-architecture-asset-validation-draft.md#accepted-performance-measurement-contract--execution-pending) |
| Execution prerequisite | Phase 7 exit and explicit authorization for the applicable Phase 8 subphase |

These procedures refine the existing final scenarios without changing accepted gameplay, scope or
budgets. Phase 1.4 remains planning in progress; Phase 1.5 and implementation remain unstarted.
No build, benchmark, package, asset-policy configuration or publication is performed by this draft.

## Shared Setup And Evidence

- Apply the [foundation evidence rules](foundation-validation-procedures.md#shared-execution-and-evidence-rules).
  Codex performs authorized build, state, file and log analysis. The repository owner observes player
  experience, readability and physical fit unless another method is specifically authorized.
  Computer Use retains its separate permission requirement.
- Use the primary laptop, Win64 and keyboard/mouse. Record exact source revision and relevant local
  changes, build/package identity, host, settings, starting state, performer and actual outcomes.
  A planning approval, successful command or earlier editor observation is not a runtime pass.
- Reuse the existing T/G/S/I/M/R evidence and scenario IDs. Record which evidence applies to the
  candidate and repeat checks affected by later changes. Do not create a second readiness registry
  or require an exhaustive combination of every optional rendering technology and gameplay branch.
- Keep raw traces, logs and captures in ignored local working storage, with authored summaries and
  evidence pointers in the validation documentation. Source-media and derivative publication needs
  its existing explicit authorization; a successful package or LFS retrieval grants none.

## VS1-A01

**Complete slice acceptance and focused regression**

**Owning checkpoint:** 8.1; final standalone corroboration remains 8.3.

**Starting state:** Phase 7 integrated candidate, declared dormant initial state, accepted controls
and source/assumption records. Carry forward actual machinery and route evidence, not proxy-only fit.

### Planned Steps

1. Map each VS-01–VS-10 criterion to candidate-specific observations and relevant existing scenarios.
   Include all eight SHIP READY conditions. Identify gaps before marking the matrix complete;
   an unexecuted check cannot inherit a pass from its approved procedure.
2. Complete the ordinary physical opening route in both camera perspectives, preserving one player
   body and shared state. Observe the dark hangar reveal and scale, loaded approach/boarding,
   guide-lit route, case/laptop interactions, Gilliam registration, witnessed Melfina sequence,
   engineering preparation and occupied key/seat ignition. Do not use debug-assisted completion.
3. Verify natural 600 s resuscitation and its local shortcut as distinct paths. The shortcut changes
   remaining revival time only. Record any separate natural-duration run against the same candidate;
   it need not fit inside an approximately five-minute performance route.
4. Carry forward focused alternative-path proof: registration recovery/hold/resume, early and partial
   engineering preparation, all-four local preparation, graceful OFF, push-in/relock/redeploy and
   restart. Check guidance and missing-prerequisite feedback against actual equipment state.
   Preserve accepted dialogue and choreography rather than replacing them with generic success text.
5. Continue exploring after startup, leave the seat, exit/re-enter through the hatch and compare
   ship/hangar gravity behavior. Check hatch-open ignition and separate departure warnings.
   Exercise optional empty-trunk cleanup through the accepted route/staging location; it remains
   optional and cannot become a new startup gate or require an additional cargo room.
6. Run the owned automated state checks and targeted S/I/M/R regressions for invalid/local/duplicate
   actions, pause/focus/input release, obstructed machinery and incomplete/completed-run reset.
   Label diagnostic setup separately from physical positive completion. Check body, controls and
   bridge→engineering→bridge access before and after machinery movement in both views.
7. Reconcile applicable motion-clearance checks and future reservations with the supported hull pose.
   Record actual machinery motion separately from reservation-only future assemblies. Confirm that
   invented dimensions, connections, timelines and substitutions retain explicit E/F records and
   source-derived appearance retains evidence pointers. Deferred features cannot be needed to finish.

**Expected outcome / evidence:** the VS-01–VS-10 matrix contains observed results and criterion-level
evidence, including creative pacing, physical fit, consistent status and repeatable continued play.
Record failures, accepted limitations and unexecuted parts explicitly. An editor pass does not prove
package reproduction or measured performance; an exception cannot silently remove a baseline obligation.

**Recovery:** fix the smallest owning interaction, state, motion or layout issue and repeat affected
checks. Preserve the last runnable candidate and accepted creative intent. Do not mask failures with
teleports, forced completion, extra rooms, detailed art or deferred systems.

## VS1-A02

**Measured host performance, readability and responsiveness**

**Owning checkpoint:** 8.2; corroborate the exact final package in 8.3.

**Starting state:** working integrated route and a standalone packaged Development candidate, editor
closed. The [accepted performance contract](../phase-1-4-architecture-asset-validation-draft.md#accepted-performance-measurement-contract--execution-pending)
owns thresholds and measurement conditions. Resolve exact capture tools, route checkpoints and the
candidate quality profile before execution; no additional quality setting is approved by this procedure.

### Planned Steps

1. Record build/commit, engine, backend, complete rendering/quality settings, internal/output
   resolution, window mode, driver, active GPU, display refresh, AC power, power/fan profile and
   relevant background activity. Use native internal/output 2560 × 1440, dynamic resolution,
   upscaling and frame generation OFF. Native-resolution TSR is compatible with this baseline;
   gameplay depth of field and motion blur remain OFF for the baseline.
2. Capture startup/loading and shader/pipeline preparation duration separately from active play.
   Capture first-use reveal, lighting, screens, apparatus, engineering and ignition before repeated
   play warms those combinations. Record backend/driver/cache conditions: a fresh process is not
   proof of a cold cache. Any deliberate cache reset needs a reviewed project-scoped recipe;
   do not clear broad driver/editor caches or unrelated games' data.
3. Warm up through representative play for ten minutes, then capture three approximately five-minute
   routes under unchanged conditions. Identify segment boundaries for reveal, boarding, laptop/
   dialogue, apparatus, engineering, ignition, full-power exploration and OFF/restart. Record camera
   perspective and reproducible reset/replay setup; report the separate natural-revival run as well.
4. Measure uncapped with VSync OFF. For each representative segment in each warm run, assess average
   throughput ≥60 FPS, p95 frame time ≤16.67 ms and p99 ≤25 ms. Compute throughput from frames/elapsed
   time and percentiles from frame durations. Report 120 FPS stretch separately against average
   ≥120 FPS, p95 ≤8.33 ms and p99 ≤12.5 ms; missing stretch does not fail the required 60 FPS target.
   Do not use a whole-route average or ambiguous “1% low” to conceal a failing segment.
5. Record spike count, maximum duration and every active-play frame above 33.3 ms for first-use and
   warm captures. Diagnose recurring/reproducible hitches; correction or an explicit reviewed
   exception is required before a pass. Report isolated spikes too. Use targeted CPU/render/GPU
   diagnostics and traces to investigate, preserving a minimally instrumented baseline; overlapping
   CPU/GPU timings must not be summed as frame duration. Record RAM/VRAM use and repeated-loop growth.
6. Perform a separate 60 FPS-capped playability check, plus 120 FPS where stretch is supported,
   recording display/sync settings. Observe dark/guide/limited/full-power visibility, controls and
   small text, laptop/HUD/dialogue focus, feedback, camera clipping and machinery/body reach in both
   views. Pause/HOLD feedback must remain understandable beyond color alone. Record actual response
   problems without inventing an unapproved numerical interaction-latency target.
7. For any separately scoped quality comparison, verify essential visibility, interaction rules,
   controls, collision and machinery clearance remain intact. Keep Vulkan, alternative shadows/AA,
   DLSS/generated output and path-traced learning results separate from native acceptance. These
   experiments are not all required for slice closure.

**Expected outcome / evidence:** per-segment results for all three warm runs, first-use/startup
evidence, natural-revival evidence, capped playtest observations and the exact settings/host identity.
The required budget and readable, usable play must both hold. Startup duration and memory usage are
reported diagnostics; no numerical loading or RAM/VRAM limit has yet been selected. An enabled PSO
precaching setting alone does not establish hitch-free first use.

**Recovery:** isolate the bottleneck and propose bounded settings/content changes with affected
functional and performance rechecks. Do not silently lower resolution, disable the chosen lighting,
enable generated frames or relax thresholds. Record untested hosts and unsupported experiments.

## VS1-A03

**Exact standalone package reproduction**

**Owning checkpoint:** 8.3.

**Starting state:** 8.1/8.2 evidence and the existing T04 build/package recipe. Use the primary host;
no initial desktop/second-host validation, store installer or remote deployment is required.

### Planned Steps

1. Record exact input revision/local changes, effective engine/toolchain, build/cook/package commands,
   target/configuration, maps, asset dependencies and output location. Cooking prepares content for
   runtime; packaging assembles that content and executable. Review inputs and cooked dependencies
   for source media, unintended derivatives, test-only content and editor/MCP dependencies. Include
   only the intended runtime maps/content; required reusable assets cannot depend on excluded labs.
2. Produce an identified candidate with an artifact checksum or equivalent immutable output identity.
   First use Development for diagnostics, then repeat in the intended distribution configuration.
   Record configuration differences; Development results cannot automatically certify a changed
   distribution artifact. Preserve earlier runnable output instead of overwriting the only recovery copy.
3. Close the editor and run the candidate as a fresh process using the documented launch recipe.
   Complete the full physical dormant→ready route, required camera/interaction checks and continued
   exploration without debug assistance, MCP, an editor session or absolute source-folder dependencies.
   Do not remove installed development tools to simulate a clean host or claim clean-machine proof.
4. Exercise in-process reset using R03, then repeat startup from another fresh process. Corroborate
   applicable A01 alternative/negative cases and natural-revival evidence on the packaged candidate.
   Record startup, runtime and dependency failures; copying missing files from the source checkout
   during a run is a failed reproduction, not an accepted installation step.
5. Repeat relevant A02 measurements/readability checks for the exact intended distribution artifact
   and settings. Identify any reused evidence by matching artifact/configuration; rebuilds or changes
   require affected validation rather than assuming an earlier pass transfers. Keep fresh-process
   reproducibility distinct from cold-cache performance.
6. Retain output identity, launch instructions, logs, criterion mappings and explicit single-host
   limits. Freeze the reviewed candidate identity for handoff. Later content/configuration changes
   produce a new candidate and repeat affected proof; do not silently replace accepted output.

**Expected outcome / evidence:** the identified complete package reproduces outside the editor,
repeats startup/reset, preserves VS-08/09 and meets relevant performance/readability conditions.
The evidence states which package/configuration was actually tested; it makes no broader platform,
installer, clean-machine or public-distribution claim.

**Recovery:** preserve source and prior runnable output, fix the owning cook/runtime/reference issue,
rebuild and repeat affected acceptance. Do not silently change engine versions, ship reference media
to repair a dependency or require an editor/automation server for play.

## VS1-A04

**Documentation, artifact boundaries, publication and explicit closure**

**Owning checkpoint:** 8.4.

**Starting state:** A01–A03 evidence for the reviewed candidate, known limitations and the accepted
owned-asset/storage/recovery policy. Runtime acceptance and publication are separate recorded states.

### Planned Steps

1. Review the criterion/scenario evidence inventory and record passed, failed, blocked and unexecuted
   parts with revision/package/settings identities. Resolve unsupported completion claims before
   closure. Retain source provenance, E/F distinctions and meaningful approval history.
2. Update README, roadmap, implementation status and build/play guidance only to the extent supported
   by evidence. Document prerequisites, launch recipe, controls/camera modes, normal startup, natural
   revival/shortcut, pause/menu/focus behavior, continued play, graceful OFF/restart and fresh reset.
   Distinguish reset from a save/load feature and startup success from ending the demo or launch.
3. Reconcile owned editable assets, designated exports, authoring recipes and recovery evidence under
   the existing storage policy. Verify retrieval evidence applies to the reviewed asset set and that
   generated data, local sources and derivatives remain inside their approved boundaries. Binary
   retrieval does not establish permission to publish third-party reference material or fan assets.
4. Prepare the exact source/document/owned-artifact diff for review, with package delivery status
   stated separately. On explicit confirmation, follow the established focused Git workflow: inspect
   intended changes, run diff checks, stage only in-scope files, commit/push and verify status and
   HEAD/upstream parity. Preserve and report unrelated edits. Do not infer authorization for a public
   package release, new paid service or unrelated publication from documentation confirmation.
5. Record explicit maintainer acceptance of the first playable slice, remaining limits and actual
   publication outcome. A successful push cannot substitute for gameplay acceptance, and accepted
   gameplay does not imply a package was publicly released. Record the next proposed direction
   without automatically starting another phase, flight, detailed art or a new slice.

**Expected outcome / evidence:** current specifications and run instructions agree with the tested
candidate; artifact/source boundaries and recovery evidence are traceable; acceptance and publication
states are explicit. Any remaining baseline obligation needs resolution rather than silent omission.

**Recovery:** keep closure pending for missing required proof or unresolved artifact boundaries.
Prepare a focused documentation correction or requested reversion while preserving sources, earlier
evidence and unrelated work. Do not rewrite historical records to make the candidate appear complete.

## Completion Boundary

All four scenarios are accepted for planning on 2026-10-23 and remain unexecuted. This acceptance
approves the planning approach only. Phase 8 exit still requires actual observed proof and explicit slice
acceptance. Phase 1.4 closeout and the separate Phase 1.5 implementation gate are not completed by
this document; no installation, engine initialization, gameplay or asset work is authorized here.
