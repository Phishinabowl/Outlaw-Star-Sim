# Unreal strategy

## Intended baseline — recorded 2026-10-07

**Unreal Engine 5.8** is the intended project baseline. The current local installation is **5.8.3**, verified from the engine's `Engine\Build\Build.version` (changelist 58210709, release-5.8 branch) and launcher inventory. The 5.8 family is selected; this does not freeze every future patch or establish a working project build. Revisit it only if later testing exposes a concrete compatibility or project requirement, recording the reason and obtaining agreement before migration.

The chosen Windows toolchain is **Visual Studio Community 2026, MSVC 14.50, Windows SDK 10.0.26100.0**. MSVC 14.50 is the preferred compiler target; installed 14.51 is not build-validated. Any missing component installation is deferred for discussion; no installer or settings change was run.

## Current Phase 1.1 inventory

The [dated readiness record](../implementation/phase-1-1-host-tooling-readiness.md) owns the latest
observed host/tool inventory and limitations. MSVC 14.50 is now installed alongside 14.51; actual
compiler product version 14.50.35739 clears the engine's banned range. The corrected Unreal Test Adapter
query confirms it is installed. Remaining .NET workloads/matching ATL are proposed setup additions;
no install or build was performed. This supersedes the earlier absence observations below.

The primary proof target is the inspected laptop, Win64 and keyboard/mouse, with no initial desktop validation
requirement and a native 1440p/60 FPS required target, with 120 FPS as a stretch goal pending measured
proof (revised in Phase 1.4). Lumen is the preferred lighting candidate for evaluation, not a measured
performance promise. Detailed budgets belong to Phase 1.4.

## Earlier read-only observations — before Phase 1.1

| Component | Observed on 2026-10-07 | Baseline / validation status |
|---|---|---|
| UE | 5.8.3, launcher binary distribution | Intended engine family 5.8; no editor launch or project compilation in this pass. |
| Visual Studio | Community 2026, product version 18.10.3, installation version 18.10.12224.181 | Chosen IDE family; installer reports complete/launchable. |
| MSVC | Earlier default file and tool directory reported 14.51.36231; x64 compiler/linker executables present | At that inspection, target 14.50 was absent; superseded by the Phase 1.1 inventory above. |
| Windows SDK | 10.0.26100.0 includes present; Windows header and x64 kernel32 library present | Intended SDK candidate; no complete link/package test yet. |
| .NET | System SDK 10.0.204; engine bundled `DotNet\10.0` directory present | Installation observations, not a separate project framework-version decision. |
| Workloads | Game development with C++ and Desktop development with C++ positively matched by `vswhere` | Core C++ workload presence verified; complete optional-component audit not claimed. |
| UE integration | `Component.Unreal.Ide` and `Component.Unreal.Debugger` positively matched | Available integration components; test-adapter/plugin functionality not verified. |

Checks used launcher JSON, build/config files, `vswhere`, directory inventory and executable/header/library existence. Registry enumeration was incomplete under the runtime's read permissions; the installed engine version comes from files and launcher metadata instead. No unrelated installed applications are recorded here. Local install paths are environment observations, not repository-wide required paths.

## Compatibility references and compiler distinction

[Epic's UE 5.8 Visual Studio setup guide](https://dev.epicgames.com/documentation/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine) lists VS 2026 18.0+ for general development, recommends MSVC 14.50 and Windows SDK 10.0.26100 or newer. [Microsoft's UE integration guide](https://learn.microsoft.com/en-us/visualstudio/gamedev/unreal/get-started/vs-tools-unreal-install) describes the C++ gaming workload and optional IDE/debugging/test integrations. Read 2026-10-07; later engine-specific guidance can change.

The installed UE 5.8.3 file `Engine\Config\Windows\Windows_SDK.json` prefers MSVC families 14.50.35717–14.50.99999 and 14.44.35207–14.44.99999, but bans actual 14.50 compiler versions through 14.50.35722. UBT distinguishes directory family from executable product version: the current folder 14.50.35717 contains compiler product version **14.50.35739**, above the ban. Installed 14.51 is outside the preferred families; absence from the banned ranges is not a successful build test. Let the engine's build tools and actual build results establish the later effective selection rather than silently accepting the IDE's default compiler.

The preferred compiler is now available side by side. The remaining installation discussion concerns the setup gaps in the dated readiness record. No downgrade, VS reinstall, plugin installation or global compiler configuration is selected by this document. Installed, preferred and build-validated remain separate statuses.

## Implementation direction

[Editor automation](editor-automation.md) records optional Blender/Unreal MCP evaluation, requirements
and fallbacks. Epic's experimental server/tool-provider descriptors are present in installed UE 5.8.3;
none has been enabled or tested. Evaluate after ordinary project proof, keeping packaged slice execution
independent of MCP. The official Blender candidate is selected for bounded evaluation under the
accepted local pilot contract; client/server compatibility and operational adoption remain unproven.

C++ foundations own inspectable, testable, diffable simulation/gameplay state. Blueprints handle editor-facing configuration, content hookup, animation/VFX/audio events and light composition. Avoid monolithic Blueprint state ownership. Blender remains the reconstruction direction; Git is established, and Phase 1.4 accepts Git LFS for project-owned binary assets, with tracking configuration and cost controls still to perform under later authorized scope.

[Shared external-control compatibility](external-control-automation.md) remains authoritative for future commands/results and locality. The [Phase 1.4 draft](../implementation/phase-1-4-architecture-asset-validation-draft.md) records accepted project/module layout and initial rendering candidates. Detailed implementation types, serialization, networking, renderer quality settings and integration compatibility remain unresolved. Reference-derived percentages do not select physics constants.

No Unreal project is created. [Phases 1.1–1.3](../implementation/vertical-slice-1-implementation-plan.md)
are complete for planning; Phase 1.4 architecture/asset/validation planning is in progress, with
remaining contracts pending. Phase 1.5 gate review remains unstarted. Phase 2 owns later authorized
tool/project proof. This supersedes the earlier
planning-gate deferral, not implementation/installation boundaries. Tool observations are dated;
this documentation sweep performs no fresh host inventory or build validation.
