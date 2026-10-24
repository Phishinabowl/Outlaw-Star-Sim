# Phase 2.3 — Local Unreal MCP Pilot

| Field | Value |
| --- | --- |
| Started | 2026-10-23 |
| Status | Pilot/cleanup and project-user auto-start verified; retention and 2.3 closeout accepted 2026-10-23 |
| Authorization | Optional Unreal MCP pilot requested after ordinary 2.3 proof; closeout deferred; no 2.4 |
| Baseline | Published `23ace3f` plus current uncommitted 2.3 evidence and owner-enabled project plugins |
| Contract | [Local pilot requirements](../../architecture/editor-automation.md#current-local-pilot-contract--accepted-2026-10-11) |

## Verified Setup

The installed engine is UE 5.8.4/CL 58902052. Engine-shipped ModelContextProtocol and EditorToolset
descriptors identify experimental version 1.0 plugins from the installed Epic distribution. Their
engine license applies; no third-party server package or Python dependency installation was performed.

The repository owner enabled Unreal MCP, restarted/saved the descriptor, then enabled EditorToolset
and restarted again. Saved OutlawStarSim.uproject now has both enabled. The second startup log records
EditorToolset DLL loading and actor, scene, primitive, asset and other toolset registration. Registration
counts change during startup; a logged count is not actual MCP client discovery evidence.

ToolsetRegistry dependencies include PythonScriptPlugin, EditorScriptingUtilities and FileSandbox.
EditorToolset was chosen instead of the broader AllToolsets aggregator for the neutral actor pilot.
The available programmatic toolset is not permission for arbitrary scripts or unrelated file access.
No engine source, unrelated client settings or reference media were changed.

The inspected settings class defaults Auto Start Server to false, port to 8000 and URL path to `/mcp`.
No corresponding override was initially found in the checked project-user settings. The repository
owner subsequently confirmed auto-start off, port 8000, path `/mcp`, and ran the manual start command.

## Connection Checks

The current editor session writes `OutlawStarSim_2.log`; the unnumbered log belongs to a prior
closed process. The live log records `ModelContextProtocol.StartServer` and creation of an HTTP
listener at **127.0.0.1:8000**. An OS listener query independently matches that loopback address
and the running main-project editor PID. The MCP listener is not bound to a LAN/wildcard address.

Serialized read-only HTTP requests initialized MCP, sent initialized notification, listed tools and
called `list_toolsets`. Initialize returned HTTP 200 and protocol **2025-11-25** (the request offered
2025-03-26); follow-up requests used the returned version. The serverInfo fields were empty, so plugin
version attribution uses the installed descriptors rather than invented handshake metadata.
The catalog advertises `list_toolsets`, `describe_toolset` and `call_tool`; actual list_toolsets output
includes scene/actor/primitive tools. No scene mutation has run. Protocol evidence is retained locally
under `.local/validation/phase-2-3/mcp-*.json`, without publishing session metadata.

Codex CLI reports **0.163.0-alpha.11.2**. A new host-local, Git-ignored `.codex/config.toml` defines
`mcp_servers.outlaw_star_unreal` with Streamable HTTP URL `http://127.0.0.1:8000/mcp`, enabled state,
20 s startup and 60 s tool timeouts, the three discovery tools, and default tool approval mode `prompt`.
No prior project configuration existed and unrelated global settings were untouched.
`codex mcp get outlaw_star_unreal --json` successfully reads the expected configuration. This confirms
configuration parsing, not that this already-running chat has loaded the new native MCP tools.
Restart/reload the client before claiming native Codex tool discovery. Server auto-start remains off.

After the repository owner restarted Codex, native `mcp__outlaw_star_unreal` tools became available.
Native list_toolsets and describe_toolset calls succeeded, followed by SceneTools.get_current_level
returning `/Game/XGP/Development/L_NeutralProof` and find_actors returning live actor references.
These serialized calls were read-only; no scene mutation, selection or viewport manipulation occurred.

The supplied Codex settings screenshot shows disabled-looking gear/toggle controls for this entry.
The entry is project-scoped and file-configured; official documentation confirms this configuration
layer, but the exact reason for the app's disabled controls is unverified. Native connection success
is established independently of that UI. No global-config migration or scope change was performed.

## Mutation And Recovery

First mutation attempt: AssetTools.duplicate created an in-memory copy at
`/Game/XGP/Development/MCPPilot/L_MCPPilot`. SceneTools.load_level refused to switch because the
target copy had unsaved changes (initially misdiagnosed as the original's state). A subsequent placement call was mistakenly dispatched before
handling that failure and created MCP_Pilot_Cube in the original level. It was immediately removed
with remove_from_scene, and find_actors confirmed no matching pilot actor remains. The original
map file retained its baseline SHA-256; it was not saved or reverted. Further dependent mutations
must inspect each result before proceeding.

Only the copied map was then saved successfully, creating `MCPPilot/L_MCPPilot.umap` (49,081 bytes).
The owner confirmed no independent scene edits and authorized discarding the unsaved test state.
After saving the target copy, load_level succeeded; get_current_level verified the pilot map before
the next placement. No save-all or write to the original map occurred.

## Saved Pilot Mutation

The pilot map initially returned 15 actor references including engine-generated actors. A single
engine Cube was placed with label `MCP_Pilot_Cube`, location (0,0,100) cm, zero rotation and unit scale.
Its returned reference belongs to `MCPPilot/L_MCPPilot`, not the original. save_assets targeted only
the pilot map and succeeded. Loading the original and then the pilot again succeeded; find_actors
found the labeled cube and get_actor_transform independently returned the intended transform.
The original file SHA-256 still matches the baseline.

An optional CaptureViewport request failed schema handling because an omitted annotations parameter
was reported as needing a default. No image or visual pass is claimed from that call. Owner visual
confirmation was subsequently supplied: the repository owner selected/framed the labeled cube and
confirmed it was visible. This observation supplies the visual evidence; no desktop control was used.

## Stop, Reconnect And Cleanup

The owner ran StopServer. OS inspection still found a loopback listener at 127.0.0.1:8000, but GET
and protocol POST requests to `/mcp` returned HTTP 404. Installed StopServer source unbinds MCP routes
and clears its router reference without stopping the shared engine HTTP listener. Thus MCP route
shutdown passed; full TCP-listener shutdown is not the behavior of this command. Closing the editor
is the ordinary way to release its remaining listener. No engine source/firewall changes were made.
Stopped evidence: local `mcp-stopped.log` and `mcp-stop-probe.json`.

After the owner manually restarted the server, native list_toolsets, get_current_level and find_actors
succeeded without another Codex restart. The saved pilot cube was still found. It was removed,
only the pilot map was saved, and loading away/back confirmed find_actors returned no pilot cube.
The original map was then reloaded and its path verified before deleting pilot content.

AssetTools.delete returned false; the engine log reported that assets were removed but the directory
could not be removed. File inspection still found the single temporary map. Native PowerShell then
removed only the exact verified MCPPilot folder after workspace/ancestor reparse-point and expected
contents checks. Absence was verified; no pilot actor remains in the current original map. Original
SHA-256 still matches the published baseline. `mcp-reconnect-cleanup.log` preserves the local log.
The disposable scene change is fully reversed; no pilot content is intended for publication.

The pilot demonstrates useful scene inspection, bounded placement and persistence, but also records
the optional-argument capture issue, target-dirty load guard and deletion fallback. Do not treat all
EditorToolset functions as proven.

## Final Shutdown And Auto-Start Review

The owner ran StopServer again and closed Unreal. The current session log records the stop command,
editor shutdown and exit. Independent checks found zero UnrealEditor/UnrealEditor-Cmd processes,
zero port-8000 listeners, and connection refusal at the MCP endpoint. `mcp-final-closed.log` preserves
the final local log. Pilot shutdown and cleanup are verified.

After these checks the owner proposed auto-start for regular use. The installed setting is
EditorPerProjectUserSettings, default false. Enabling it would start MCP alongside interactive
editor launches; it would not create a separate Windows service. Installed source skips this
preference for commandlets unless the explicit start-server command-line flag is supplied.
This does not prove packaged-runtime exclusion, which remains a Phase 2.4 check.
Project-local interactive auto-start is a reasonable proposed convenience after the bounded pilot;
actual preference change, automatic startup and loopback binding were subsequently verified below.
The earlier manual-only pilot policy remains historical; broader/global auto-start is not proposed.

## Automatic Startup Verification

The owner enabled Auto Start Server and restarted Unreal. Saved project-user settings contain
`bAutoStartServer=True`, port 8000 and `/mcp`. The new editor command line contains only the project
descriptor, with no start-server flag. Its fresh startup log records the MCP server and loopback
listener starting during engine initialization, with no manual StartServer command. An independent
OS query ties 127.0.0.1:8000 to that editor process. Native get_current_level succeeds and returns
`/Game/XGP/Development/L_NeutralProof`. The local snapshot is `mcp-autostart.log`.

Auto-start is verified for this interactive project session; MCP is intentionally running while
the editor remains open. Earlier manual shutdown and editor-exit behavior were independently tested.
Recommend retaining the integration for local development, with ordinary editor/file fallback and
the documented tool limitations. Packaged behavior is untested and belongs to 2.4.

All pilot steps above are complete. Manual startup was used for the initial pilot; approved
project-user auto-start was then verified separately. No 2.4 work follows automatically.

Sources checked 2026-10-23: [Epic Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor),
[Codex MCP configuration](https://developers.openai.com/codex/mcp), installed descriptors/source and local startup log.
