"""One deliberate pilot revision: 10 to 12 cm flap thickness, retaining hinge and collision."""
import bpy
from pathlib import Path

source = Path(bpy.data.filepath).resolve()
assert source.parts[-4:] == ("assets", "blender", "development", "scale-handoff.blend")
root = source.parents[3]
source = root / "assets/blender/development/scale-handoff.blend"
assert Path(bpy.data.filepath) == source and not bpy.data.is_dirty
checkpoint = root / ".local/validation/phase-3-1/scale-handoff-before-revision.blend"
assert not checkpoint.exists()
assert abs(bpy.data.objects["SM_HandoffFlap"].dimensions.x - .1) < .0001
bpy.ops.wm.save_as_mainfile(filepath=str(checkpoint), check_existing=False, copy=True)
for name in ["SM_HandoffFlap", "UCX_SM_HandoffFlap_00"]:
    obj = bpy.data.objects[name]
    assert obj.get("handoff_owned") is True
    for vertex in obj.data.vertices:
        vertex.co.x *= 1.2
    obj.data.update()
bpy.context.view_layer.update()
bpy.ops.wm.save_as_mainfile(filepath=str(source), check_existing=False)
result = {"revision": "flap thickness 10 -> 12 cm", "dimensions_m": list(bpy.data.objects["SM_HandoffFlap"].dimensions),
          "source_origin_m": list(bpy.data.objects["SM_HandoffFlap"].location)}
