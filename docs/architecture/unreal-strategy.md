# Unreal strategy

## Intended baseline — recorded 2026-10-07

**Unreal Engine 5.8** is the intended project baseline, as requested by the user. The current local installation is **5.8.3**, verified from the engine's `Engine\Build\Build.version` (changelist 58210709, release-5.8 branch) and launcher inventory. The 5.8 family is selected; this does not freeze every future patch or establish a working project build. Revisit it only if later testing exposes a concrete compatibility or project requirement, recording the reason and obtaining agreement before migration.

The chosen Windows toolchain is **Visual Studio Community 2026, MSVC 14.50, Windows SDK 10.0.26100.0**. The user explicitly selected the preferred 14.50 compiler target instead of treating the installed 14.51 as validated. Any missing component installation is deferred for discussion; no installer or settings change was run.

## Local read-only observations

| Component | Observed on 2026-10-07 | Baseline / validation status |
|---|---|---|
| UE | 5.8.3, launcher binary distribution | Intended engine family 5.8; no editor launch or project compilation in this pass. |
| Visual Studio | Community 2026, product version 18.10.3, installation version 18.10.12224.181 | Chosen IDE family; installer reports complete/launchable. |
| MSVC | Default file and installed tool directory report 14.51.36231; x64 compiler/linker executables present | Not UE's preferred family; not claimed unsupported or validated. Target 14.50 is not installed in the inspected VS instance. |
| Windows SDK | 10.0.26100.0 includes present; Windows header and x64 kernel32 library present | Intended SDK candidate; no complete link/package test yet. |
| .NET | System SDK 10.0.204; engine bundled `DotNet\10.0` directory present | Installation observations, not a separate project framework-version decision. |
| Workloads | Game development with C++ and Desktop development with C++ positively matched by `vswhere` | Core C++ workload presence verified; complete optional-component audit not claimed. |
| UE integration | `Component.Unreal.Ide` and `Component.Unreal.Debugger` positively matched | Available integration components; test-adapter/plugin functionality not verified. |

Checks used launcher JSON, build/config files, `vswhere`, directory inventory and executable/header/library existence. Registry enumeration was incomplete under the runtime's read permissions; the installed engine version comes from files and launcher metadata instead. No unrelated installed applications are recorded here. Local install paths are environment observations, not repository-wide required paths.

## Compatibility references and compiler distinction

[Epic's UE 5.8 Visual Studio setup guide](https://dev.epicgames.com/documentation/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine) lists VS 2026 18.0+ for general development, recommends MSVC 14.50 and Windows SDK 10.0.26100 or newer. [Microsoft's UE integration guide](https://learn.microsoft.com/en-us/visualstudio/gamedev/unreal/get-started/vs-tools-unreal-install) describes the C++ gaming workload and optional IDE/debugging/test integrations. Read 2026-10-07; later engine-specific guidance can change.

The installed UE 5.8.3 file `Engine\Config\Windows\Windows_SDK.json` prefers MSVC families 14.50.35717–14.50.99999 and 14.44.35207–14.44.99999, but bans 14.50 builds through 14.50.35722. Therefore the intended **14.50 candidate must be at least 14.50.35723 within that preferred family**. Installed 14.51 is outside those preferred ranges; absence from the banned ranges is not a successful build test. Let the engine's build tools and actual build results establish the later effective selection rather than silently accepting the IDE's default compiler.

The immediate installation discussion is the side-by-side preferred compiler and any genuinely required missing components. No downgrade, VS reinstall, plugin installation or global compiler configuration is selected by this document. Installed, preferred and build-validated remain separate statuses.

## Implementation direction

C++ foundations own inspectable, testable, diffable simulation/gameplay state. Blueprints handle editor-facing configuration, content hookup, animation/VFX/audio events and light composition. Avoid monolithic Blueprint state ownership. Blender remains the reconstruction direction; Git is established, and a policy for later project-owned binary assets/Git LFS still needs discussion.

[Shared external-control compatibility](external-control-automation.md) remains authoritative for future commands/results and locality. Project/module layout, serialization, networking, renderer choices and integrations are undecided. Reference-derived percentages do not select physics constants.

No Unreal project is created. The formal implementation-planning gate is deferred at the user's request; toolchain documentation does not authorize project creation, compilation, modeling or gameplay work. A later approved implementation increment will establish the actual build/editor validation and may justify revisiting this baseline.
