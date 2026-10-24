# Foundation Validation Procedures — VS1-T01–T04

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Status | Accepted for planning/publication 2026-10-23; not executed; no validation results claimed |
| Scope | Phase 2 toolchain, repository boundary, C++ build/editor and neutral standalone package |
| Authority | [Implementation plan and scenario register](../vertical-slice-1-implementation-plan.md#validation-register-and-requirement-traceability) |
| Execution prerequisite | Phase 1 exit and explicit authorization for the applicable Phase 2 subphase |

These procedures refine existing scenario IDs. They do not create another test framework or authorize
installations, LFS configuration, project creation, engine execution or publication. Phase 1.4 remains
planning in progress at that historical acceptance checkpoint, and all four scenarios were then
**not executed**. This procedure document itself verifies no host/tool availability.
Subsequent execution evidence is maintained separately in the
[2.1 inventory](../phase-2-1-closeout.md), [2.3 build/editor closeout](../phase-2-3-closeout.md) and
[2.4 package closeout](../phase-2-4-closeout.md). Current Phase 2.4 evidence includes
successful first/repeat standalone runtime checks; phase acceptance remains distinct from test results.

## Shared Execution And Evidence Rules

- Codex performs authorized file/configuration checks, builds and log analysis through available tools.
  The repository owner performs editor/package observations and basic input checks unless another
  method is explicitly authorized. Computer Use needs its own specific permission.
- Use the primary laptop, Win64 and keyboard/mouse. The dated
  [Phase 1.1 inventory](../phase-1-1-host-tooling-readiness.md) is previous evidence, not a fresh inventory.
  [Unreal strategy](../../architecture/unreal-strategy.md) owns intended toolchain choices.
- Record scenario ID, date, performer/reviewer, checkout revision plus relevant uncommitted changes,
  host/tool identities, starting state, exact commands/settings, expected/actual outcomes and evidence
  locations. Mark each subcheck passed, failed, blocked or not executed, explaining partial results.
  **Procedure accepted** and **scenario passed** are separate statuses.
- Raw logs/captures remain in ignored local working storage; authored result summaries belong in
  `docs/implementation/validation/`. Media publication retains its existing authorization boundary.
  Do not create placeholder pass records before execution.
- Preserve existing accepted checkpoints or local copies before mutations. Recover only resources
  changed within the authorized scope; preserve unrelated edits/tools. Checkpoint publication still
  follows explicit Git confirmation.
- Resolve exact executable paths, generated destinations, neutral-map identity and basic input
  observation before the corresponding run; retain them in its recipe. Do not add game systems to
  satisfy a foundation check.

## VS1-T01

**Toolchain availability and effective selection**

**Owning checkpoints:** 2.1 inventory; 2.3 and package-build corroboration of effective selection.

**Prerequisites / starting state:** approved Phase 2.1 scope and primary laptop. No project is needed
for inventory. Any component installation requires its separately approved scope; this procedure does
not select extra workloads or updates.

### Planned Steps

1. Record the actual engine installation and `Engine/Build/Build.version` identity. Compare with the
   intended UE 5.8 family and previously observed 5.8.3. Record discrepancies before assuming a
   changed installation is approved for the project.
2. Inventory the intended Visual Studio instance, side-by-side toolsets, Windows SDK and relevant
   .NET/runtime availability using read-only metadata/component queries. Resolve current paths;
   earlier host-specific paths are observations rather than required locations.
3. Check the x64 compiler/linker and representative SDK headers/libraries/tools. Record MSVC directory
   family and executable product version separately, comparing them with the installed engine's
   preferred/banned policy. The dated 14.50 folder/product-version distinction must not be lost.
4. Compare current components with the dated proposed setup gaps. Distinguish required blockers,
   guidance-alignment gaps and optional integrations. A failed metadata query is unavailable evidence,
   not proof a component is absent.
5. Record readiness to attempt the bounded build, or the exact blocker/decision needed. Do not launch
   installers or change global compiler settings as an inspection side effect.
6. At T03, attach real build evidence identifying effective compiler product version, toolset path,
   SDK and engine .NET/runtime selection. Confirm intended MSVC 14.50 and SDK 10.0.26100.0; installed
   or default 14.51 is not an unexplained substitute. Corroborate packaging selection when it builds.

### Expected Outcomes And Evidence

- Inventory establishes actual availability and policy compatibility, or identifies a precise blocker.
  The 2.1 result leaves effective-selection corroboration pending until a real build.
- Complete T01 success requires that later corroboration; installer/component presence alone is not
  compilation proof.
- Retain dated inventory/query outputs, engine version/policy references, discrepancy dispositions
  and build-log evidence of effective selection.

**Failure / recovery:** retain installations. Diagnose missing files, unsupported versions or selection
problems and propose the smallest scoped correction. Do not silently switch compiler/engine, reinstall
Visual Studio or select extra components. Repeat affected checks after an authorized correction.

## VS1-T02

**Project, asset storage and generated/source boundaries**

**Owning checkpoints:** 2.2 boundary/publication/file-recovery evidence; retrieved-map editor
corroboration in 2.3. The later Blender handoff fixture belongs to 3.1 before repeated geometry production.
Completion of 2.2 does not require executing those later checkpoints or declaring the whole scenario passed.

**Prerequisites / starting state:** 2.1 readiness sufficient for the authorized skeleton scope and the
accepted [storage/recovery contract](../phase-1-4-architecture-asset-validation-draft.md#asset-storage-and-recovery-contract--accepted-2026-10-23).
The skeleton is Games Blank C++ at the accepted OutlawStarSim location. Ship/player implementation
and Blender production assets are not prerequisites.

### Planned Steps

1. Record pre-change repository status and skeleton creation/configuration recipe. Audit descriptor,
   module/source, configuration and neutral-map locations against the accepted layout.
2. Audit repository-local `.gitattributes` rules created during authorized 2.2 work. Designated
   Blender/FBX and owned Unreal binary paths use LFS; source/configuration/recipes/docs use ordinary
   Git. Check effective attributes for actual owned binaries and representative planned paths.
3. Check effective ignore rules for caches, Blender backups, generated outputs and protected reference
   locations. Inspect tracked files and the proposed publication diff: ignoring does not untrack
   existing files. Do not add protected media to test exclusion.
4. Confirm the neutral map and required owned dependencies are in the intended versioned set. Check
   real working binary contents and LFS pointer representation in Git where applicable. Record
   source/export/import recipe links for handoff assets that actually exist.
5. After separately authorized binary publication, retrieve its recorded revision in an approved
   separate checkout with LFS payloads. Verify actual content, not unresolved pointer text or assets
   copied from the original working folder.
6. Observe the retrieved neutral Unreal asset opening through the designated editor check. Coordinate
   with T03, avoiding an earlier unapproved launch. Blender open/export/reimport proof remains with
   the later existing handoff fixture.

### Expected Outcomes And Evidence

- Versioned content matches policy; source media, caches, temporary outputs and packaged builds are
  absent from tracked/staged changes. Effective attributes/ignores support those boundaries.
- First owned binaries are retrievable from the published revision and the test asset opens.
  Retain layout audit, attribute/ignore results, tracked/diff review, LFS identities, retrieval output
  and the editor-observation reference.
- Publication/retrieval not yet performed remains pending; it is not complete T02 success. Absent
  future Blender assets are not a foundation failure or permission to create them. This scenario
  does not certify their dimensions, pivots, collision or handoff behavior.

**Failure / recovery:** stop affected asset publication/production; preserve local originals and
unrelated edits. Correct scoped tracking/layout issues. Accidental committed media/binaries require a
reviewed remedy, not automatic history rewriting. Restore affected known-good asset/recipe sets under
the accepted recovery contract, preserving failed reimport evidence locally.

## VS1-T03

**Reproducible C++ build and observed editor startup**

**Owning checkpoint:** 2.3.

**Prerequisites / starting state:** 2.2 skeleton/boundary audit and T01 readiness available. T02 remote
retrieval may await authorized publication and can be corroborated here. Begin with the editor closed,
using the selected engine and neutral map. The accepted target is the project's **Win64 Development
Editor** target, distinct from the packaged game's target.

### Planned Steps

1. Record checkout/configuration and project target/module identity. Resolve the installed engine's
   ordinary build entry point and record exact command/log destination. Do not depend on Live Coding
   or a running editor.
2. Compile/link project C++ and retain exit status and relevant complete build log. Establish actual
   compilation at least once; an up-to-date result alone is not initial compile proof. A rebuild is
   scoped to the owned project target; no engine rebuild or broad cache deletion is implied.
3. Extract effective compiler/toolset, SDK and engine .NET/runtime evidence. Resolve T01 selection
   discrepancies before accepting the build as proof of the intended baseline.
4. Open the intended project/neutral map. Observe correct map load and the minimal fixture's documented
   basic input response. Record performer/method. Do not require Gene, two-view movement, machinery
   or additional gameplay to complete this observation.
5. Review module-load, asset/dependency and initialization logs. Classify relevant warnings and their
   dispositions rather than demanding silence or globally suppressing warnings.
6. Close the editor; repeat the ordinary build from a fresh tool/process session and reopen the
   map. Record the repeat result, which may be up to date after the initial compilation. An OS
   reboot is not required by this procedure.

### Expected Outcomes And Evidence

- Compilation/linking succeeds with the intended toolchain; module/map load and basic input are
  actually observed, including reopening.
- Retain exact commands/configuration, exit/results, selection evidence, startup logs and first/repeat
  observation records. Binaries existing, a successful tool response or Live Coding alone is not proof.
- Missing observations remain pending even when compilation passes.

**Failure / recovery:** preserve logs; isolate toolchain, skeleton, module or asset cause. Return to
2.1/2.2 where appropriate and restore only affected owned changes. Gameplay additions, optional MCP
enablement, engine migration and wider refactors are not default repairs.

## VS1-T04

**Early standalone package smoke test**

**Owning checkpoint:** 2.4.

**Prerequisites / starting state:** T03 proof complete; T02 retrieval completed before Phase 2 exit.
Specify the **Win64 Development** game package, neutral map/default startup selection, prerequisite
policy and owned ignored output destination in the run recipe. Development game and Development
Editor are different targets. Missing runtime prerequisites require review, not automatic installation.

### Planned Steps

1. Build/cook/stage/package the neutral map and required content with a recorded recipe. Capture
   effective configuration/toolchain, exit status, warnings/errors and output identity. Confirm an
   actual packaged executable/content set, not editor Play-In-Editor or an uncooked launch shortcut.
2. Audit staged content/dependencies: no source episodes/settei, extracted frames, absolute reference
   paths or required editor/debug/MCP services. The neutral map is intentional fixture content;
   its inclusion does not permit shipping all development fixtures in the slice.
3. Close the project editor and run from the separate generated output directory without MCP or a
   cook server supplying the application. Record optional pilot exclusion/deferral. Do not stop
   unrelated shared services to perform the test.
4. Observe correct startup/map, the documented minimal keyboard/mouse response and ordinary exit.
   Inspect relevant missing-content/module/crash messages. Relaunch the executable to verify repeat
   startup without editor preparation; retain runtime evidence and performer/method.
5. Record revision/output identity and reviewed results. Confirm package/log outputs remain outside
   source publication. Preserve failed-run evidence before another packaging attempt overwrites it.

### Expected Outcomes And Evidence

- Packaging succeeds; the actual package loads the intended fixture, responds to documented input
  and exits/relaunches without editor/MCP/cook-server assistance.
- Retain packaging command/settings/logs, staged-content/dependency review, artifact identity,
  available runtime logs and explicit first/repeat observations.
- Installed development tools remain on the host. Dependency review and separate-directory execution
  provide bounded primary-host proof, not clean-PC portability. No uninstall or second-host test is
  required; record runtime prerequisites and untested dependency limits.
- This is not 1440p performance acceptance, full-slice packaging, player fit or gameplay validation.
  Those remain separate later scenarios.

**Failure / recovery:** preserve cook/package/runtime evidence; return to 2.2/2.3 for the identified
content/build/dependency issue. Do not make launch succeed by starting editor/MCP, including source
media or installing unapproved components. Repeat affected checks after bounded correction.

## Review And Completion Boundary

The four procedures and target/configuration choices are accepted for planning on 2026-10-23.
Resolve run-specific paths, commands and fixture observations within the later authorized scope.
Later result records
link existing IDs and distinguish inventory, effective build selection, retrieval, observations and
outstanding checks. Phase 2 exit still requires T01–T04 evidence and maintainer acceptance under the
implementation plan. Procedure acceptance does not close Phase 1.4, start Phase 1.5 or authorize Phase 2.

Technical references: [Epic build configurations](https://dev.epicgames.com/documentation/unreal-engine/build-configurations-reference-for-unreal-engine),
[build/cook/stage/package operations](https://dev.epicgames.com/documentation/unreal-engine/build-operations-cooking-packaging-deploying-and-running-projects-in-unreal-engine)
and [packaging overview](https://dev.epicgames.com/documentation/unreal-engine/packaging-your-project).
These explain engine concepts, not proven compatibility or success on this host.
