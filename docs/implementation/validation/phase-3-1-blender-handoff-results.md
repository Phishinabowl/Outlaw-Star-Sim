# Phase 3.1 — Blender To Unreal Handoff

| Field | Value |
| --- | --- |
| Date | 2026-10-24 |
| Status | Local handoff/reimport, owner visual/traversal and published recovery checks passed |
| Scope | Owned cube, hinged flap and doorway frame in L_TestLab; no ship geometry or 3.2A |
| Authority | [Handoff contract](../phase-1-4-architecture-asset-validation-draft.md#accepted-blender-to-unreal-handoff-conventions--fixture-proof-pending), [3.1 plan](../vertical-slice-1-implementation-plan.md#phase-31-player-and-scale-fixture) |

## Source, Export And Import Ownership

- Blender source: `assets/blender/development/scale-handoff.blend`, Blender 5.2.3 LTS,
  metric display, unit scale 1. Source scene was saved and reopened through native Blender MCP;
  the eight expected render/collision objects persisted. The initial clean startup scene was
  preserved in `.local/blender-pilot/runs/handoff-01/baseline.blend` before source creation.
- `assets/recipes/create_scale_handoff.py` creates the initial source and exports;
  `export_scale_handoff.py` repeats exports from the saved source. The source assembly retains
  separate cube, flap and frame origins at (0,0,0), (0,-3,0) and (0,3,0) metres.
  Export temporarily recentres each selected render part and its collision at that part's pivot,
  then restores the editable assembly. No object/actor scale is used to repair imported units.
- FBX files: `assets/exports/development/scale-handoff/SM_HandoffCube.fbx`,
  `SM_HandoffFlap.fbx` and `SM_HandoffDoorFrame.fbx`. One render part plus its named UCX collision
  per file; the doorway has three separate convex collision boxes around its opening.
- Unreal meshes: `/Game/XGP/Development/Handoff/SM_HandoffCube`, `SM_HandoffFlap` and
  `SM_HandoffDoorFrame`. Native `StaticMeshTools.import_file` uses legacy `FbxFactory/FbxImportUI`,
  static-mesh mode, combine meshes true and material/texture import false. Cube marker slots use
  three simple Unreal-created colour materials; Blender shader transfer is not a pass criterion.
- Material tool recipe: `assets/recipes/create_handoff_marker_materials.py`. Cube faces identify
  front (red), right (green) and top (blue); the offset cube bounds independently expose axis flips.

## Export Settings And Initial Measurements

Tested Blender FBX settings: selected MESH objects only; global scale 1; apply unit scale true;
`FBX_SCALE_NONE`; forward -Y/up Z; use space transform true; bake space transform false;
face smoothing; animation/custom-property export false. `FBX_SCALE_NONE` bakes the metre-to-centimetre
factor into node/geometry transforms for this importer. The initial `FBX_SCALE_UNITS` candidate left
the cube only 1 cm in Unreal; it was rejected before placement. Owned unreferenced trial imports
were removed and imported again from corrected exports. Native import refuses an existing asset;
this replacement was not a successful reimport test.

An inward face-winding error in the initial primitive helper was corrected before import, including
collision meshes and face-slot assignment. The retained creation recipe has outward winding.

| Asset | Imported local bounds, cm | Collision |
| --- | --- | --- |
| Cube | X -25..75, Y -40..60, Z 0..100 | One imported convex hull |
| Initial flap | X -5..5, Y 0..100, Z 0..100 | One imported convex hull |
| Frame | X -10..10, Y -70..70, Z 0..220 | Three imported convex hulls; opening 100 × 200 cm |

Source +X/front, -Y/right and +Z/up map to Unreal +X/front, +Y/right and +Z/up. The cube is exactly
one metre on each side with an intentionally asymmetric origin; its bounds distinguish orientation
from mere cubic size. Named material slots were retained. Collision hulls report QueryAndPhysics,
not generated replacement hulls; collision trace mode is Default.

## Level Placement And Pivot Checks

Saved/reopened `L_TestLab` contains `Handoff_Cube` at (-350,350,0), `Handoff_DoorFrame` at
(-100,450,0) and `Handoff_Flap` at (-100,650,0) cm, all actor scales (1,1,1). These are separated
test stations, not the source assembly offsets or an operating ship mechanism. Pre-placement map
checkpoint: `.local/validation/phase-3-1/L_TestLab-before-handoff.umap`.

Numeric scene traces found no hit through the frame centre, and hits at 40 cm through a post,
75 cm through the cube and 45 cm through the initial flap. These line queries support configuration
checks; the actual player's capsule passage/blocking still needs owner-run observation.

The flap pivot remained (-100,650,0) cm at both 0 and 90 degrees yaw. Its bounds changed from
X -105..-95 / Y 650..750 to X -200..-100 / Y 645..655, Z 0..100 throughout. The old trace became
clear and a trace through the rotated panel hit at approximately 50 cm. Restored 0-degree pose,
saved and reopened the level. Raw checks: `.local/validation/phase-3-1/handoff-native-checks.json`.

Native ActorTools partial transform updates unexpectedly reset omitted location to zero, contrary
to its description. The affected owned flap was restored; the successful repeat supplied full
location/rotation/scale explicitly. No successful pivot claim relies on that failed partial update.

## Deliberate Source Revision

`assets/recipes/revise_scale_handoff_flap.py` changed render and collision thickness from 10 to
12 cm, preserving the source hinge/origin, length and height. Saved source checkpoint:
`.local/validation/phase-3-1/scale-handoff-before-revision.blend`. Re-exported with the tested settings.
Blender now measures 0.12 × 1 × 1 m; Unreal still measures 10 × 100 × 100 cm before reimport.

Owner subsequently reimported all three meshes and reported saving everything.
Initial imports also emitted degenerate tangent/near-zero binormal warnings because the proxy
helper omitted UV coordinates. Added normalized non-degenerate per-face UVs to all three render
meshes, saved and re-exported; retained `add_scale_handoff_uvs.py` records that repair and the initial
creation recipe includes it. These overlapping face UVs are sufficient for this untextured fit fixture,
not a finished texture/lightmap layout. Reimport results below verify the fix in Unreal.

## Owner Reimport And Saved-Package Verification — 2026-10-24

- Native queries measured flap render and collision bounds X -6..6, Y 0..100, Z 0..100 cm,
  confirming the deliberate 12 cm thickness change. Cube and frame bounds remain unchanged;
  collision hull counts are respectively one, three and one for cube, frame and flap.
- All three existing actor/component references still resolve to the same mesh asset paths,
  locations, zero rotations and scales (1,1,1). Cube marker material slots retain the three
  Unreal-created materials. Raw live-query result: `.local/validation/phase-3-1/handoff-after-reimport.json`.
- The three mesh packages reported dirty during inspection. Explicitly saved only those three
  owned assets before independent verification; no claim is made about why dirty flags remained
  after the owner-reported Save All. The level was clean at inspection.
- Retained `.local/validation/phase-3-1/handoff-reimport-snapshot.log`. The segment from the
  latest flap build through the cube/frame reimports contains no errors or degenerate-tangent /
  near-zero-binormal warnings. Earlier rejected imports and an earlier expired MCP-session message
  remain in the full historical log; they are not new reimport failures.
- `tools/unreal/verify_scale_handoff.py` loaded the saved packages and map in a separate
  read-only NullRHI commandlet. Initial verification stopped because StaticMeshEditorSubsystem
  is unavailable in commandlet mode; the corrected verifier reads reflected collision data and
  mesh texture-coordinate counts directly. The repeat passed, exit 0, zero reported errors/warnings.
  Log: `.local/validation/phase-3-1/handoff-saved-package-verification-02.log`; result:
  `handoff-saved-package-verification.json` in that folder. Retained the failed first log as evidence.
- Independent checks corroborate dimensions, hull counts, UV channels, marker-material references,
  scale-1 level placements and the unchanged neutral-map hash. These are saved-data checks, not
  a rendered appearance, capsule traversal or owner-observed hinge-motion pass.

## Owner Visual And Traversal Results — 2026-10-24

- Owner reported all requested checks worked, explicitly confirming imported-frame traversal in
  both camera modes, expected blocking and edge-hinge rotation. No cube marker/shading issue was
  reported. Owner restored Z rotation to zero and saved.
- Native inspection confirmed the flap at (-100,650,0) cm, rotation (0,0,0), scale (1,1,1),
  with the level clean. This corroborates the saved editor pose; visual pivot behavior is the
  owner-run observation, not a claim based solely on numeric bounds.
- Retained `.local/validation/phase-3-1/handoff-owner-play-snapshot.log`. The latest PIE run
  kept player ID 60254 across 15 switches, 12 with nonzero velocity; all logged `stable=true`
  and capsule 30/90 cm. The latest Play segment has no Error/Fatal/failed-ensure messages and
  records teardown. Earlier diagnostic messages remain in the historical portion of the log.
- Local handoff, deliberate reimport and player-fit checks pass for these owned proxies. Equipment
  and actual ship mechanism motion remain outside the fixture. [Published retrieval/open proof](phase-3-1-recovery-results.md)
  for the new source/export/imported asset set also passed under the existing storage contract.
  The [3.1 closeout](../phase-3-1-closeout.md) records acceptance and closure within those limits.
