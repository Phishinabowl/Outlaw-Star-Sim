# Blender And Unreal Editor Automation

Status: development-tool evaluation requirements confirmed for publication, 2026-10-07. No connector selected,
installed, enabled or connected. This document owns editor-automation requirements; the
[slice implementation plan](../implementation/vertical-slice-1-implementation-plan.md) owns
execution checklists and gates. Baseline v1 remains authoritative for reconstruction.

## Role And Sequence

MCP is an optional way to inspect and modify development scenes. Neither server is a dependency
of the playable slice or a replacement for Git, reviewed source files, evidence or runtime state.
Choose tools for demonstrated tasks rather than catalog size. The user's supplied ChatGPT discussion
is a proposal; the upstream findings below are separately identified.

Blender is the reconstruction direction. A Blender MCP pilot belongs before repeated geometry
production in Phase 3.2/3.3, using the accepted scale/player fixture from 3.1. Useful tasks include
hull/room proxies, four-cylinder placement, swept-volume helpers and repeatable orthographic views.
Outputs still require human/evidence review; generated geometry is not canon.

Unreal MCP can be evaluated after the minimal project's successful build/editor proof in 2.3.
Useful tasks include scene inspection, bounded actor placement and test invocation. This can happen
before Blender grayboxing because Unreal foundation proof precedes the playable spatial fixture.
Blender may be the first geometry automation tool adopted; both connectors need not be installed
together. Phase 1.4 may choose to defer either pilot entirely.

## Candidates And Verified Limits

Sources checked 2026-10-07; upstream compatibility and capabilities must be rechecked at adoption.

| Candidate | Upstream finding | Project position |
| --- | --- | --- |
| [Epic Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor) | Experimental embedded server; incomplete/changeable APIs. `ModelContextProtocol` supplies the server; tool providers use `ToolsetRegistry`, with `AllToolsets` as a convenience bundle. | Evaluate first for Unreal rather than assuming a community replacement is needed. Verify selected toolsets and actual client discovery. |
| [Blender Lab MCP](https://www.blender.org/lab/mcp-server/) | Official page requires Blender 5.1+, an add-on, an MCP server and an LLM client. It explicitly warns generated Python has no guards against data removal or remote transmission, recommending a VM or a system without sensitive information. | Candidate, not automatic selection. Record an isolation decision before executing it; a disposable scene alone does not isolate filesystem/network access. |
| [RFingAdam/mcp-blender](https://github.com/RFingAdam/mcp-blender) | README advertises Blender 4.2 LTS/5.0 and a stdio server with a Blender TCP add-on; it includes unrelated generation/integration features. Repository license metadata and `LICENSE` indicate AGPL-3.0 while README claims MIT. | Inspect a pinned revision, dependencies and actual license before adoption. Do not infer quality from advertised tool count or enable external asset/generation services. |
| [glonorce/Blender_mcp](https://github.com/glonorce/Blender_mcp) | Community candidate advertising structured tools and Blender Python execution. | Verify supported Blender version, dependency/transport requirements, license and code-execution behavior at a pinned revision; no local compatibility proof yet. |

Local read-only inspection found these descriptors in the installed UE 5.8.3 engine:

- `Engine\Plugins\Experimental\ModelContextProtocol\ModelContextProtocol.uplugin`
- `Engine\Plugins\Experimental\ToolsetRegistry\ToolsetRegistry.uplugin`
- `Engine\Plugins\Experimental\Toolsets\AllToolsets\AllToolsets.uplugin`

The first descriptor marks the plugin experimental and disabled by default. File presence proves
availability for later evaluation, not project enablement, connection or successful execution.
Blender installation/version and the chosen client/server combination remain unverified here.
The Blender official page's full fetch failed; its indexed official-page text supplied the requirements
and warning above. These must be reconfirmed before setup.

## Adoption Requirements

Phase 1.4 records proposed selection or deferral and the following evaluation contract. Later scoped
authorization covers any installation, plugin/configuration change and pilot scene mutation.

- Pin the application and server/add-on revision; record source, license, dependencies, transport,
  startup/stop procedure and actual client compatibility. Preserve existing client configuration.
- Select only tools needed for the pilot. Review arbitrary Python, shell, file, network and destructive
  operations; a structured schema or loopback listener is not a sandbox. Resolve the official Blender
  warning through an accepted isolated environment or choose another reviewed workflow.
- Use project-owned disposable assets with recoverable copies and explicit output paths. Source
  media stays immutable/local-only; no media upload or external generation service is included.
- For Unreal, keep the listener local. Epic documents no authentication and serialized game-thread
  calls: do not issue overlapping mutations. Verify binding and stop/reconnect behavior in the pilot.
- Agree the Blender→Unreal handoff: units, axis/orientation, origin/pivots, naming, export/import settings,
  collision and source/export ownership. Check one known-size fixture in Unreal before bulk production.
- Keep repeatable Blender Python/build recipes and scene manifests as reviewable text where practical.
  Owned `.blend`, maps and Blueprints follow the agreed binary/LFS policy; backups are not commits.
- Record before/after scene inventory, intended changes, saves, exports and resulting file diff.
  Reopen saved assets and verify results independently; an MCP success response is not visual proof.
- Desktop mouse/keyboard or foreground-control tools still require the explicit Computer Use permission
  in `AGENTS.md`. Connector installation or phase approval does not grant it.

## Bounded Pilot And Acceptance

Each pilot starts with read-only discovery/scene inspection, then one reversible change to an owned
fixture. Save/reopen, stop/reconnect and verify the actual result and all affected files. Record latency,
errors, tool availability, recovery and whether the workflow is useful enough to retain.

The Unreal pilot follows 2.3; use a neutral actor fixture and repeat the 2.4 standalone smoke with
the selected configuration. The shipped build must work without an MCP client/server running;
record how development automation is excluded or disabled in the package.

The Blender pilot follows 3.1 and precedes MCP-assisted 3.2/3.3 production. Inspect and create a
known-size proxy, record its recipe, export/import it and verify scale, transform, pivot and collision
against the same player fixture. Do not build ship geometry merely to prove connector connectivity.

Pass means observed, reproducible results, bounded changes and demonstrated recovery. Failure or
deferral selects ordinary editor operations or reviewed Blender Python scripts with the same evidence
and asset contracts. Disable only pilot settings/processes, restore the owned fixture from its checkpoint
and preserve unrelated user settings. Optional MCP failure does not block the slice when fallback passes.

## Deferred Extensions

Custom XGP toolsets are deferred until a concrete repeated task warrants them. Proposed state queries,
room-clearance checks and startup-test runners are examples, not an approved API backlog. Future tools
must use the shared [command/query and result contract](external-control-automation.md); they must not
create another readiness writer. Debug fixtures must be distinguishable from player actions and cannot
replace locality/visual acceptance tests. Fault injection and a damage model remain outside Slice 1.

Server catalogs, client settings and connection instructions belong in later verified setup records.
No always-on server, remote access, broad custom framework or packaged MCP dependency is selected.
