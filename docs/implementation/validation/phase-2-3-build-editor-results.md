# Phase 2.3 — Build And Editor Results

| Field | Value |
| --- | --- |
| Started | 2026-10-23 |
| Baseline | `main` at `23ace3f`, clean before the first build |
| Status | Ordinary 2.3 proof and optional Unreal MCP pilot passed; closeout accepted 2026-10-23 |
| Scope | Phase 2.3 ordinary proof and subsequent optional Unreal MCP pilot requested; no 2.4 |
| Scenarios | VS1-T03; effective-selection corroboration for VS1-T01 and retrieved-map observation for VS1-T02 |
| Performers | Codex: command-line build and log inspection; repository owner: guided editor/input observations |

## First Build

No UnrealEditor/UnrealEditor-Cmd process was found in the pre-build check. From the repository root:

```powershell
& 'D:\Epic Games\UE_5.8\Engine\Build\BatchFiles\Build.bat' OutlawStarSimEditor Win64 Development '-Project=D:\Repos\Outlaw-Star-Game\Unreal\OutlawStarSim\OutlawStarSim.uproject' -WaitMutex -NoHotReloadFromIDE
```

Output was captured with Tee-Object; the native exit code was preserved. Result: **Succeeded, exit 0**,
10.42 s reported execution time. Four actions compiled `OutlawStarSim.cpp`, linked the project library
and DLL, and wrote target metadata. This is actual project compilation, not merely an up-to-date result
or Live Coding. Plugin files did not require recompilation in this invocation.

The log selects **MSVC 14.50.35739** from family directory `14.50.35717` under the installed VS 2026
instance, and **Windows SDK 10.0.26100.0**. The wrapper reports the engine-bundled **DotNet 10.0 win-x64**;
that output alone does not identify a .NET patch version. No compiler/SDK override was added.

Local logs, ignored from Git:

- `.local/validation/phase-2-3/build-first.log`: full captured wrapper/build output.
- `.local/validation/phase-2-3/ubt-first.log`: copied UBT diagnostic log before later runs can replace it.

No warning/error diagnostic was found in the targeted first-build log review. Build success is not
editor, runtime input, package or performance acceptance.

## Ordinary Proof Summary

- Primary checkout: startup, editor navigation and Play In Editor input/exit observed.
- Fresh published checkout: retrieval, independent build, map opening and Play input/exit passed; logs preserved and temporary clone deleted.
- Repeat build and primary reopening/Play input passed.
- The optional Unreal MCP pilot subsequently completed; see its record and the [closeout proposal](../phase-2-3-closeout.md).

## Primary Editor Startup

The repository owner reports that direct project launch opened `L_NeutralProof` and that mouse-look
and WASD editor-camera navigation worked. The current startup log independently records the intended
map load, engine 5.8.4, project VisualStudioTools mount and D3D12/SM6 selection. This is editor
navigation, not player/game input or performance acceptance.

The targeted log review found no Error/Fatal entries. Warnings report editor-layout migration
(the log says the layout key was updated) and failed DNS resolution for Epic's datarouter telemetry
endpoint. Neither prevented the observed map opening; no network or layout settings were changed.
A startup-log snapshot is retained locally as `.local/validation/phase-2-3/editor-first-startup.log`.
The repository owner subsequently confirms Play In Editor mouse-look/WASD worked and Esc returned
cleanly to editing. The log records the intended PIE world, GameModeBase, start and teardown, with
no Error/Fatal entries in the targeted review. Snapshots are retained as `editor-first-play.log`
and, after reported editor closure, `editor-first-closed.log` under the same local evidence folder.

## Repeat Build And Recovery Preparation

The repository owner confirmed Unreal closed; a process check found no editor process. The same
ordinary Build.bat command ran in a fresh shell/process and returned **Succeeded, exit 0**, target
up to date, zero build actions, 1.04 s reported execution time. This repeat does not substitute for
the first run's real compile. Logs: `build-repeat.log` and `ubt-repeat.log` in the local evidence folder.
The repository owner confirms the repeated launch opened the correct map, Play movement worked,
Esc returned to editing, and Unreal was then closed. Process inspection confirms no editor remains.
`editor-repeat-closed.log` preserves this session: the primary map load, GameModeBase PIE startup
and teardown are recorded, with no Error/Fatal entries in the targeted review. The primary repeat
build/open/input check is complete.

A fresh remote clone was prepared at `.local/recovery-editor-23ace3f` for the later editor observation.
Its neutral map is 49,070 bytes and matches the recorded SHA-256. No source, map or compiled binaries
were copied from the main checkout. Recovered-copy editor observations and cleanup are recorded below.

The recovered checkout is at published revision `23ace3fb507af8023e83f264a27d2f5f61713846` and
had a clean worktree before its build. The same target/configuration command, with `-Project` pointing
inside that clone, passed with **exit 0**, 25 actions and 62.90 s reported execution time. It compiled
the project and both VisualStudioTools editor modules from the recovered source. Effective toolchain
remained MSVC 14.50.35739/family 14.50.35717 and SDK 10.0.26100.0. No build Error/Warning diagnostics
were found in the targeted UBT log review. Logs are preserved outside the clone as `build-recovered.log`
and `ubt-recovered.log` in the local evidence folder.

## Recovered Editor Observation And Cleanup

The repository owner confirms the recovered copy opened the intended map, mouse-look/WASD worked
in Play, Esc returned to editing and Unreal was then closed. The preserved
`editor-recovered-closed.log` independently identifies the map inside `.local/recovery-editor-23ace3f`,
GameModeBase PIE startup/teardown and orderly editor exit. No Error/Fatal entries were found in the
targeted review. Warnings concern the same editor-layout migration and Epic datarouter DNS/outstanding
telemetry request at shutdown; no project/module/asset load failure was identified.

After opening, the recovered map still matches the recorded SHA-256. No Unreal editor process remained.
The complete temporary clone was removed with native PowerShell after verifying the resolved exact
path beneath the workspace and absence of ancestor reparse points. An existence check confirms it
is gone. Build/editor logs remain only in the main checkout's ignored local evidence directory.

Ordinary VS1-T03 proof and the VS1-T02 retrieved-map editor corroboration have passed for this neutral
fixture. Effective compiler/SDK selection is corroborated; packaging remains untested. On completion
of these observations, the repository owner explicitly deferred closeout preparation to pursue the
optional Unreal MCP pilot. No MCP installation, project enablement or connection has yet occurred.
That was the pre-pilot checkpoint; subsequent enablement, native connection and results are recorded
in [the completed pilot record](phase-2-3-unreal-mcp-pilot.md).
