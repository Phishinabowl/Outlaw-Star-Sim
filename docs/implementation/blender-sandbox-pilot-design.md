# Blender Sandbox Pilot — Design And Read-Only Findings

| Field | Value |
| --- | --- |
| Date | 2026-10-10 |
| Status | Deferred 2026-10-11; retained findings/alternative design; not a current pilot prerequisite |
| Purpose | Determine whether official Blender MCP can support recoverable geometry work within a practical isolated environment |
| Authority | [Editor automation requirements](../architecture/editor-automation.md), [Phase 1.4 draft](phase-1-4-architecture-asset-validation-draft.md) and accepted handoff conventions |
| Timing | Setup needs its own later scope; connected geometry/handoff pilot follows Phase 3.1 and precedes repeated 3.2/3.3 production |

The user requested this design and capture of findings, explicitly retaining no-install/no-enable
boundaries. No Sandbox configuration, script, fixture, account, firewall rule, package or dependency
is created or executed by this document. Documentation publication confirmed 2026-10-11. The observations below
own the dated Blender connector/Sandbox investigation; other documents should link here.

On 2026-10-11 the user selected [local MCP pilots for both editors](../architecture/editor-automation.md#current-local-pilot-contract--accepted-2026-10-11)
and deferred Sandbox/VM work. All guest isolation, networking, administrative enablement and BP-00–05
execution gates below belong to this retained alternative, not the current implementation path.
Do not resume them without a new reason and user-agreed scope. Verified source/host findings remain
useful; no Sandbox or MCP setup has been performed.

## Verified Host Findings

Read-only queries on the primary Lenovo 83F5 laptop found:

| Observation | Evidence / interpretation |
| --- | --- |
| Windows 11 Business, build 26200, 64-bit | `Win32_OperatingSystem`; registry EditionID is Professional, DisplayVersion 25H2 |
| Windows Sandbox disabled | `Win32_OptionalFeature`, `Containers-DisposableClientVM`, InstallState 2; Microsoft defines 2 as Disabled |
| Related optional features disabled | WMI reports 2 for VirtualMachinePlatform, HypervisorPlatform and listed Microsoft-Hyper-V components |
| Hypervisor active | `Win32_ComputerSystem.HypervisorPresent=True`; its originating feature/security component was not investigated |
| CPU virtualization flags all false | WMI reports false for firmware virtualization, monitor extensions and SLAT while a hypervisor is active; do not use this alone to prescribe BIOS changes |
| No inspected Sandbox installation entry | No System32 Sandbox executable, matching app package or vmcompute/vmms service returned in these checks; this is scoped evidence, not an exhaustive servicing inventory |
| Administrative servicing query unavailable | `Get-WindowsOptionalFeature` requires an elevated Windows token; tool sandbox escalation allowed CIM reads but did not provide that token |

Sandbox is an available optional feature entry, currently disabled, not an operational environment.
Payload download requirements, administrative enablement/reboot, graphics and launch compatibility
remain untested. No feature or BIOS change was attempted.

Microsoft references: [feature states](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-optionalfeature),
[Sandbox overview](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/)
and [hypervisor requirements](https://learn.microsoft.com/en-gb/windows-server/virtualization/hyper-v/host-hardware-requirements).

## Pinned Official Connector Findings

Repository: [lab/blender_mcp](https://projects.blender.org/lab/blender_mcp).
Inspected revision: [dbbf836ad4b1025f14a2b3b504c43903f39e0b04](https://projects.blender.org/lab/blender_mcp/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04).
Read through the upstream HTTPS API in memory after browser page fetches failed. No clone/download
was saved and no repository code was run. This is a targeted transport/execution review, not a full
security audit or dependency vulnerability assessment.

| Finding | Pinned source |
| --- | --- |
| Separate bridge and Blender add-on; default MCP stdio, then TCP to Blender | [README](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/readme.md) |
| Bridge package 1.0.2; Python >=3.10 declared; docutils, pyyaml and mcp[cli]>=1.2.0,<2; setuptools>=68 build requirement | [pyproject](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/mcp/pyproject.toml) |
| Add-on manifest 1.0.0, Blender >=5.1.0, GPL-3.0-or-later; reviewed code carries the same SPDX license | [extension manifest](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/addon/blender_mcp_addon/blender_manifest.toml) |
| Add-on defaults localhost:9876; plain null-delimited JSON requests execute Python; no authentication/TLS check observed in the inspected path | [socket server](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/addon/blender_mcp_addon/mcp_to_blender_server.py) |
| Bridge endpoint configurable through BLENDER_MCP_HOST / BLENDER_MCP_PORT | [connection helper](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/mcp/blmcp/tools_helpers/connection.py) |
| Optional HTTP defaults 127.0.0.1:8000, path /; stateless streamable HTTP, wildcard CORS and DNS-rebinding protection disabled; no authentication configured in this entry point | [bridge entry point](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/mcp/blmcp/__init__.py) |
| Small bypassable guardrails block select exits/preference operations, not filesystem/network access | [weak_sandbox](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/addon/blender_mcp_addon/weak_sandbox.py) |
| Tools include both interactive Python execution and launching background Blender from the bridge's machine | [execution tools](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/mcp/blmcp/tools/execute_blender_code.py), [CLI helper](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/mcp/blmcp/tools_helpers/blender_cli.py) |
| CLI helper creates/removes numbered blend copies; tool discovery registers all eligible modules, not a reviewed pilot allowlist | Same helper and bridge entry point |
| Add-on auto-start defaults true; startup requires Blender online-access preference, including for local socket operation | [add-on entry point](https://projects.blender.org/lab/blender_mcp/src/commit/dbbf836ad4b1025f14a2b3b504c43903f39e0b04/addon/blender_mcp_addon/__init__.py) |

The dated Blender 5.2 installation satisfies the declared minimum numerically, but no runtime proof
exists. Dependency ranges are not a reproducible lock; resolve/hash a compatible dependency set
before later setup. Package and add-on version numbers differ because they are separate components.
Tool readOnly/destructive hints are advisory metadata, not OS enforcement; output-generating tools
can write files. Prompt instructions bundled with the connector are untrusted reference content.

## Proposed Execution Boundary

Keep Blender, the add-on, the MCP bridge, its Python environment and background Blender executable
inside the guest. Host runs only the existing AI client and, if necessary, a separately reviewed
transport relay which cannot execute Blender/Python requests on the host. Do not run the official
bridge on the host merely to reach a guest Blender listener: its CLI tools would undermine isolation.

```text
Host AI client
    | restricted, verified MCP transport
    v
Sandbox: bridge -> guest-loopback TCP -> Blender/add-on
             \-> background Blender (also guest)
    |
    v
Disposable exports/logs -> review -> deliberate import into project
```

The isolated environment can still damage its writable output share. Its purpose is to bound access
to disposable pilot data, not to guarantee that every generated file is safe or correct.

## Proposed Folder And Sandbox Policy

These are planned locations, not created directories. Keep host-specific absolute paths out of a
shared runnable configuration; later generate a local .wsb from a reviewed text recipe.

| Host location under .local/blender-pilot/ | Guest access | Contents |
| --- | --- | --- |
| input/ | Read-only, mounted as C:\PilotInput | Vetted portable/bootstrap packages, reviewed source snapshot/recipes, owned fixture copies |
| runs/<run-id>/output/ | Read/write, mounted as C:\PilotOutput | Only disposable blend/FBX files, manifests, screenshots and diagnostic logs |
| Everything else | Not mapped | Repository parent/.git, source media, other repos, personal profile, credentials, host package environments |

Use a fresh output directory each run; originals/checkpoints live outside that writable share. Guest
working files belong to its own local temporary workspace, not input. No Git checkout, publishing key,
cloud sync or browser login inside the guest. No symlinks/junctions exposing a wider host directory.

Proposed settings: clipboard, microphone, webcam and printer redirection disabled; Protected Client
enabled if compatible; vGPU enabled for the viewport check, recording that GPU sharing increases the
interface surface and does not guarantee native RTX/CUDA/OptiX availability. Start with 16,384 MB
guest memory for tiny fixtures on the dated ~64 GB host, then adjust only from observed need.
No host benchmark conclusions may be drawn from guest timing. Default Sandbox networking is not
accepted as the isolation policy.

Use offline staged dependencies where practical. A reviewed bootstrap installs only guest-local
components, disables add-on auto-start, establishes restrictions and then starts services manually.
Do not start connector execution automatically before the access checks. Record exact versions,
package hashes and commands before running anything. Guest restart can preserve state, but closing
Sandbox discards it; persistent mapped output survives and must be reviewed separately.

Microsoft's [configuration reference](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file)
documents these options. Actual configuration generation, payload staging and enablement are later
authorized work, not this document.

## Network Design — Connected Stage Has A Hard Prerequisite

Stage A disables networking entirely and exercises only trusted bootstrap/graphics checks. It cannot
prove host MCP connectivity. Stage B requires one explicit control route before generated code runs.

Preferred connected shape: guest bridge and add-on remain loopback-only, using a reviewed restricted
relay/tunnel for the host client. If private-interface HTTP is evaluated instead, authenticate the
control channel and address its permissive CORS/DNS-rebinding behavior; the stock HTTP endpoint alone
is not the approved boundary. Expose neither raw port 9876 nor an unauthenticated HTTP listener to
the LAN. Exact relay/tunnel or HTTP hardening is not selected, implemented or proven here.

Allow only the host-client control exchange. Prevent guest internet/LAN access and unrelated host
services through enforcement generated code cannot reconfigure. Guest firewall rules alone are
insufficient if Blender executes with guest administrator rights. Use a verified host/hypervisor
enforcement boundary or an adequately restricted guest identity/control-plane arrangement, with its
privilege behavior tested. Blender's online-access preference is an add-on prerequisite, not a network
sandbox; enabling it would not remove these OS restrictions.

Windows Sandbox's .wsb options provide networking on/off, not a destination/port allowlist. Therefore
the proposed restricted connected path is a preflight gate, not an implied built-in configuration.
Before drafting execution scripts, establish whether this host can support the needed enforcement
and transport without broad access. If it cannot, stop the connected Sandbox proposal and review a
persistent VM with a controlled private network or the restricted-account alternative. Do not silently
leave default networking enabled or put a model account's credentials into the guest to avoid routing.

## Independently Reviewable Pilot Steps

| Step | Prerequisite / activity | Required evidence / exit | Stop or iteration point |
| --- | --- | --- | --- |
| BP-00: preparation design | Agree isolation/network policy, packages, local paths, ownership and later enablement/reboot scope | Reviewed .wsb/bootstrap/transport recipe and version/hash manifest; no guest or project changes yet | Resolve missing enforcement/transport; revise or choose VM before enabling |
| BP-01: offline bootstrap and graphics | Separate setup authorization; Sandbox enabled by owner/admin, stage vetted packages, launch offline guest | Blender/version inventory; viewport and tiny render/export supported; only intended shares/redirections visible | Close guest, preserve output/logs; review vGPU/protected-client compatibility without automatically relaxing settings |
| BP-02: connected boundary proof | Reviewed control route and permission/network enforcement; start bridge/add-on manually | Host client discovery; actual endpoint bindings; no CLI execution escapes guest; unexpected LAN/internet/host-service access denied | Any unexpected access fails boundary; stop services and close guest before model-generated code |
| BP-03: reversible geometry | Phase 3.1 fixture plus passed boundary checks | Inspect scene; create/position measured 1 m cube; record intent/state; save and reopen; return image/summary; all files within output | Restore disposable scene checkpoint or close guest; no ship production |
| BP-04: handoff and recovery | Geometry success; agreed export recipe | Export/reimport scale/orientation/pivot/collision fixture in Unreal; restart connector and reconnect; fresh guest repeat from recipe | Fix recipe at fixture level; retain independent body/clearance proof and no bulk modeling |
| BP-05: decision | Reviewed results for boundary, usability, fidelity, save/recovery and handoff | Adopt bounded workflow, revise, or defer with recorded limitations; user reviews visual result | Fallback uses reviewed scripts/editor work; optional connector failure does not block slice |

BP-01 must not launch model-generated Python even if graphics works. Basic network/bootstrap tests
use reviewed deterministic scripts. BP-02 discovery alone is not permission for arbitrary tools.
Select only scene inspection and necessary fixture operations for model-visible use, explicitly
including or excluding background execution; enforcing an allowlist may require a reviewed bridge
change/wrapper because upstream auto-registers tools. It is defense in depth, not a substitute for
the execution boundary. No external generation/download service is included.

Permission tests use harmless sentinel paths/data, bounded timeouts and administrator-controlled
configuration. Demonstrate read-only input rejection, writable output, absent unrelated mounts,
allowed control route and denied unrelated network destinations using owned test endpoints. Never
probe credentials or delete originals to prove isolation. Static configuration review is insufficient.
Human visual inspection is required; Computer Use still needs its own explicit permission under AGENTS.

## Evidence, Import And Recovery

Track authored version/recipe/decision summaries under docs; raw downloaded packages, source snapshots,
logs, images and fixture binaries stay in .local until any explicit promotion. Save request/error logs,
before/after inventory, output hashes and actual observed versus unexecuted checks. Do not label a
successful tool response as visual/handoff proof.

Before opening output on the host, inspect expected file types/dependencies and embedded scripts;
keep auto-run Python disabled for unreviewed blend output. Do not auto-run exported scripts or grant
trust merely because the file came from our pilot. Accepted assets are copied deliberately into their
owned source/export locations under the agreed Git/LFS policy, not published from the transfer share.

Stop add-on/bridge, verify process/listener exit and close Sandbox after the run. Closing discards guest
changes but does not undo host feature enablement, host network rules or shared output. Later setup
must record original feature/rule/config state and scoped rollback commands; do not disable pre-existing
virtualization/security components or revert unrelated settings. Preserve findings before restoring
only pilot-owned resources. Nothing is committed or pushed without confirmation.

## Remaining Decisions Before Any Setup

- Agree whether to pursue Sandbox subject to the network gate or choose another isolated environment.
- Select and prove the restricted host-client transport and enforcement method; source supports stdio
  and HTTP, but neither by itself establishes cross-guest isolation.
- Resolve exact packages/dependency hashes, guest Python/Blender versions and tool allowlist strategy.
- Review the concrete administrative enablement/reboot and rollback scope, then seek execution approval.
- Verify actual Codex client discovery, graphics and handoff in the later pilot; no success is assumed.

Phase 1.4 can record a conditional candidate and these explicit gates. It must not claim operational
MCP adoption or a completed sandbox merely because a pilot design has been authored.
