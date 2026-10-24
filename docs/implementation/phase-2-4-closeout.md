# Phase 2.4 — Standalone Package Closeout

| Field | Value |
| --- | --- |
| Prepared | 2026-10-23 |
| Baseline | `main` at `9a4b633` plus the uncommitted 2.4 packaging boundary/settings and result records |
| Status | Phase 2.4 closeout accepted 2026-10-23; publication authorized |
| Authority | [Phase 2.4](vertical-slice-1-implementation-plan.md#phase-24-early-standalone-package-smoke), VS1-T04 |
| Evidence | [Detailed commands, artifact identities and observations](validation/phase-2-4-package-results.md) |

## Results

- Win64 Development Game compilation, cook, stage, package and archive completed with AutomationTool
  exit 0. Actual build selection was MSVC 14.50.35739/family 14.50.35717 and SDK 10.0.26100.0.
- The package contains the intended neutral project map, Engine Entry and required runtime content.
  Manifest/filesystem/archive review found no protected reference media or disposable pilot content.
- Editor tooling references are limited to Editor targets. The Game receipt, staged paths and archive
  listing contain no matching MCP/EditorToolset/ToolsetRegistry/VisualStudioTools dependencies.
- The owner ran the archived executable twice from its separate output directory with the editor and
  MCP stopped. Floor/sky, mouse-look/WASD and Alt+F4 exit worked both times. Both logs show local
  Pak/IoStore mounting, the expected map and orderly shutdown, with zero Warning/Error/Fatal entries.
- After the repeat, no game/editor process or MCP listener remained. The original neutral-map file
  remains 49,070 bytes with its previously recorded SHA-256.

## Dispositions And Limits

Staging hit a local Zen connection refusal; UAT's readiness retry recovered and completed. No
manual cache/service changes were needed. Cook's final summary reported zero errors/warnings.
This successful attempt is not represented as a pipeline with no intermediate recovery events.

The owner accepted Windows Firewall/network-access prompts on first launch; none appeared on repeat.
Exact programs/profiles/rules were not captured. No firewall rules or prerequisite installers were
changed/run by Codex. Included redistributables were not invoked. Installed host tools remain present;
this is bounded primary-host proof, not a clean-PC or network-isolation test.

The package is a Development neutral fixture, not a release build, completed slice or performance
benchmark. Test resolution 1280×720 was for a convenient window and does not revise the accepted
1440p target. No new player/gameplay behavior was implemented.

## Repository And Artifact Boundary

The intended change set contains project plugin TargetAllowList restrictions, DefaultGame packaging
settings, a narrow FileOpenOrder ignore rule and authored setup/status/result documentation.
All package/staging/log artifacts remain under ignored working paths; local Codex settings remain ignored.
The retained archive is `.local/packages/phase-2-4/attempt-01/Windows`; its recipe and executable hashes
are in the result record. Generated output is reproducible and is not intended for Git publication.

Keep editor/MCP access for development through the Editor target. Ordinary standalone package
operation requires neither service; future plugin changes must preserve this boundary. On a failed
future rebuild, preserve logs and diagnose the affected content/build setting before replacing outputs.
Do not overwrite protected references or add source media to fix a dependency.

## Accepted Gate

Scoped 2.4 package and repeated primary-host runtime proof were accepted on 2026-10-23, with
publication authorized. All 2.4 tasks are complete. VS1-T01 package corroboration and VS1-T04 evidence
are available for the separately requested Phase 2 exit review. No Phase 3, Blender pilot or other
later execution is authorized.
