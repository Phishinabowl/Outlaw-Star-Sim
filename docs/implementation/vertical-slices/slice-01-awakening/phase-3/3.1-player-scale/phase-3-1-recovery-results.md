# Phase 3.1 — Published Asset Recovery Results

| Field | Value |
| --- | --- |
| Date | 2026-10-24, America/New_York |
| Published revision | `6b2de6f7173f9c197da309ce5e62c44e0fab2d04` |
| Status | Passed; temporary recovery checkout deleted |
| Scope | Published LFS payload retrieval, recovered Blender source/export and Unreal fixture/import proof on the primary host |

## Retrieval And Identity

A fresh single-branch clone of `https://github.com/Phishinabowl/Outlaw-Star-Sim.git` checked out
the exact published revision under `.local/recovery/phase-3-1/checkout`. No source media or primary
checkout binaries were copied into it. Git LFS fsck passed; all 12 LFS files had retrieved payloads
rather than unresolved pointers. This includes the 11 new designated binary files and the existing
neutral map. Each recovered payload's SHA-256 matched the primary published working copy before
any regeneration. Inventory: `.local/validation/phase-3-1/recovery-payload-hashes.json`.

## Recovered Blender Source And Recipe

Blender 5.2.3 LTS opened the recovered `.blend` in a separate background process with factory
startup and automatic file scripts disabled. Checks found all eight expected render/collision
objects, metric/unit scale 1, correct cube/flap/frame dimensions and assembly origins, and a UV
layer on each render mesh. Source-file hash remained unchanged.

The recovered export recipe regenerated all three FBX files only inside the temporary checkout,
demonstrating that its root is derived from the opened source rather than the primary path.
Source/bootstrap/revision helpers likewise retain explicit or source-relative root handling.
Regenerated FBX byte identity is not asserted; imported geometric results were checked instead.
Result: `.local/validation/phase-3-1/recovery-blender-result.json`. Background process exited 0.

## Recovered Unreal Fixture And FBX Import

The recovered checkout built its own `OutlawStarSimEditor` module and project plugin binaries:
29 build actions, exit 0, 98.16 seconds, MSVC 14.50.35739 / SDK 10.0.26100.0. Its own module was
needed to resolve native fixture classes in L_TestLab; the primary project's DLL was not reused.
Log: `.local/validation/phase-3-1/recovery-editor-build.log`.

A separate NullRHI commandlet opened the recovered saved meshes/materials and L_TestLab using
the published verifier. It checked dimensions, UV channels, one/one/three collision hulls, cube
marker material references, scale-1 placements and the neutral-map hash. It then imported the
FBX files regenerated from the recovered Blender source into temporary in-memory packages using
the same legacy FbxFactory/FbxImportUI path. Local bounds confirmed units, axes and pivots:

| Asset | Imported bounds, cm | Hulls |
| --- | --- | --- |
| Cube | X -25..75, Y -40..60, Z 0..100 | 1 |
| Revised flap | X -6..6, Y 0..100, Z 0..100 | 1 |
| Frame | X -10..10, Y -70..70, Z 0..220 | 3 |

The commandlet exited 0 with zero reported errors/warnings. Results/log:
`.local/validation/phase-3-1/recovery-unreal-result.json` and `recovery-unreal-open.log`.
Reviewed probe scripts remain beside those records. Primary interactive Blender/Unreal sessions
were not controlled or replaced. No installations, MCP registration or project configuration changes
were needed in the recovered checkout; PythonScriptPlugin was enabled only for the commandlet process.

## Cleanup And Evidence Limits

After both recovery processes exited, cleanup verified the exact resolved checkout path stayed
within the owned recovery directory, no reparse points existed, and no matching recovery processes
remained. Removed the entire checkout and its empty phase directory; verified checkout absence.
The path/process/size check is retained in `recovery-cleanup-check.json` in the primary evidence folder.

An optional final sandboxed Git status query in the temporary copy failed to start Git LFS's shell
filter process (MSYS access denied). It is not counted as a passed status check; retrieval integrity,
payload hashes and application checks had already passed. The disposable checkout was then removed.

This is recovery/handoff proof on the existing primary host. It does not repeat interactive Play,
owner visual/capsule observations, package/performance acceptance or clean-PC validation. Those
claims retain their own earlier evidence and later checkpoints. No Phase 3.2A work was performed.
