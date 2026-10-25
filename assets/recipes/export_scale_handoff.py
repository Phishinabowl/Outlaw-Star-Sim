"""Re-export only the owned handoff meshes; preserve assembly origins in the source."""
import bpy
import json
from pathlib import Path

source = Path(bpy.data.filepath).resolve()
assert source.parts[-4:] == ("assets", "blender", "development", "scale-handoff.blend")
root = source.parents[3]
source = root / "assets/blender/development/scale-handoff.blend"
assert Path(bpy.data.filepath) == source and bpy.context.mode == "OBJECT"
assert not bpy.data.is_dirty, "Save reviewed source changes before exporting"
manifest_path = root / ".local/validation/phase-3-1/handoff-source-export.json"
settings = dict(use_selection=True, object_types={"MESH"}, global_scale=1.0,
                apply_unit_scale=True, apply_scale_options="FBX_SCALE_NONE",
                axis_forward="-Y", axis_up="Z", use_space_transform=True,
                bake_space_transform=False, mesh_smooth_type="FACE",
                bake_anim=False, add_leaf_bones=False, use_custom_props=False)
# Bake metre-to-centimetre conversion into transforms; tested legacy importer
# does not apply the FBX unit metadata emitted by FBX_SCALE_UNITS.
settings["apply_scale_options"] = "FBX_SCALE_NONE"
manifest = {"blender": bpy.app.version_string, "metres_per_unit": 1,
            "source_axes": "+X front, -Y right, +Z up; Unreal +X, +Y, +Z verified",
            "settings": {k: sorted(v) if isinstance(v,set) else v for k,v in settings.items()},
            "assets": []}
for name, collision_names in [
    ("SM_HandoffCube", ["UCX_SM_HandoffCube_00"]),
    ("SM_HandoffFlap", ["UCX_SM_HandoffFlap_00"]),
    ("SM_HandoffDoorFrame", ["UCX_SM_HandoffDoorFrame_00", "UCX_SM_HandoffDoorFrame_01", "UCX_SM_HandoffDoorFrame_02"])]:
    manifest["assets"].append({"name": name, "source": str(source),
        "export": str(root / "assets/exports/development/scale-handoff" / (name + ".fbx")),
        "collision_objects": collision_names})
for item in manifest["assets"]:
    obj = bpy.data.objects[item["name"]]
    parts = [obj] + [bpy.data.objects[n] for n in item["collision_objects"]]
    assert all(part.get("handoff_owned") is True for part in parts)
    path = root / "assets/exports/development/scale-handoff" / (obj.name + ".fbx")
    anchor = obj.location.copy()
    item["source_assembly_origin_m"] = list(anchor)
    original = [(part, part.location.copy(), part.hide_get()) for part in parts]
    bpy.ops.object.select_all(action="DESELECT")
    try:
        for part in parts:
            part.hide_set(False)
            part.location -= anchor
            part.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.context.view_layer.update()
        bpy.ops.export_scene.fbx(filepath=str(path), check_existing=False, **settings)
        item["dimensions_m"] = list(obj.dimensions)
        item["local_min_m"] = [min(v[i] for v in obj.bound_box) for i in range(3)]
        item["local_max_m"] = [max(v[i] for v in obj.bound_box) for i in range(3)]
    finally:
        for part, location, hidden in original:
            part.location = location
            part.select_set(False)
            part.hide_set(hidden)
bpy.context.view_layer.update()
manifest_path.parent.mkdir(parents=True, exist_ok=True)
manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
result = {"exports": [item["export"] for item in manifest["assets"]]}
