# Phase 2.4 — Neutral Standalone Package Results

| Field | Value |
| --- | --- |
| Started | 2026-10-23 |
| Baseline | `main` at `9a4b633`, clean before 2.4 changes |
| Status | Build/package, audit and first/repeat standalone observations passed; closeout accepted 2026-10-23 |
| Scope | Explicitly authorized Phase 2.4 only; no later phase execution |
| Scenario | VS1-T04; package corroboration for toolchain and development-automation boundaries |
| Performers | Codex: configuration, command-line packaging and log/artifact review; owner: guided executable launch/input/exit/relaunch |

## Configuration And Recipe

Unreal was closed by the owner and no editor process was found. Installed RunUAT.bat is available.
Project plugin references now restrict ModelingToolsEditorMode, VisualStudioTools, ModelContextProtocol
and EditorToolset to Editor targets. Installed UBT PluginReferenceDescriptor supports TargetAllowList;
this preserves editor tooling while excluding those explicit references from the Game target. Actual
build/staging/runtime evidence must still verify exclusion; configuration alone is not proof.

DefaultGame.ini selects Development, Pak/IoStore, standard prerequisites and only the neutral map.
Cook-all is off. The package will use Win64 Development with `L_NeutralProof` and required dependencies.
No installer runs automatically; missing prerequisites require review. This is primary-host proof,
not a clean-PC compatibility claim or release/distribution approval.

Attempt 01 runs from the repository root:

```powershell
& 'D:\Epic Games\UE_5.8\Engine\Build\BatchFiles\RunUAT.bat' BuildCookRun '-project=D:\Repos\Outlaw-Star-Game\Unreal\OutlawStarSim\OutlawStarSim.uproject' -noP4 -platform=Win64 -clientconfig=Development -build -cook '-map=/Game/XGP/Development/L_NeutralProof' -stage -pak -iostore -package -archive '-archivedirectory=D:\Repos\Outlaw-Star-Game\.local\packages\phase-2-4\attempt-01' '-stagingdirectory=D:\Repos\Outlaw-Star-Game\.local\packages\phase-2-4\stage-01' -prereqs -unattended -utf8output -nocompileeditor
```

Full output is captured to ignored `.local/validation/phase-2-4/package-attempt-01.log` with the
native exit code preserved. The executable/content set and manifests were audited before owner launch.
Logs/packages stay out of source publication. Outcomes are recorded below.

## Attempt 01 Progress

The Game target compiled and linked successfully: 11 actions, result Succeeded, build-tool exit 0,
59.95 s reported build time. Effective selection remained MSVC 14.50.35739/family 14.50.35717 and
SDK 10.0.26100.0. The generated target receipt identifies Win64 Development and contains no matching
runtime-dependency paths for ModelContextProtocol, EditorToolset, ToolsetRegistry or VisualStudioTools.
The receipt check is corroborated by the staged-content and runtime checks below.
Cook completed in UnrealEditor-Cmd for Windows and the selected neutral map; its summary reports
0 errors and 0 warnings. The first pass compiled cold SM5/SM6 shaders under existing template settings.
Some engine startup Display messages mention unavailable non-Windows SDKs; Windows cooking succeeded
without installing those platforms. No broad renderer/plugin cleanup was introduced to suppress them.

Staging initially encountered connection refusal from the local Zen cooked-data store; UAT's readiness
retry restarted/sponsored the service and completed. This automatic recovery is recorded rather than
claimed as a warning-free pipeline. The archived package uses local Pak/IoStore containers, not a
cook-on-the-fly launch. Runtime checks below corroborate local-container loading without editor/MCP.

Final result: **BUILD SUCCESSFUL, AutomationTool exit 0**, BuildCookRun time 263.03 s, approximately
4m28s total AutomationTool time. Build, cook, stage, package and archive each completed. The output is
`.local/packages/phase-2-4/attempt-01/Windows`, 50 files totaling 1,101,192,610 bytes at audit.
Prerequisite redistributable executables are included; none were run.

## Artifact And Dependency Audit

The archived root contains the bootstrap OutlawStarSim.exe and the game executable under
`OutlawStarSim/Binaries/Win64/OutlawStarSim.exe`, plus Pak/IoStore content. SHA-256 values:

- Bootstrap: `db344f9cca1c4fb3047f146e93eee5e0c473acb726f21f739039bcb5e7471fc6`.
- Game: `41e35fea7102dc8de7181ec8041084781ed720eb41d34b7b895d8f93fc01b1f8`.

Stage manifests contain the project neutral map and Engine/Maps/Entry, with no other project map
identified. Game target receipt BuildPlugins/runtime paths, staged filesystem, UFS/NonUFS manifests
and successful UnrealPak listing show no matching ModelContextProtocol, EditorToolset, ToolsetRegistry,
VisualStudioTools, immutable source-media, extracted-frame or MCPPilot paths. This is manifest/path
audit evidence, not a claim that binary debug strings contain no build paths.

Preserved local evidence: `ubt-game.log`, `stage-ufs.txt`, `stage-nonufs.txt` and `pak-list.txt` alongside
the complete packaging log. Before owner launch, OS checks found zero editor processes and zero
port-8000 listeners. No unrelated Zen/cache service was stopped to create an artificial clean host.

## First Runtime Check

Launch the archived bootstrap from its Windows output directory with `-windowed -ResX=1280 -ResY=720`
and `-abslog=D:\Repos\Outlaw-Star-Game\.local\validation\phase-2-4\runtime-first.log`.
The small window is for convenient smoke testing, not a change to the 1440p acceptance target.
Observe floor/sky startup, click into the window, test mouse/WASD and exit via Alt+F4 or window close.
No game-menu/Esc-exit feature is assumed from the editor's Esc behavior. Inspect the first log before
relaunching with a separate second log.

The owner reports correct floor/sky startup, mouse-look/WASD response and Alt+F4 exit. The preserved
`runtime-first.log` corroborates UE 5.8.4 Development startup, D3D12/SM6, the intended neutral map,
GameModeBase, world startup and orderly game-engine exit. Targeted review found zero Warning/Error/Fatal
entries and no ModelContextProtocol, EditorToolset, ToolsetRegistry or VisualStudioTools loading entries.
No game/editor processes remained after exit. This first primary-host runtime check passed.

The owner confirms accepting multiple Windows Firewall/network-access prompts during first launch.
Exact program names, network profiles and resulting rules were not captured, so the prompts are not
attributed to a specific subsystem. Codex did not edit firewall settings or run prerequisite installers.
Do not claim this is evidence of clean-PC or network-isolated operation.

## Repeat Runtime Check

The owner launched the same archived bootstrap again with identical window/input settings and
`-abslog=D:\Repos\Outlaw-Star-Game\.local\validation\phase-2-4\runtime-repeat.log`.
The owner confirms floor/sky startup, mouse-look/WASD and Alt+F4 exit worked again, with no further
firewall prompts. This session did not require opening Unreal Editor or starting MCP.

The 94,093-byte repeat log records local global/project IoStore containers and the project Pak mount,
the intended neutral map and GameModeBase startup, and orderly game-engine exit. Targeted review
found zero Warning/Error/Fatal entries and no MCP/editor-tool names. After exit there were zero
game/editor processes and zero port-8000 listeners. The original map's SHA-256 remains unchanged.

VS1-T04 passes for the agreed primary-host neutral fixture. Actual Game-target MSVC/SDK selection
corroborates VS1-T01, and package independence from the adopted MCP integration is verified within
this test scope. This is not clean-PC portability, network-isolation, performance or full-slice acceptance.

Generated Build/Windows/FileOpenOrder logs are narrowly ignored; authored Build resources are not
blanket-excluded. The archived package, staging output and local evidence remain ignored working
artifacts. No packaged binaries, raw logs or source media belong in the publication set.
