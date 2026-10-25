"""Owned Phase 3.1 rigid-mesh handoff source/export recipe. Run inside Blender."""
import bpy
import json
from pathlib import Path
from mathutils import Vector

# Running the file uses its repository; MCP execution can supply XGP_HANDOFF_ROOT.
ROOT = Path(globals().get("XGP_HANDOFF_ROOT", Path(__file__).resolve().parents[2] if "__file__" in globals() else Path.cwd())).resolve()
assert (ROOT / "Unreal/OutlawStarSim/OutlawStarSim.uproject").is_file(), "Set XGP_HANDOFF_ROOT to this checkout"
SOURCE = ROOT / "assets/blender/development/scale-handoff.blend"
EXPORTS = ROOT / "assets/exports/development/scale-handoff"
BASELINE = ROOT / ".local/blender-pilot/runs/handoff-01/baseline.blend"
assert not SOURCE.exists() and not BASELINE.exists()
assert bpy.data.filepath == "" and not bpy.data.is_dirty
assert set(bpy.data.objects.keys()) == {"Cube", "Camera", "Light"}
assert bpy.context.mode == "OBJECT"
SOURCE.parent.mkdir(parents=True, exist_ok=True)
EXPORTS.mkdir(parents=True, exist_ok=True)
BASELINE.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(BASELINE), check_existing=False)
bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE), check_existing=False)
for obj in list(bpy.data.objects):
    bpy.data.objects.remove(obj, do_unlink=True)
scene = bpy.context.scene
scene.unit_settings.system = "METRIC"
scene.unit_settings.scale_length = 1.0

def boxes(name, parts, origin):
    verts, faces = [], []
    template = [(-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]
    face_indices = [(0,4,6,2),(1,3,7,5),(0,1,5,4),(2,6,7,3),(0,2,3,1),(4,5,7,6)]
    for centre, size in parts:
        offset = len(verts)
        verts += [tuple(centre[i] + v[i]*size[i]/2 for i in range(3)) for v in template]
        faces += [tuple(offset+i for i in reversed(face)) for face in face_indices]
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    if name.startswith("SM_"):
        uv = mesh.uv_layers.new(name="UVMap")
        for face in mesh.polygons:
            normal_axis = max(range(3), key=lambda i: abs(face.normal[i]))
            axes = [i for i in range(3) if i != normal_axis]
            coords = [mesh.vertices[mesh.loops[i].vertex_index].co for i in face.loop_indices]
            lows = [min(v[a] for v in coords) for a in axes]
            spans = [max(v[a] for v in coords)-lows[j] for j,a in enumerate(axes)]
            for loop_index in face.loop_indices:
                vertex = mesh.vertices[mesh.loops[loop_index].vertex_index].co
                uv.data[loop_index].uv = tuple((vertex[a]-lows[j])/spans[j] for j,a in enumerate(axes))
    obj = bpy.data.objects.new(name, mesh)
    scene.collection.objects.link(obj)
    obj.location = origin
    obj["handoff_owned"] = True
    return obj

cube_part = ((.25,-.1,.5),(1,1,1))
cube = boxes("SM_HandoffCube", [cube_part], (0,0,0))
# Asymmetric local bounds and named face slots expose axis flips/rotations.
for name, colour in [("Marker_Front_PosX",(1,.05,.02,1)),("Marker_Right_NegY",(.02,.8,.05,1)),
                     ("Marker_Top_PosZ",(.02,.1,1,1)),("Proxy_Neutral",(.5,.5,.5,1))]:
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = colour
    cube.data.materials.append(mat)
for face in cube.data.polygons:
    face.material_index = 0 if face.normal.x > .5 else 1 if face.normal.y < -.5 else 2 if face.normal.z > .5 else 3
cube_collision = boxes("UCX_SM_HandoffCube_00", [cube_part], (0,0,0))

flap_part = ((0,-.5,.5),(.1,1,1))
flap = boxes("SM_HandoffFlap", [flap_part], (0,-3,0))
flap_collision = boxes("UCX_SM_HandoffFlap_00", [flap_part], (0,-3,0))

frame_parts = [((0,-.6,1),(.2,.2,2)),((0,.6,1),(.2,.2,2)),((0,0,2.1),(.2,1.4,.2))]
frame = boxes("SM_HandoffDoorFrame", frame_parts, (0,3,0))
frame_collisions = [boxes("UCX_SM_HandoffDoorFrame_%02d"%i, [part], (0,3,0)) for i,part in enumerate(frame_parts)]
groups = [(cube,[cube_collision]),(flap,[flap_collision]),(frame,frame_collisions)]
settings = dict(use_selection=True, object_types={"MESH"}, global_scale=1.0,
                apply_unit_scale=True, apply_scale_options="FBX_SCALE_NONE",
                axis_forward="-Y", axis_up="Z", use_space_transform=True,
                bake_space_transform=False, mesh_smooth_type="FACE",
                bake_anim=False, add_leaf_bones=False, use_custom_props=False)
manifest = {"blender": bpy.app.version_string, "metres_per_unit": 1,
            "source_axes": "+X front, -Y right, +Z up; conversion pending Unreal measurement",
            "settings": {k: sorted(v) if isinstance(v,set) else v for k,v in settings.items()}, "assets": []}
for obj, collisions in groups:
    selected = [obj] + collisions
    anchor = obj.location.copy()
    original = [(part, part.location.copy()) for part in selected]
    bpy.ops.object.select_all(action="DESELECT")
    for part in selected:
        part.location -= anchor
        part.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.context.view_layer.update()
    path = EXPORTS / (obj.name + ".fbx")
    assert not path.exists()
    try:
        bpy.ops.export_scene.fbx(filepath=str(path), check_existing=False, **settings)
        corners = [Vector(v) for v in obj.bound_box]
        manifest["assets"].append({"name": obj.name, "source": str(SOURCE), "export": str(path),
            "source_assembly_origin_m": list(anchor), "dimensions_m": list(obj.dimensions),
            "local_min_m": [min(v[i] for v in corners) for i in range(3)],
            "local_max_m": [max(v[i] for v in corners) for i in range(3)],
            "collision_objects": [part.name for part in collisions]})
    finally:
        for part, location in original:
            part.location = location
            part.select_set(False)
    for part in collisions:
        part.display_type = "WIRE"
        part.hide_render = True
        part.hide_set(True)
cube.select_set(True)
bpy.context.view_layer.objects.active = cube
bpy.context.view_layer.update()
bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE), check_existing=False)
(ROOT / ".local/validation/phase-3-1/handoff-source-export.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
result = manifest
