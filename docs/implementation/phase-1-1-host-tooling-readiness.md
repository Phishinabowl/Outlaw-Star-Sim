# Phase 1.1 — Host And Tooling Readiness

| Field | Value |
| --- | --- |
| Inventory / decisions | 2026-10-07 |
| Scope | Read-only Phase 1.1 inventory and agreed host/target decisions |
| Status | Inventory and scope decisions complete; confirmed for publication 2026-10-07 |
| Execution boundary | No installation, editor launch, build, project creation or later subphase |

This is the dated evidence record for [implementation Phase 1.1](vertical-slice-1-implementation-plan.md#phase-11-scope-host-and-tooling-readiness-inventory).
[Unreal strategy](../architecture/unreal-strategy.md) owns the intended engine/toolchain direction;
this record supersedes its earlier inventory where observations changed. Installed and build-validated
remain distinct. Repository status was clean before this documentation update, with HEAD matching
the locally recorded upstream; no remote refresh was performed during the read-only inventory.

## Agreed Proof Scope

- Primary proof host: the inspected Lenovo laptop. The user selected it over their desktop.
- Initial platform/input scope: Win64, keyboard and mouse.
- No required desktop/second-host validation initially; no support claim for that uninspected host.
- Performance target: 2560 × 1440 at 120 FPS on the primary host, pending actual measurement.
- Tooling direction: follow Epic/Microsoft setup guidance; proposed additions remain separate from
  installation authorization and completed build proof.

120 FPS implies approximately 8.33 ms per frame. It is an engineering target, not a benchmark result,
minimum supported machine specification or promise across every renderer/quality configuration.
Phase 1.4 must define rendering/display mode, internal resolution/upscaling/frame-generation policy,
build configuration, measurement route/duration, warm-up, frame-time acceptance and memory budgets.
Proposed measurement conditions are a packaged build, AC power, NVIDIA GPU and initially no frame
generation. Those detailed conditions remain proposals for 1.4 rather than silently accepted settings.

## Observed Host

| Item | Observation | Evidence |
| --- | --- | --- |
| System | Lenovo model 83F5 | Windows CIM system query |
| OS | Windows 11 Business, 64-bit, build 26200 | Windows CIM OS query |
| CPU | Core Ultra 9 275HX; 24 cores / 24 logical processors | Windows CIM processor query |
| Memory | Approximately 63.4 GiB reported system RAM | Windows CIM system query |
| GPU | NVIDIA RTX 5090 Laptop GPU; 24,463 MiB total GPU memory; driver 610.74 | CIM adapter inventory and `nvidia-smi` query |
| Other adapters | Intel graphics and a virtual display driver also present | CIM adapter inventory; actual renderer selection untested |
| Free space | C: approximately 97.8 GiB; D: approximately 150.8 GiB | Filesystem drive query; point-in-time capacity, not I/O measurement |

Sandboxed CIM access initially failed; the same read-only queries succeeded with runtime-approved
escalation. No hardware settings were changed. Display refresh rate, thermals/power mode, sustained
performance and actual Unreal GPU selection remain unverified.

## Observed Tools And Components

| Item | Observation / evidence | Limit |
| --- | --- | --- |
| UE | 5.8.3, CL 58210709 from `Engine\Build\Build.version`; editor, UBT DLL and build/UAT scripts present | No launch, compile, cook or package test |
| VS | Community 2026 18.10.3; install 18.10.12224.181; `vswhere` reports complete/launchable, no reboot required | IDE integration not exercised |
| MSVC 14.50 | Folder family 14.50.35717; compiler product version 14.50.35739, file version 19.50.35739 | Compiler/linker, representative header and runtime library present; build untested |
| MSVC 14.51 | Folder family 14.51.36231; compiler product version 14.51.36260; VS default file still names this family | Keep side by side; not the intended UE compiler target |
| SDK | 10.0.26100.0; Windows/UCRT headers, x64 kernel32/UCRT libraries and resource compiler present | Representative file checks, not complete link proof |
| .NET | System SDK 10.0.204; engine bundled `DotNet\10.0` directory present | Does not prove every VS workload is installed |
| C++ workloads | Native Desktop and Native Game matched by `vswhere` | No full workload execution test |
| C++ tools | AddressSanitizer and C++ profiling component matched | Functionality not exercised |
| UE integration | IDE, debugger and `Microsoft.VisualStudio.Component.Unreal.TestAdapter` matched | Editor-side integration and test discovery not validated |
| Blender | `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe`, version metadata 5.2 | Not on inspected PATH; no launch/MCP/export proof |
| Python | Direct installed interpreter reports 3.14.6; Pillow import discovery succeeds | WindowsApps alias inaccessible in sandbox, not a missing installation |
| Media tools | FFmpeg 9.0.1 reported by executable; FFprobe resolves on PATH; ImageMagick package 7.1.2.30 registered | ImageMagick alias inaccessible in sandbox; no new media processing |
| Git | 2.54.0.windows.1; Git LFS 3.7.1 executable present | LFS asset policy remains a later decision; no LFS initialization |
| Unreal MCP | ModelContextProtocol, ToolsetRegistry and AllToolsets descriptors present | No enablement, server connection or capability validation |

Unreal installation inspected at `D:\Epic Games\UE_5.8`; VS at
`D:\Program Files\Microsoft Visual Studio\18\Community`. These are host observations, not required
paths for other contributors. No `.uproject` was found in the repository inventory.

## Compiler Reconciliation

The installed `Windows_SDK.json` prefers the 14.50 family and bans compiler versions through
14.50.35722. The installed UBT source `MicrosoftPlatformSDK.cs` uses the tool directory name for
family ranking, but reads `cl.exe` product-version metadata for the banned-version check.
Therefore folder name 14.50.35717 does not mean this patched compiler is banned: its actual
14.50.35739 product version clears that range. This is static compatibility evidence, not build proof.

No build-configuration XML was present at the inspected engine Saved, user Roaming and user Documents
locations. No global defaults were changed. Phase 2.3 must record UBT's effective compiler and SDK;
do not infer them solely from VS's default file or force a global compiler change preemptively.

The first inventory queried the wrong test-adapter ID and reported no match. A corrected check using
Microsoft's published `Microsoft.VisualStudio.Component.Unreal.TestAdapter` positively matched it.
This record supersedes that initial report; no test-adapter installation is proposed.

## Setup Gaps And Deferred Actions

The following IDs did not match the inspected VS instance:

- `.NET desktop development` — `Microsoft.VisualStudio.Workload.ManagedDesktop`.
- `.NET Multi-platform App UI development` — `Microsoft.VisualStudio.Workload.NetCrossPlat`.
- MSVC 14.50 ATL — `Microsoft.VisualStudio.Component.VC.14.50.18.0.ATL`.
- Unreal Engine installer — `Component.Unreal`.

Recommend the two .NET workloads to follow Epic's setup guide and matching 14.50 ATL from the
installed engine's VS 2026 suggestions. The engine is already installed, so the installer component's
absence does not establish a missing engine or justify installing another copy. Review actual installer
selections, dependency/storage impact and any new engine warnings in the separately scoped tooling
step. User preference for vendor guidance does not select every optional VS component.

No confirmed installation blocker remains for the selected compiler/version baseline. Full setup
alignment and compilation proof are still incomplete. Blender/MCP/client compatibility, editor-side
VS integration, renderer settings and packaged runtime behavior remain at their existing later checkpoints.
No further user decision blocks closing this inventory; Phase 1.2 requires its own authorization.

## Primary References

Checked 2026-10-07:

- [Epic VS setup](https://dev.epicgames.com/documentation/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine): UE 5.8 tooling versions, workloads and profiling/sanitizer setup.
- [Microsoft UE integration](https://learn.microsoft.com/en-us/visualstudio/gamedev/unreal/get-started/vs-tools-unreal-install): IDE/debugger/test-adapter roles and editor-plugin dependency.
- [Microsoft component directory](https://learn.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-community): corrected test-adapter and workload IDs; do not use catalog versions as proof of locally installed versions.
- Installed engine `Engine\Config\Windows\Windows_SDK.json` and `Engine\Source\Programs\UnrealBuildTool\Platform\Windows\MicrosoftPlatformSDK.cs`: version policy and detection behavior.
