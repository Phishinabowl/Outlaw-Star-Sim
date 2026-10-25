"""Create the Phase 3.1 development map once, using Unreal's editor Python API.

Run with UnrealEditor-Cmd, PythonScriptPlugin enabled for that process only.
Refuses to replace an existing L_TestLab or alter L_NeutralProof/default maps.
"""
import hashlib
import json
import os
from pathlib import Path

import unreal


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


project = Path(unreal.Paths.project_dir()).resolve()
repo = project.parent.parent
neutral_file = project / "Content/XGP/Development/L_NeutralProof.umap"
target_file = project / "Content/XGP/Development/L_TestLab.umap"
engine_config = project / "Config/DefaultEngine.ini"
neutral_hash = digest(neutral_file)
config_hash = digest(engine_config)

levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
editor = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
if target_file.exists():
    # Recovery only for an inspected incomplete copy, never a general overwrite switch.
    resume_hash = os.environ.get("XGP_TESTLAB_RESUME_SHA256", "")
    assert resume_hash and digest(target_file) == resume_hash, "Refuse to modify an unreviewed existing L_TestLab"
    assert levels.load_level("/Game/XGP/Development/L_TestLab")
else:
    assert levels.new_level_from_template(
        "/Game/XGP/Development/L_TestLab", "/Game/XGP/Development/L_NeutralProof"
    ), "Could not create the isolated map from the neutral template"

initial_actors = actors.get_all_level_actors()
floor_actors = [a for a in initial_actors if isinstance(a, unreal.StaticMeshActor)
                and a.static_mesh_component.get_editor_property("static_mesh")
                and a.static_mesh_component.get_editor_property("static_mesh").get_path_name()
                == "/Engine/MapTemplates/SM_Template_Map_Floor.SM_Template_Map_Floor"]
starts = [a for a in initial_actors if isinstance(a, unreal.PlayerStart)]
assert len(floor_actors) == 1, "Expected the template's single floor mesh"
assert len(starts) == 1, "Expected one template PlayerStart"
removed_floor = floor_actors[0].get_actor_label()
assert actors.destroy_actor(floor_actors[0]), "Could not remove the copied floor"

fixture_class = unreal.load_class(None, "/Script/OutlawStarSim.XGPScaleFixture")
mode_class = unreal.load_class(None, "/Script/OutlawStarSim.XGPScaleGameMode")
character_class = unreal.load_class(None, "/Script/OutlawStarSim.XGPScaleCharacter")
assert fixture_class and mode_class and character_class
fixture = actors.spawn_actor_from_class(fixture_class, unreal.Vector(0, 0, 0))
assert fixture
fixture.set_actor_label("ScaleFixture_3_1")
start = starts[0]
start.set_actor_location(unreal.Vector(-650, 0, 95), False, False)
start.set_actor_rotation(unreal.Rotator(0, 0, 0), False)
editor.get_editor_world().get_world_settings().set_editor_property("default_game_mode", mode_class)
assert levels.save_current_level(), "Could not save L_TestLab"
assert levels.load_level("/Game/XGP/Development/L_TestLab"), "Could not reopen L_TestLab"

reopened = actors.get_all_level_actors()
fixtures = [a for a in reopened if a.get_class() == fixture_class]
starts = [a for a in reopened if isinstance(a, unreal.PlayerStart)]
assert len(fixtures) == 1 and len(starts) == 1
assert editor.get_editor_world().get_world_settings().get_editor_property("default_game_mode") == mode_class
assert unreal.get_default_object(mode_class).get_editor_property("default_pawn_class") == character_class

components = []
for c in fixtures[0].get_components_by_class(unreal.StaticMeshComponent):
    loc, scale = c.get_world_location(), c.get_world_scale()
    components.append({"name": c.get_name(), "location_cm": [loc.x, loc.y, loc.z],
                       "scale": [scale.x, scale.y, scale.z],
                       "collision_profile": str(c.get_collision_profile_name()),
                       "mesh": c.get_editor_property("static_mesh").get_path_name()})

assert digest(neutral_file) == neutral_hash, "Neutral map changed unexpectedly"
assert digest(engine_config) == config_hash, "Default map/configuration changed unexpectedly"
output = repo / ".local/validation/phase-3-1"
output.mkdir(parents=True, exist_ok=True)
manifest = {"map": "/Game/XGP/Development/L_TestLab", "map_sha256": digest(target_file),
            "neutral_sha256": neutral_hash, "default_engine_ini_sha256": config_hash,
            "copied_floor_removed": removed_floor,
            "actors": [{"name": a.get_actor_label(), "class": a.get_class().get_path_name()}
                       for a in reopened],
            "fixture_components": components, "game_mode": mode_class.get_path_name(),
            "default_pawn": character_class.get_path_name(), "reopen_passed": True,
            "runtime_validation": "not executed"}
(output / "test-lab-creation.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
unreal.log("XGP_TESTLAB_CREATED " + json.dumps(manifest))
