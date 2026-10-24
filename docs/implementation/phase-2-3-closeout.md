# Phase 2.3 — Build, Editor And Unreal MCP Closeout

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Baseline | `main` at `23ace3f`, plus uncommitted 2.3 records and owner-enabled MCP project plugins |
| Status | Phase 2.3 closeout accepted 2026-10-23; publication authorized; no 2.4 authorization |
| Scope | Reproducible Development Editor build/open, recovered-map validation and selected local Unreal MCP pilot |
| Evidence | [Build/editor results](validation/phase-2-3-build-editor-results.md), [MCP pilot](validation/phase-2-3-unreal-mcp-pilot.md) |

## Results

| Check | Result / evidence |
| --- | --- |
| Primary C++ build | Passed, exit 0, 10.42 s; actual project compile/link outside Live Coding |
| Effective compiler/SDK | MSVC 14.50.35739, family directory 14.50.35717; Windows SDK 10.0.26100.0 |
| Repeat build | Passed in a fresh process after editor closure, exit 0; target correctly up to date |
| Primary editor/input | Owner confirmed correct map, editor navigation, Play mouse-look/WASD and Esc return; repeated after reopening; logs corroborate startup/teardown |
| Recovered checkout | Fresh GitHub checkout of `23ace3f` built independently, exit 0, 25 actions, including project and VS plugin modules; owner confirmed map and Play input/exit |
| Recovery cleanup | Both recovery checkouts fully deleted after logs were preserved outside them |
| Native MCP | Codex discovery, scene inspection, bounded cube placement, save/reload, owner visual observation and stop/reconnect passed |
| Reversal | Cube removal persisted after reload; disposable pilot folder removed; original map SHA-256 unchanged |
| Final manual shutdown | Editor exited, no port-8000 listener, endpoint connection refused |
| Approved auto-start | Owner enabled the project-user preference and restarted; saved True, no launch start flag or manual-start command, startup log and OS query confirm 127.0.0.1:8000; native query reads L_NeutralProof |

Build durations are diagnostic observations, not performance benchmarks. The wrapper identifies
bundled .NET 10.0 win-x64; a patch version is not claimed from that output.

## MCP Disposition

Recommend retaining the engine-shipped ModelContextProtocol and EditorToolset plugins for local
editor work. The owner-approved auto-start preference applies to this project's interactive editor
sessions. The host-local Codex connection is Git-ignored; no unrelated/global configuration changed.
Server exposure remains loopback-only. The server is currently running with the reopened editor,
as intended; closing the editor releases it. StopServer removes MCP routes but leaves Unreal's shared
HTTP listener until editor exit, so HTTP 404 is the verified route-stop result rather than port closure.

Recorded limitations remain visible: a target-dirty load guard, CaptureViewport optional-argument
handling failure, and asset-folder deletion requiring a scoped filesystem fallback. An initial cube
was placed in the wrong active map after a failed load; it was immediately removed without saving
the original. Later mutations checked each dependent result. All final scene changes were reversed.
No general correctness claim is made for untested toolsets or arbitrary scripting.

The manual editor/file workflow remains the fallback. No Computer Use was performed. MCP is a
development integration, not a runtime game requirement. Packaged operation without the server,
and exclusion/disablement of development automation, remain Phase 2.4 work.

## Validation And Remaining Boundaries

- VS1-T03 ordinary build/editor/repeat proof passed for the neutral fixture.
- VS1-T02 retrieved-map editor corroboration passed for the published pre-MCP baseline `23ace3f`.
  This does not claim fresh-clone recovery of the currently uncommitted MCP configuration.
- VS1-T01 effective-selection evidence is corroborated by actual editor builds; packaging corroboration remains at 2.4.
- VS1-T04 and Phase 2 exit remain open. No packaging, ship/player implementation, Blender pilot or performance acceptance occurred.

Raw logs and protocol responses stay under ignored `.local/validation/phase-2-3/`; authored summaries
are versioned. The original map remains 49,070 bytes with SHA-256
`1dc38b4e2ee6cf16c0af7e122d8615a677ce9b805774388ebf44231d0b5d1b43`.
No temporary recovery or pilot-content folder remains.

## Accepted Gate

The scoped 2.3 results and retention of the bounded local Unreal integration were accepted on
2026-10-23, including documented limitations and host-local auto-start. No 2.3 tasks remain open.
Publication is authorized. Phase 2.4 remains unstarted and unauthorized; its walkthrough is informational.
