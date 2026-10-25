# Player And Scale Fixture — Phase 3.1

Status: editor build, saved-map measurements and scoped owner-run input, traversal, camera and
neutral clearance checks passed 2026-10-24. Local Blender handoff checks also passed; publication /
storage proof and later equipment/context repeats remain separate. See the
[results record](../implementation/validation/phase-3-1-player-scale-results.md).
The [implementation plan](../implementation/vertical-slice-1-implementation-plan.md#phase-31-player-and-scale-fixture)
owns scope. [VS1-G01](../implementation/validation/spatial-validation-procedures.md#vs1-g01)
owns validation. This fixture is a development aid, not ship geometry or finished Gene artwork.

## What The Components Do

- `AXGPScaleCharacter` is one physical walking actor. Unreal's Character Movement component handles
  ordinary floor/wall collision; a collision capsule is the invisible rounded boundary around the body.
  The visible block/sphere body has no separate collision. It exists only to make scale readable.
- Two cameras view that same actor. First person places the view at eye level. Third person uses a
  spring arm: a camera mount that shortens when an obstacle would otherwise sit between camera and
  body. Switching cameras does not replace the actor or move its collision boundary.
- Enhanced Input maps keyboard/mouse inputs to named actions in a transient context owned by this
  fixture. It does not add a rebinding menu or prove controller support.
- `AXGPScaleFixture` provides measured static obstacles and labels. `AXGPScaleGameMode` selects the
  walking character for the test level only. A Game Mode chooses such things as the player class;
  it does not require changing the project's neutral proof map or its global defaults.

## Initial Test Configuration

These are provisional E/F fit and usability values, not verified character dimensions or approved
ship openings. Preserve the accepted nominal body scale while reviewing camera/clearance issues.

| Item | Initial value |
| --- | --- |
| Physical capsule | 180 cm total height, 30 cm radius (60 cm diameter) |
| First-person eye | 160 cm above capsule bottom on a flat floor |
| Visible proxy | Block torso and sphere head; highest point 180 cm above capsule bottom |
| Walk speed / step height | 300 cm/s / 35 cm; temporary ordinary-gravity fixture tuning |
| First/third-person field of view | 90 degrees |
| Third-person arm | 300 cm; target 55 cm above capsule centre; 12 cm collision probe |
| Reference floor | 20 × 16 m; top at Z=0 |
| Freestanding openings | 100 × 200 cm and 80 × 200 cm clear; dimensions exclude posts/header |
| Static reference cube | 100 × 100 × 100 cm |
| Wall / marker | Camera obstruction/collision wall and a non-interactive reach-reference marker |

The 200 cm openings test the initial 20 cm nominal head margin. They do not set a universal deck
height. The reference marker does not implement interaction or certify equipment reach.

## Guided Runtime Check — Not Yet Executed

Open the project in Unreal Editor, open the Content Drawer (Ctrl+Space), navigate to
`Content/XGP/Development` and double-click `L_TestLab`. The neutral proof remains the project's
startup/default map; the scale player is assigned through this level's Game Mode override only.

For the first runtime pass:

1. Open that level and press Play. Click inside the viewport if it has not captured mouse input.
2. Use **WASD** to walk and the **mouse** to look. This is a walking body rather than the neutral
   proof's floating test pawn. Jumping, magnetic boots, low gravity and equipment are not included.
3. Press **V** while stationary, while walking and beside a wall. The view changes; the same body
   ID should remain in the development overlay. Report awkward framing/clipping separately from
   physical teleportation or collision errors.
4. Walk through both labelled openings in both views and try walking into the posts/wall. Compare
   perceived scale, visible head clearance and the third-person camera's response near obstacles.
5. Stop beside the reference marker and switch views. Camera distance must not become a new
   physical player position. Actual interaction/equipment permission checks remain later work.
6. Press **Esc** to return to editing. Keep observations for the G01 results record; compilation
   or a successful Play launch alone does not close the procedure.

Perspective switches log actor identity, transform, velocity and capsule dimensions under
`LogXGPScale`; an immediate transform/identity/velocity invariant is checked in code. This supplements
the observed traversal checks and does not substitute for them. IDs are session-local, not save IDs.
