# Guided Unreal Project Setup — Phase 2.2

Status: Phase 2.2 fully closed; closeout accepted 2026-10-23 and file recovery verified.
The [closeout proposal](../implementation/phase-2-2-closeout.md) records disabled Android file-server
settings and the cleared token. Publication and fresh-clone file recovery are verified for `49511af`;
retrieved-map editor opening belongs to Phase 2.3 and the handoff fixture to Phase 3.1, not open 2.2 work.
The [implementation plan](../implementation/vertical-slice-1-implementation-plan.md#phase-22-project-skeleton-and-repository-boundary)
owns scope and completion. These instructions are a guide, not evidence that steps have been performed.

## First Stop: The Project Browser

1. Open Epic Games Launcher and select the Unreal Engine Library. Launch the installed UE 5.8 engine;
   installed file evidence identifies 5.8.4 even though launcher metadata previously named 5.8.3.
2. Wait for the Unreal Project Browser, where new-project categories/templates are shown. If an
   existing-project screen appears, use its new-project option to reach template selection.
3. Review the visible options before creating anything. Choose Games, Blank and C++ for the accepted
   skeleton. Do not enable MCP/plugins or select a character template.

The planned parent location is `D:\Repos\Outlaw-Star-Game\Unreal` and project name is
`OutlawStarSim`. The resulting descriptor must be
`D:\Repos\Outlaw-Star-Game\Unreal\OutlawStarSim\OutlawStarSim.uproject`.
Check the wizard's effective path to avoid a duplicated project-name folder. Confirm any additional
visible quality/ray-tracing/starter-content choices against the bounded foundation before Create;
do not interpret template defaults as measured rendering decisions.

## Creation Observations And Remaining Guided Steps

The repository owner completed the Games Blank C++ wizard with Desktop/Maximum settings. Files
confirm `OutlawStarSim.uproject` at the accepted path, engine association 5.8 and one OutlawStarSim
runtime module plus game/editor targets. The template enabled ModelingToolsEditorMode; subsequent
repository-owner installation added the project-local Microsoft VisualStudioTools **2.8** plugin.
Its inspected descriptor declares editor modules on Win64; screenshot evidence shows the version
detected and Test Adapter green, not a completed test run. No MCP entry was added. The Basic level
is saved as `Content/XGP/Development/L_NeutralProof.umap` (49,070 bytes at inspection). Screenshots
show its floor, sky/lighting and All Saved status. Saved `DefaultEngine.ini` selects
`/Game/XGP/Development/L_NeutralProof.L_NeutralProof` for both EditorStartupMap and GameDefaultMap.
Default-map relaunch and runtime proof remain pending, as does Phase 2.2 closeout.

Generated defaults include DX12, Lumen methods, Virtual Shadow Maps and ray-tracing settings. These
are configuration observations, not proof of effective rendering, final quality approval or performance.
The wizard opened Visual Studio and the editor was reported opening; no separate 2.3 build/relaunch
check was run. Preserve creation logs as incidental evidence rather than declaring T03 passed.

The generated `.vsconfig` initially listed SDK 22621 and Clang; component queries identified those
as its only unmatched entries. During 2.2 the project manifest was aligned with the selected MSVC
baseline by removing the Clang suggestion and replacing SDK 22621 with SDK 26100. No installed tools
were changed by that manifest edit. Engine
project-file regeneration may recreate generic suggestions, so review any regenerated manifest rather
than changing the installed engine's shared policy. Setup-page suggestions are not permission to
enable MCP or import all offered components.

Initial IDE checks showed incomplete naming, HLSL, background integration and UBT configuration.
The guided follow-up below resolved those indicators; the final screenshot shows green overall
configuration. The repository owner reports good status after restarting Visual Studio.

### Project-Scoped C++ Naming Rules

Added `Unreal/OutlawStarSim/.editorconfig` during 2.2 using Microsoft's Unreal naming sample retained
with VisualStudioTools 2.8. It applies only to `Source/**/*.{cpp,h,hpp,inl}`: actor/UObject/Slate
prefixes A/U/S, struct/enum/template prefixes F/E/T, boolean b and general PascalCase. This is the
sample's supported naming coverage, not enforcement of every Epic coding convention. It does not
reformat existing code or add C# rules, and the vendor plugin's own configuration remains untouched.
Property names/references were checked for consistency; screenshots confirm IDE recognition at
Suggestion. Actual code diagnostics remain untested. No build is needed
to refresh its configuration status. Do not press Add to create a competing naming file.

The integration background checkbox was enabled during guided setup. The installed plugin includes
a background VSServer commandlet using local named-pipe
communication for the VS test integration. This can keep an additional Unreal helper process active;
it is separate from MCP and does not by itself demonstrate that tests ran. Subsequent screenshots
confirm the green status. No background helper was launched by Codex in preparing these rules.

HLSL configuration can be reviewed as a separate small IDE setup step if desired; shader-editing
support is not a gameplay/rendering requirement or an authorization to author shaders. Inspect its
actual configuration action/output before selecting include paths or preprocessor definitions.
The repository owner applied the UBT page's 49,152-character include-path setting with solution
regeneration. Inspection confirms `VCProjectFileGenerator/MaxSharedIncludePaths=49152` in the
user-wide `%APPDATA%\Unreal Engine\UnrealBuildTool\BuildConfiguration.xml`, overriding the inspected
engine default of 24,576 for generated IDE shared include paths. This does not change compiler
selection or simulation behavior. Overall configuration became green and Visual Studio was restarted.
This host setting can affect other Unreal projects; it is not a shared project requirement.

Subsequent screenshot evidence confirms Naming Checker green at Suggestion, and integration v2.8
green with background mode checked. That is configuration-status evidence, not a test/compile pass.
The HLSL Configure action selected the project root and generated `shadertoolsconfig.json` with empty
definition/include/mapping collections. Corrected a leading space in the generated include-directory
property name; JSON parsing/property checks pass. Actual HLSL diagnostics remain untested, and no
custom shaders, guessed include mappings or engine-specific host paths were added.
Subsequent screenshot evidence confirms HLSL configuration green.

The remaining installer prompt identified .NET Compiler Platform SDK. The repository owner completed
that installation; subsequent screenshots show the banner absent. This separate IDE recommendation
does not invalidate the selected MSVC/Windows SDK baseline.

An incidental AutomationTool C# restore failed with NU1101/NU1102 while searching offline/local
sources only. The repository owner added enabled `nuget.org` (`https://api.nuget.org/v3/index.json`)
and retried Restore NuGet Packages. The saved user NuGet configuration contains that source;
screenshot output reports restore finished. This is not C++ build validation.

Windows opened `.uproject` in Visual Studio; association repair was reported unsuccessful and remains
unresolved. Direct UnrealEditor invocation with the descriptor reached a rebuild prompt for
VisualStudioTools and VisualStudioBlueprintDebuggerHelper. The subsequent editor screenshots
establish successful opening after that prompt, not a separately audited plugin build.

To bypass the unresolved Windows association, run this in PowerShell from the repository root:

```powershell
& 'D:\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor.exe' (Join-Path (Get-Location) 'Unreal\OutlawStarSim\OutlawStarSim.uproject')
```

The executable path is host-specific; the descriptor path is repository-relative. Independent
non-Live-Coding build instructions and execution evidence belong to Phase 2.3.

For the later authorized Phase 2.3 check, the ordinary target is `OutlawStarSimEditor`, Win64,
Development, with the editor closed. The installed build entry point exists. From the repository
root, the proposed command is:

```powershell
& 'D:\Epic Games\UE_5.8\Engine\Build\BatchFiles\Build.bat' OutlawStarSimEditor Win64 Development '-Project=D:\Repos\Outlaw-Star-Game\Unreal\OutlawStarSim\OutlawStarSim.uproject' -WaitMutex
```

This recipe has not been executed as independent validation. Phase 2.3 must capture its exit status,
actual compiler/SDK selection and complete local log, then perform the accepted repeated editor/input
observations. Do not use Build Solution on the generated engine/tool projects as a substitute.

References: [Microsoft naming checker](https://learn.microsoft.com/en-us/cpp/ide/lnt-naming-convention)
and [sample rules](https://github.com/microsoft/vc-ue-extensions/blob/v2.8/Source/.editorconfig).

Creating a C++ project may automatically generate IDE files, compile initial code and open the editor.
Record that outcome and any errors as creation evidence; it does not replace Phase 2.3's independent
non-Live-Coding build and repeated editor proof. Do not start those later checks automatically.

After creation, inspect the actual descriptor, Config and Source/module files. In the editor, create
and save the small neutral fixture as `Content/XGP/Development/L_NeutralProof.umap`, following the
guided steps appropriate to the visible editor. No ship geometry, player/gameplay implementation,
production art or extra template assets are needed. Do not create TestLab/Awakening merely because
their names are reserved.

## Repository Boundaries

Repository preparation performed 2026-10-23: added scoped root `.gitattributes` rules and ran
`git lfs install --local` successfully. `git check-attr` verified intended LFS treatment for
representative direct/nested owned asset paths and ordinary treatment for C++/protected sources;
`git check-ignore --no-index` verified representative source-media/cache/output exclusions. These
were path-policy checks, not created test assets. No LFS assets were staged, uploaded or retrieved.
Project generation and content audit are recorded in the closeout. Publication and fresh-clone map
recovery subsequently passed; VS1-T02 still awaits retrieved-map editor observation.
Generated `.slnx` files, like `.sln` files, are excluded from source publication; `.vsconfig` is
retained for review of its suggested-component contract rather than imported automatically.

The root `.gitattributes` applies LFS to owned `.blend` sources under `assets/blender/`, designated
`.fbx` handoffs under `assets/exports/`, and `.uasset`/`.umap` files under the project Content folder.
Source/configuration/documentation use ordinary Git. Existing ignore rules exclude Unreal generated
Binaries/Intermediate/Saved/DDC, personal workspace files and protected reference media. Keep temporary
exports and future package outputs in ignored `.local/` working locations rather than designated exports.

Actual new files need an attribute/ignore and intended-diff review. Do not force-add source media or
generated caches. Confirmation is required before publishing project assets; review any paid LFS
usage before incurring it. Fresh-clone payload retrieval passed for the published neutral map;
observed opening of a retrieved copy remains pending. Rules alone cannot prove recovery.

## Stop Boundary And MCP Sequence

Phase 2.2 ends with the reviewed skeleton, saved neutral map, repository policy and concise setup
record. Document actual outcomes and untested parts before closeout. No automatic transition into
2.3, plugin enablement or MCP registration follows.

Unreal MCP's optional local pilot follows ordinary **2.3** build/editor proof. Blender MCP's pilot
follows the **3.1** player/scale fixture and precedes repeated ship modeling. Both require their own
bounded setup scope under the [editor-automation contract](../architecture/editor-automation.md).
