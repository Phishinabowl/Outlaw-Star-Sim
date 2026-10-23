# Phase 2.1 — Post-Installation Results And Closeout Proposal

| Field | Value |
| --- | --- |
| Observed / prepared | 2026-10-23 |
| Source checkpoint | `main` at `52255d5`; worktree clean at the post-installation read-only check |
| Status | Phase 2.1 closeout accepted 2026-10-23; availability verified, build proof pending |
| Scope | Verify repository-owner installations and updated VS metadata; no project initialization or build |
| Evidence | Follow-up `vswhere` queries, file/version inspection and installed engine policy; Codex performed read-only checks |
| Authority | [Phase 2.1 checklist](vertical-slice-1-implementation-plan.md#phase-21-approved-toolchain-preparation), [VS1-T01](validation/foundation-validation-procedures.md#vs1-t01) |

## Verified Post-Installation Results

The [pre-installation preflight](validation/phase-2-1-tooling-preflight-2026-10-23.md) remains the
historical baseline. The repository owner reported completing the two workloads, matching ATL and
another VS update. Follow-up observations establish the following availability results:

| Item | Observed result / evidence | Limit |
| --- | --- | --- |
| Visual Studio Community 2026 | **18.11.1**, installation **18.11.12315.225**; installer metadata reports complete/launchable, no reboot required | Updated from preflight's 18.11.0; no IDE launch performed |
| .NET desktop development | `Microsoft.VisualStudio.Workload.ManagedDesktop` matches the intended VS instance | Workload inventory, not compilation proof |
| .NET MAUI | `Microsoft.VisualStudio.Workload.NetCrossPlat` matches | Workload inventory, no mobile-target expansion |
| MSVC 14.50 ATL | `Microsoft.VisualStudio.Component.VC.14.50.18.0.ATL` matches; `atlmfc/include/atlbase.h` and `atlmfc/lib/x64/atls.lib` present | Previously absent files now present; no ATL compile/link test |
| MSVC 14.50 | Family **14.50.35717**, compiler product **14.50.35739.0**; linker, representative C++ header and x64 runtime library present | Clears installed engine's static banned range; effective build selection untested |
| MSVC 14.51 | Family **14.51.36231**, compiler product **14.51.36260.0**; remains the VS default version text | Retained side by side; no default change proposed |
| Windows SDK | **10.0.26100.0** component matches; Windows/UCRT headers, kernel32/UCRT libraries and resource compiler present | Representative availability, not full link/package proof |
| .NET SDK / desktop runtime | System SDK **10.0.402** added alongside **10.0.204**; Windows Desktop runtime **10.0.13** added alongside **10.0.8** and **8.0.32** | Directory inventory only; no .NET build/first-run command |
| Unreal | Build.version remains **5.8.4 / CL 58902052**; intended preferred compiler ranges and banned ranges unchanged | No engine launch/build; preflight launcher discrepancy was not rechecked in this follow-up |
| Supporting tools/integrations | Native Desktop/Game, 14.50 C++ tools, SDK 26100, Unreal IDE/debugger/test-adapter component queries match; MSBuild and C++ target files present | Tooling integration remains unexercised |
| UBT configuration | Previously observed Roaming BuildConfiguration.xml still has only an empty Configuration root | No compiler/SDK override observed or written |

The three identified setup gaps are resolved at the component/file-availability level. No further
installation is recommended from these observations. This does not certify that every optional
component in a general vendor guide is installed or required for the chosen Win64/MSVC scope.

## Reproduction And Evidence Boundary

- VS instance: `D:\Program Files\Microsoft Visual Studio\18\Community`.
- Query identity with `vswhere -all -products '*' -format json`; query each exact component ID with
  `vswhere -all -products '*' -requires <ID> -property installationPath`.
- Read compiler product versions from the x64 `cl.exe` file metadata. Use `Test-Path` for the ATL,
  header/library and SDK files; read VS's `Microsoft.VCToolsVersion.default.txt` without changing it.
- Read `D:\Epic Games\UE_5.8\Engine\Build\Build.version` and
  `Engine\Config\Windows\Windows_SDK.json` for engine identity, preferred/banned compiler ranges
  and SDK bounds. System .NET versions come from installed SDK/runtime directory names.
- No files or settings changed during the check. No editor, Blender, compiler, build, package,
  installer or MCP server was launched. Blender and other unchanged tools retain the earlier record's
  evidence limits. All build/runtime tests remain unexecuted.

## Proposed Closeout Disposition

Phase 2.1's scoped preparation and availability work is complete; closeout was accepted on 2026-10-23.
The reported installations were performed by the repository owner; read-only follow-up independently
matched the three selected component IDs and representative ATL files. The installation observation
does not claim that Codex performed or audited every installer operation.

VS1-T01 has availability and static-policy evidence only. Actual UBT compiler/SDK selection must be
recorded during Phase 2.3 and corroborated in package work. Do not mark the entire scenario passed
or change the global VS default to hide that pending proof. Phase 2 exit remains open.

## Next Scope — Phase 2.2, Not Yet Authorized

Once explicitly authorized, Phase 2.2 creates the smallest agreed project skeleton at
`Unreal/OutlawStarSim/OutlawStarSim.uproject`, using Games Blank C++ and one initial runtime module.
It adds the neutral `L_NeutralProof` map, applies the accepted repository-local owned-binary/LFS and
generated/source exclusion policy, and records concise build/open instructions. No ship geometry,
character implementation, startup gameplay or production art belongs in this increment.

Build/editor validation is Phase 2.3; the neutral package is Phase 2.4. Binary publication still needs
confirmation, followed by real LFS retrieval evidence for the published revision. A map existing in
the checkout is not proof that it opens or survives retrieval.

## MCP Timing — Existing Sequence

| Checkpoint | Purpose | Boundary |
| --- | --- | --- |
| 2.2 | Create/configure the minimal project and repository boundary through ordinary supported generation/file workflows | MCP is not needed to initialize the project; no connector setup in this increment |
| 2.3 ordinary build/editor proof | Establish that the base project compiles and opens independently | Diagnose foundation problems before introducing connector configuration |
| Optional Unreal MCP pilot after 2.3 | Evaluate official embedded server/tool providers against the neutral fixture: inspect, reversible change, save/reopen, stop/reconnect and recovery | Separate scoped setup/enablement; local contract and current client/tool compatibility review apply; not authorized by closeout |
| 2.4 | Prove neutral standalone package operation | If Unreal MCP was adopted, corroborate that the package runs without the client/server |
| Optional Blender MCP pilot after 3.1 | Use the accepted player/scale fixture to validate known-size export/import before repeated ship geometry production | Before MCP-assisted 3.2/3.3 modeling; can support later modeling without being required for 3.2A image concepts; separate setup scope |

The [editor-automation contract](../architecture/editor-automation.md) owns permissions, current
local-pilot direction and fallbacks. No Sandbox/VM prerequisite is reintroduced. MCP is editor
automation, not a runtime game dependency. Connector setup does not grant Computer Use permission.

**Subsequent scope:** Phase 2.2 only was explicitly authorized on 2026-10-23, with guided Unreal setup.
Do not continue automatically into 2.3 or configure MCP. No initialization, LFS configuration,
installation or MCP enablement occurred in preparing this closeout record.
