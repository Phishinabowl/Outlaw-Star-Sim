"""Read-only saved-package verification after the Phase 3.1 owner reimport."""
import hashlib
import json
from pathlib import Path
import unreal

project = Path(unreal.Paths.project_dir()).resolve()
repo = project.parent.parent
output = {}
for name, dimensions, hulls in [
    ("SM_HandoffCube", (100,100,100), 1),
    ("SM_HandoffFlap", (12,100,100), 1),
    ("SM_HandoffDoorFrame", (20,140,220), 3)]:
    mesh = unreal.load_asset("/Game/XGP/Development/Handoff/" + name)
    assert mesh, name
    box = mesh.get_bounding_box()
    size = box.max - box.min
    measured = [size.x, size.y, size.z]
    assert all(abs(a-b) < .01 for a,b in zip(measured,dimensions)), (name, measured)
    # StaticMeshEditorSubsystem is unavailable in commandlets; read saved data directly.
    body = mesh.get_editor_property("body_setup")
    count = len(body.get_editor_property("agg_geom").get_editor_property("convex_elems"))
    channels = mesh.get_num_tex_coords(0)
    assert count == hulls and channels >= 1, (name, count, channels)
    output[name] = {"dimensions_cm": measured, "collision_hulls": count, "uv_channels": channels}
    if name == "SM_HandoffCube":
        slots = {str(s.material_slot_name): s.material_interface.get_path_name()
                 for s in mesh.get_editor_property("static_materials")}
        for slot, material in [("Marker_Front_PosX","M_HandoffFront"),
                               ("Marker_Right_NegY","M_HandoffRight"),
                               ("Marker_Top_PosZ","M_HandoffTop")]:
            assert slots[slot] == "/Game/XGP/Development/Handoff/" + material + "." + material
        output[name]["materials"] = slots

levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
assert levels.load_level("/Game/XGP/Development/L_TestLab")
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_all_level_actors()
placements = {}
for actor in actors:
    label = actor.get_actor_label()
    if label.startswith("Handoff_"):
        scale = actor.get_actor_scale3d()
        assert all(abs(v-1) < .0001 for v in [scale.x,scale.y,scale.z])
        mesh = actor.get_component_by_class(unreal.StaticMeshComponent).get_editor_property("static_mesh")
        placements[label] = {"mesh": mesh.get_path_name(), "location": str(actor.get_actor_location()),
                             "rotation": str(actor.get_actor_rotation()), "scale": [scale.x,scale.y,scale.z]}
assert set(placements) == {"Handoff_Cube","Handoff_Flap","Handoff_DoorFrame"}
assert placements["Handoff_Flap"]["mesh"].endswith("/SM_HandoffFlap.SM_HandoffFlap")
neutral_hash = hashlib.sha256((project/"Content/XGP/Development/L_NeutralProof.umap").read_bytes()).hexdigest()
assert neutral_hash == "1dc38b4e2ee6cf16c0af7e122d8615a677ce9b805774388ebf44231d0b5d1b43"
result = {"meshes": output, "placements": placements, "neutral_hash": neutral_hash,
          "owner_visual_and_walking": "not assessed by this read-only verifier; see result record"}
path = repo / ".local/validation/phase-3-1/handoff-saved-package-verification.json"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(result, indent=2), encoding="utf-8")
unreal.log("XGP_HANDOFF_SAVED_PACKAGES_VERIFIED " + json.dumps(result))
