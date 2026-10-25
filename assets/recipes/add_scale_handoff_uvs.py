"""Add non-degenerate face UVs to the owned proxy meshes before repeat export."""
import bpy
from pathlib import Path

assert Path(bpy.data.filepath).name == "scale-handoff.blend"
assert not bpy.data.is_dirty
for name in ["SM_HandoffCube", "SM_HandoffFlap", "SM_HandoffDoorFrame"]:
    obj = bpy.data.objects[name]
    assert obj.get("handoff_owned") is True
    mesh = obj.data
    assert len(mesh.uv_layers) == 0, "Refuse to overwrite existing UV work"
    uv = mesh.uv_layers.new(name="UVMap")
    for face in mesh.polygons:
        normal_axis = max(range(3), key=lambda i: abs(face.normal[i]))
        axes = [i for i in range(3) if i != normal_axis]
        coords = [mesh.vertices[mesh.loops[i].vertex_index].co for i in face.loop_indices]
        lows = [min(v[a] for v in coords) for a in axes]
        spans = [max(v[a] for v in coords)-lows[j] for j,a in enumerate(axes)]
        assert all(span > 0 for span in spans)
        for loop_index in face.loop_indices:
            vertex = mesh.vertices[mesh.loops[loop_index].vertex_index].co
            uv.data[loop_index].uv = tuple((vertex[a]-lows[j])/spans[j] for j,a in enumerate(axes))
    mesh.update()
bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath, check_existing=False)
result = {name: len(bpy.data.objects[name].data.uv_layers) for name in ["SM_HandoffCube","SM_HandoffFlap","SM_HandoffDoorFrame"]}
