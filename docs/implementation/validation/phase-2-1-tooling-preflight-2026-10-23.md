# Phase 2.1 — Read-Only Tooling Preflight

| Field | Value |
| --- | --- |
| Observed | 2026-10-23 |
| Starting revision | `b68d283` on `main`, matching `origin/main` before result documentation |
| Authorization | [Accepted Phase 1.5 scope](../phase-1-5-gate-review.md#accepted-first-execution-scope--read-only-preflight); read-only inventory only |
| Performer | Codex through file/metadata reads and bounded component/version queries; Blender patch update reported by repository owner |
| Result | Authorized inventory complete; setup discrepancies identified; no compilation/editor/package proof |
| Publication | Confirmed 2026-10-23; observations remain the pre-installation baseline |
| Scenario | VS1-T01 availability/policy portion only; effective build selection remains unexecuted |

This record supersedes the [October 7 inventory](../phase-1-1-host-tooling-readiness.md) only for the
items freshly inspected below. Hardware, GPU driver, display, thermals and sustained performance were
not re-inventoried. No installer, configuration change, project/asset generation, build, editor or
Blender launch, MCP connection, LFS setup/upload or cache deletion occurred.

## Current Tools And Version Changes

| Item | Current evidence | Assessment / limit |
| --- | --- | --- |
| Unreal Engine | `Engine/Build/Build.version`: **5.8.4**, CL **58902052**, release-5.8 branch. `UnrealEditor.exe` product/file version independently includes CL 58902052. | Updated from October 7's 5.8.3 / CL 58210709. Same intended 5.8 family; recommended candidate for first proof, not build-validated. |
| Epic launcher record | UE entry in `LauncherInstalled.dat` still names **5.8.3 / CL 58210709** at the same engine path. | Metadata disagreement; installed version file and editor executable agree on the newer CL. No evidence here establishes a corrupt install or warrants reinstallation. |
| Visual Studio Community 2026 | `vswhere`: **18.11.0**, installation **18.11.12306.390**, complete/launchable, no reboot required. | Previously 18.10.3. Metadata only; IDE integration remains untested. |
| MSVC 14.50 | Family directory **14.50.35717**; `cl.exe` product **14.50.35739.0**, file **19.50.35739.0**. Linker, representative C++ header and x64 runtime library present. | Preferred compiler target remains available and above the installed engine's banned range. No compile/link proof. |
| MSVC 14.51 | Family **14.51.36231**, product **14.51.36260.0**; representative linker/header/runtime present. VS default version text still selects this family. | Retain side by side. A VS default does not establish UBT's effective choice; no default was changed. |
| Windows SDK | **10.0.26100.0**; Windows/UCRT headers, x64 kernel32/UCRT libraries and resource compiler present. VS SDK component query matches. | Matches intended SDK and current Epic recommended version range. Representative checks, not complete SDK/link validation. |
| .NET | System SDK directory **10.0.204**; engine-bundled SDK **10.0.203** under `DotNet/10.0/win-x64/sdk`. System .NET/ASP.NET **10.0.8**, Windows Desktop **10.0.8** and **8.0.32**, .NET runtime **8.0.32** directories present. | Installed SDK/runtime files do not imply corresponding VS workloads are installed. No .NET first-run/build command was invoked. |
| Blender | Executable product/file metadata **5.2**, file timestamp 2026-10-22 UTC; versioned resource directory timestamp 2026-10-23 UTC. Repository owner reports update **5.2.2 → 5.2.3**. | Record **5.2.3 as reported**, with family/file evidence corroborated. Exact patch/build is not independently established by the inspected executable metadata; no launch/export/MCP proof. |
| Git / LFS | `git --version`: **2.54.0.windows.1**; `git lfs version`: **3.7.1**. | Executables available; LFS tracking/retrieval policy remains unconfigured and untested. |
| Build/editor files | UnrealEditor, UBT DLL, Build.bat and RunUAT.bat present; VS IDE/MSBuild/C++ target files present. | Availability only. No project exists or was created for proof. |
| Unreal MCP files | ModelContextProtocol, ToolsetRegistry and AllToolsets descriptors present at the previously documented engine-relative paths. | File presence only; no enablement/discovery/client compatibility proof. |

## Component Queries

`vswhere -all -products '*' -requires <ID> -property installationPath` matched the intended VS
instance for installed entries below. Nonmatches are component-query observations, supplemented by
representative file checks where noted; this is not a full installer dependency audit.

| Component ID | Result |
| --- | --- |
| `Microsoft.VisualStudio.Workload.NativeDesktop` | Matched |
| `Microsoft.VisualStudio.Workload.NativeGame` | Matched |
| `Microsoft.VisualStudio.Workload.ManagedDesktop` | Not matched |
| `Microsoft.VisualStudio.Workload.NetCrossPlat` | Not matched |
| `Microsoft.VisualStudio.Component.VC.14.50.18.0.x86.x64` | Matched |
| `Microsoft.VisualStudio.Component.VC.14.50.18.0.ATL` | Not matched; `atlmfc/include/atlbase.h` and `atlmfc/lib/x64/atls.lib` also absent in the inspected 14.50 toolset |
| `Component.Unreal.Ide` | Matched |
| `Component.Unreal.Debugger` | Matched |
| `Microsoft.VisualStudio.Component.Unreal.TestAdapter` | Matched |
| `Microsoft.VisualStudio.Component.VC.ASAN` | Matched |
| `Microsoft.VisualStudio.Component.VC.DiagnosticTools` | Matched |
| `Microsoft.VisualStudio.Component.Windows11SDK.26100` | Matched |
| `Microsoft.VisualStudio.Component.Windows11SDK.22621` | Not matched; newer intended SDK is present |
| `Microsoft.Net.Component.4.6.2.TargetingPack` | Matched |
| `Microsoft.VisualStudio.Component.VC.Llvm.Clang` | Not matched |
| `Component.Unreal` | Not matched; this installer component's absence does not mean the separately installed engine is absent |

## Installed Engine Policy And Selection Limits

The inspected 5.8.4 `Engine/Config/Windows/Windows_SDK.json` prefers MSVC family ranges
`14.50.35717–14.50.99999` and `14.44.35207–14.44.99999`; it bans actual 14.50 compiler versions
through **14.50.35722**. `MicrosoftPlatformSDK.cs` reads the compiler's product version in
`IsValidToolChainDirMSVC`, ranks its directory family and tests the actual version against banned
ranges in `AddVisualCppToolChain`. Therefore the patched **14.50.35739** clears this static ban even
though its folder ends in 35717. That conclusion is not a successful build result.

The same configuration requires at least VS 2026 18.0 and suggests the matching 14.50 ATL component.
SDK 10.0.26100.0 is within the inspected supported bounds; do not infer that the JSON's older
`MainVersion` requires installing that exact SDK alongside the accepted newer SDK.

An empty `BuildConfiguration.xml` now exists at
`C:\Users\matt\AppData\Roaming\Unreal Engine\UnrealBuildTool\BuildConfiguration.xml`.
The inspected file contains only the Configuration root, with no compiler/SDK overrides. It was
absent at the earlier inventory; no creator or cause is established. Engine Saved, ordinary Documents
and OneDrive Documents candidates were not present. No file was created, changed or deleted here.
Future build logs must establish effective compiler/SDK selection; do not force global defaults now.

## Findings And Recommended Next Scope

1. **Use installed 5.8.4 as the candidate for first proof.** It remains within the accepted 5.8
   direction. Record the launcher discrepancy without editing its metadata; corroborate actual build
   identity at the later authorized build/editor checkpoint. No migration/reinstall is proposed.
2. **Review a narrowly scoped VS modification before initialization:** .NET desktop development,
   .NET MAUI and matching MSVC 14.50 ATL. The first two are listed in
   [Epic's current setup guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine);
   ATL is suggested by the installed engine's version-specific policy. These remain setup-alignment
   gaps, not observed compile failures. Inspect actual installer selections and dependency/storage
   impact before agreeing a mutation; do not install on the strength of this report.
3. **Retain existing MSVC 14.51, SDK and integrations.** No older SDK, second Unreal copy or global
   compiler/default change is justified by this inventory. Clang is not matched and appears in the
   engine's general suggestions, but the chosen compiler is MSVC; defer Clang installation unless an
   agreed task requires it. Microsoft documents the installed IDE/debugger/test integrations in its
   [Unreal tooling guide](https://learn.microsoft.com/en-us/visualstudio/gamedev/unreal/get-started/vs-tools-unreal-install).
   Their working integration still needs later editor/project proof.
4. **Keep Blender/MCP/export and runtime proof at their existing checkpoints.** The reported Blender
   patch does not require a new modeling or connector phase. Exact build identity can be recorded at
   its later authorized proof; being absent from PATH is not a missing Blender installation.

No core compiler/SDK availability blocker was found in the inspected representative files. This does
not establish full build readiness or waive the accepted vendor-alignment review. Whole Phase 2.1
preparation remains open for discrepancy disposition; 2.2 must not begin automatically.

## Reproduction Pointers And Evidence Limits

- Engine root: `D:\Epic Games\UE_5.8`; VS instance:
  `D:\Program Files\Microsoft Visual Studio\18\Community`; SDK root:
  `C:\Program Files (x86)\Windows Kits\10`; Blender executable:
  `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe`.
- Version reads: `Get-Content` for engine Build.version, Windows_SDK.json, VS default toolset text
  and the scoped UBT configuration; `Get-Item ... | Select-Object -ExpandProperty VersionInfo` for
  editor/compiler/Blender metadata. `vswhere -all -products '*' -format json` supplied VS identity.
- Component queries use the exact IDs above. `Test-Path` checks covered the listed tools and
  representative headers/libraries; directory enumeration supplied .NET SDK/runtime identities.
  Engine source inspection covered family ranking, banned checks and product-version detection.
- Blender executable SHA-256:
  `9D5DF7A9AC2A7C5085AA0669700021BFA5C5E92DE167A2510B0D0942C34DEAB0`.
  This identifies the inspected file without pretending its generic metadata independently proves 5.2.3.
- Registry lookup returned no Blender product entry through the inspected view; no absence claim is
  inferred. Sandboxed drive-capacity output was not usable, so no current free-space figure is claimed.
  Installer disk impact remains unknown until a separately authorized review.
- VS launchability is installer metadata, not an observed launch. Editor/Blender/CLI compile tests,
  project generation, renderer performance, cold-cache behavior, package independence and LFS retrieval
  remain unexecuted. This report contains no prewritten pass for those checks.

Vendor documentation was read on 2026-10-23. Local paths and package metadata describe this host only.
The authored result was confirmed for publication on 2026-10-23. Subsequent authorization covers
repository-owner installation of .NET Desktop, MAUI and matching MSVC 14.50 ATL with guided steps;
installation outcomes remain unverified. Codex performs no installer/configuration operations, and
project initialization remains unauthorized. This later scope does not alter the observations above.
