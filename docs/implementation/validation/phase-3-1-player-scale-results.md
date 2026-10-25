# Phase 3.1 — Player And Scale Results

| Field | Value |
| --- | --- |
| Started | 2026-10-23 |
| Status | Scoped VS1-G01, Blender handoff and published recovery checks passed; later equipment repeats remain separate |
| Baseline | Initial checks followed `a0141b9`; implementation published as `6b2de6f` |
| Scope | One physical player, first/third-person cameras and isolated scale references; no 3.2A |
| Configuration / guide | [Player scale fixture](../../development/player-scale-fixture.md) |

## Initial Build Attempt

Ordinary `OutlawStarSimEditor Win64 Development` build compiled the new character, Game Mode,
fixture and generated reflection code. Linking failed because UnrealEditor.exe held the project
DLL open: LNK1104 after the build accelerator retried. This is an incomplete build, not a runtime
pass. The earlier non-elevated process query returned no editor entry and was insufficient to
establish editor closure. Owner closure was requested before a retry.

Log: `.local/validation/phase-3-1/editor-build-01.log`. Effective toolchain remained MSVC
14.50.35739 and SDK 10.0.26100.0. Neutral-map SHA-256 remained
`1dc38b4e2ee6cf16c0af7e122d8615a677ce9b805774388ebf44231d0b5d1b43` at this inspection.

## Build Retry And Map Preparation — 2026-10-24

- Following owner-reported editor closure, the ordinary editor build completed successfully,
  exit 0. The remaining two actions linked the DLL and wrote target metadata in 5.19 seconds total.
  Toolchain remained MSVC 14.50.35739 / SDK 10.0.26100.0.
  Log: `.local/validation/phase-3-1/editor-build-02.log`.
- Created `Content/XGP/Development/L_TestLab.umap` from the neutral template. Retained its lighting
  and sky sphere, replaced only the copied template floor with the measured fixture, moved its sole
  PlayerStart to (-650, 0, 95) cm and assigned `XGPScaleGameMode` as the level override.
  The override's default pawn resolves to `XGPScaleCharacter`.
- Creation recipe: `tools/unreal/create_scale_test_lab.py`. A commandlet enabled the already
  installed PythonScriptPlugin for that process only; no plugin entry or global/default map was
  changed. NullRHI disabled rendered output, so these runs are not visual or performance evidence.
- Initial creation stopped before fixture mutation because its broad static-mesh check also counted
  the sky sphere. An independent inventory identified the exact floor asset; recovery validated the
  incomplete copy's SHA-256 before continuing. The next run saved/reopened the completed map but its
  verification used a Python `isinstance` check with an Unreal class object. Corrected that check;
  a separate read-only verification process then succeeded with exit 0, zero reported errors/warnings.
  Both failed attempts remain in `test-lab-creation-01.log` / `test-lab-creation-02.log` as diagnostic evidence.
- Independent saved-map checks measured all 10 fixture mesh components, `BlockAll` collision
  profiles, the 20 × 16 m floor and 1 m reference cube. Post/header bounds give actual clear
  openings of 100 × 200 cm and 80 × 200 cm. Character defaults give capsule radius 30 cm and
  half-height 90 cm. These are configuration/geometry checks, not a traversed collision pass.
- Read-only verification log/result:
  `.local/validation/phase-3-1/test-lab-verification.log` / `test-lab-verification.json`.
  Test-map SHA-256: `ed19f899350d33c647cb480a631b056185019361dae401c82810713563bb8202`.
  Neutral-map SHA-256 remains the recorded Phase 2 value; DefaultEngine.ini remains unchanged.

## First Owner Play Pass — 2026-10-24

- Owner reported opening `L_TestLab`, working movement and V perspective switching, and Esc
  returning to editing. This establishes the initial input/view workflow; detailed opening/wall
  clearance and camera-comfort observations were not yet reported.
- Reviewed live `Saved/Logs/OutlawStarSim.log`, retained as
  `.local/validation/phase-3-1/first-owner-play-snapshot.log`. PIE startup selected
  `XGPScaleCharacter_0`, session-local ID 63274, capsule radius 30 / half-height 90 cm.
- Three perspective switches logged the same actor/ID, `stable=true` and unchanged capsule
  dimensions. Positions changed between switches as the player traversed the fixture; all three
  recorded switches occurred at zero velocity. Switching while moving still requires a repeat.
- Recorded standing centre Z was 92.15 cm: actual movement-floor separation is about 2.15 cm
  in these samples. The 20 cm head margin is a nominal geometry target; it does not establish
  an exact observed 20 cm gap above the proxy during play.
- The snapshot contains no Error/Fatal/failed-ensure messages. Startup warnings concerned the
  engine's standard MCP licensing notice and an editor-layout key migration; neither is a logged
  player/camera failure. PIE teardown is recorded; owner supplied the Esc/return-to-editing observation.

## Owner Clearance Pass — 2026-10-24

- Owner reported success for the guided sequence: both labelled openings traversed in both views,
  post/wall blocking, perspective changes while moving/in an opening/beside the reference marker,
  third-person camera obstruction near the wall and Esc return to editing. No sticking,
  teleportation, see-through-surface or camera-comfort issue was reported for this fixture.
- Retained `.local/validation/phase-3-1/clearance-owner-play-snapshot.log`. The second PIE run used
  session-local ID 59792 throughout six switches; all reported `stable=true` and capsule 30/90 cm.
  Three switches have nonzero velocity, including approximately 300 cm/s movement. The invariant
  therefore passed during movement as well as at rest. PIE teardown is recorded.
- No Error/Fatal/failed-ensure messages appeared in the reviewed snapshot. Logs corroborate identity,
  transform/velocity invariance and capsule configuration; physical clearance and camera appearance
  rely on the owner-run observations, not a log-only fit claim.
- VS1-G01 passes for this neutral proxy and available state. Neither opening is a measured canonical
  ship aperture. The non-interactive marker supplies a body/camera reference only; interaction reach,
  equipment ownership and occupied contexts require the scheduled 3.4/later repeats.

## Remaining Integration Evidence

Equipment, low-gravity traversal and interaction locality are
not implemented by this fixture. The [Blender handoff](phase-3-1-blender-handoff-results.md) has
passed local checks, including imported-frame player passage. [Published asset recovery](phase-3-1-recovery-results.md)
also passed. The [3.1 closeout review](../phase-3-1-closeout.md) records acceptance and closure.
