# Phase 3.1 — Local Blender MCP Pilot

| Field | Value |
| --- | --- |
| Date | 2026-10-23 |
| Status | Connector, local handoff and published asset recovery checks passed |
| Scope | Early local connector setup and disposable scale/handoff fixture; no 3.2A execution |
| Authority | [3.1 plan](../vertical-slice-1-implementation-plan.md#phase-31-player-and-scale-fixture), [local automation contract](../../architecture/editor-automation.md#current-local-pilot-contract--accepted-2026-10-11) |

## Preparation Evidence

- Official [Blender Lab repository](https://projects.blender.org/lab/blender_mcp) API reported
  revision `dbbf836ad4b1025f14a2b3b504c43903f39e0b04` as its latest commit at inspection.
  This matches the earlier source review. Bridge package declares 1.0.2; add-on declares
  1.0.0, Blender >=5.1.0 and GPL-3.0-or-later.
- Pinned source archive retrieved through the official repository API into ignored
  `.local/blender-pilot/`; SHA-256
  `fa2c63f79b84a99a82f0af184ad8f45faa82a4ad2d500fdaaa73f8d582cb8db6`.
  Public archive-page retrieval failed; no browser interaction was used.
- Source inspection reconfirmed stdio bridge transport, configurable Blender TCP endpoint,
  default localhost:9876 and add-on Auto Start enabled by default. Initial tests used explicit
  `127.0.0.1` and Auto Start disabled; subsequently approved auto-start is recorded below.
  Blender's online-access preference is required by this
  add-on even for local connections; it is not network containment.
- Unmodified add-on files packaged locally as
  `.local/blender-pilot/blender-mcp-addon-1.0.0.zip` for guided installation.
- Separate bridge virtual environment created under `.local/blender-pilot/venv` using the
  bundled Python runtime. Declared dependencies resolved to 41 local wheel artifacts;
  exact filenames/hashes are retained in `.local/blender-pilot/wheel-sha256.json`, with
  resolution log and wheel files beside it. No system Python packages are changed.

## Initial Connection Results

- Owner installed/enabled the add-on, enabled Blender online access, changed Host to
  `127.0.0.1`, disabled Auto Start and manually started the server.
- OS listener inspection found only `127.0.0.1:9876`, owned by PID 66484 at inspection.
  Read-only connected settings confirmed that address/port, Auto Start false and online access true.
- Bridge 1.0.2 built and installed successfully. Built wheel SHA-256:
  `70ad86544b7b4db2f39dbb83a088766241318e8039c30274d4c438bb4f868e70`.
  `pip check` passed and the installed launcher returned its expected transport help.
- A short-lived independent MCP client launched the bridge over stdio, completed initialization,
  discovered 26 tools and successfully queried scene inventory and application/settings metadata.
  Blender returned **5.2.3 LTS**. The unsaved default scene contained Cube, Camera and Light;
  filepath was empty and dirty state false. The probe made no scene changes and closed its
  bridge subprocess on completion. Raw output is `.local/blender-pilot/initial-mcp-probe.json`;
  reviewed probe source is retained beside it.
- Added the ignored project `.codex/config.toml` entry `outlaw_star_blender`, preserving Unreal's
  entry. It launches the local bridge over stdio and passes explicit loopback endpoint variables.
  Eight tools are enabled: object/detail/path/missing-file inspection, API/manual reference lookup
  and interactive Python execution. Background CLI, rendering and UI-navigation tools are excluded.
  Interactive Python still has the accepted broad process permissions; the allowlist is not containment.
  Default tool approval mode is prompt. Native Codex discovery passed after a client restart.

## Native Connection And Disposable File

- Native Codex object/path queries succeeded after restart, before mutation. The scene was still
  unsaved and clean with only Cube, Camera and Light.
- Saved that starting state as `.local/blender-pilot/runs/connectivity-01/baseline.blend`, then
  switched the active file to the separate `connectivity-pilot.blend` in the same folder. Existing
  output files would have caused the reviewed recipe to stop instead of overwriting them.
  Baseline SHA-256: `d8eca22d4a80ad079c0ee495d7c50ea704a625ce0979d5db93938a2005ad77ac`.
- Added only `MCPPilot_OneMetreCube` to the pilot scene, with dimensions 1 × 1 × 1 m,
  location (3, 0, 0.5) m and object scale (1, 1, 1). Selected metric display with unit scale 1.
  Original objects were retained. Recipe: `.local/blender-pilot/create_connectivity_fixture.py`.
- Saved and reopened the pilot through the native MCP connection with UI loading and embedded
  scripts disabled. A subsequent independent inventory/measurement call found the four expected
  objects, exact cube dimensions/scale and clean saved state. Connection remained usable after reopen.
  Raw result: `.local/blender-pilot/runs/connectivity-01/native-reopen-result.json`.
- Owner visually confirmed the additional smaller cube on 2026-10-23. No player clearance,
  Unreal import, material appearance or final handoff pass is claimed. All pilot binary files remain
  ignored/local-only; no ship geometry or 3.2A work was created.

## Stop Test

Owner clicked Stop MCP Server. OS inspection then reported zero listening connections on
port 9876. Native `get_objects_summary` failed with the expected cannot-connect response for
`127.0.0.1:9876`. The stdio bridge remaining available in Codex does not imply that Blender's
socket server is running. Subsequent restart/reconnection and reversal results follow below.

## Restart And Reversal Results

- Owner manually restarted the server. OS inspection again found only `127.0.0.1:9876`
  (PID 66484); native object inventory succeeded through the existing Codex connection without
  restarting Codex or Blender. All four saved pilot objects remained present after reconnection.
- Removed only the tagged `MCPPilot_OneMetreCube` and its now-unused mesh. The reviewed recipe
  checked the active pilot path, clean state, expected object inventory, ownership tag and dimensions
  before removing anything. Recipe: `.local/blender-pilot/remove_connectivity_cube.py`.
- Saved and reopened the pilot with UI loading and embedded scripts disabled. Subsequent native
  inventory confirmed only Camera, Cube and Light. Clean saved state and Auto Start false were
  reconfirmed; raw result is `runs/connectivity-01/native-removal-reopen-result.json` under the
  local pilot folder. Original baseline hash remained unchanged at the restart inspection.
- Reversal covers the added object/mesh. The pilot retains its metric display settings; it is not
  a byte-for-byte restoration of the separate baseline. Local pilot files and backups remain as
  evidence at this checkpoint; no claim of disk cleanup or final handoff acceptance is made.

## Approved Interactive Auto-Start — 2026-10-23

- Owner visually confirmed the smaller cube was gone, then approved and enabled Blender Auto Start
  and restarted Blender. This supersedes the initial on-demand-only pilot setting; an additional
  final stop is not required by the retained workflow. The earlier manual stop/reconnect proof stands.
- Post-restart OS inspection found only `127.0.0.1:9876`, now owned by PID 73200, compared with
  PID 66484 before the owner-reported restart. Native scene queries succeeded through the existing
  Codex bridge. Connected settings reported Blender 5.2.3 LTS, Auto Start true, host `127.0.0.1`,
  port 9876 and online access true.
- Restart opened a clean unsaved default scene containing Cube, Camera and Light; the pilot file
  was not automatically reopened. No scene changes were made during this verification.
- Auto-start applies to the add-on in the Blender application session, not a Windows service.
  Codex launches its separate local stdio bridge. Existing tool restrictions and reviewed-code
  boundaries remain unchanged; loopback binding does not sandbox Python execution.

## Handoff And Storage Proof

The [handoff results](phase-3-1-blender-handoff-results.md) now record passed export/import,
pivot/orientation/collision, deliberate reimport and owner-run player passage checks.
[Published asset recovery](phase-3-1-recovery-results.md) also passed; the temporary checkout was
deleted. The [3.1 closeout review](../phase-3-1-closeout.md) records acceptance and closure.

The accepted local permission tradeoff remains in force. Generated Python is reviewed for each
bounded task; no source media, credentials, external asset services, desktop control or ship
production is included. Setup and test results will be added here as observed.
