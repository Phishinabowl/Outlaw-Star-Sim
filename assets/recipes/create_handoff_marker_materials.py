import json

def create_material(name):
    return execute_tool("editor_toolset.toolsets.material.MaterialTools.create_material",
                        json.dumps({"folder_path":"/Game/XGP/Development/Handoff","asset_name":name}))["returnValue"]
def add_colour(material):
    return execute_tool("editor_toolset.toolsets.material.MaterialTools.add_expression",
                        json.dumps({"material_or_function":material,
                                    "expression_class":{"refPath":"/Script/Engine.MaterialExpressionConstant3Vector"},
                                    "x":-200,"y":0}))["returnValue"]
def set_colour(expression, colour):
    return execute_tool("editor_toolset.toolsets.object.ObjectTools.set_properties",
                        json.dumps({"instance":expression,"values":json.dumps({"Constant":colour})}))
def connect(expression):
    return execute_tool("editor_toolset.toolsets.material.MaterialTools.connect_to_output",
                        json.dumps({"expression":expression,"output_name":"","material_property":"MP_BaseColor"}))
def compile_material(material):
    return execute_tool("editor_toolset.toolsets.material.MaterialTools.recompile",
                        json.dumps({"material_or_function":material}))
def assign_material(slot, material):
    return execute_tool("editor_toolset.toolsets.static_mesh.StaticMeshTools.set_material",
                        json.dumps({"mesh":{"refPath":"/Game/XGP/Development/Handoff/SM_HandoffCube.SM_HandoffCube"},
                                    "slot_name":slot,"material":material}))
def run():
    made=[]
    for suffix,slot,colour in [
        ("Front","Marker_Front_PosX",{"r":1,"g":.02,"b":.01,"a":1}),
        ("Right","Marker_Right_NegY",{"r":.01,"g":.7,"b":.02,"a":1}),
        ("Top","Marker_Top_PosZ",{"r":.01,"g":.04,"b":1,"a":1})]:
        material=create_material("M_Handoff"+suffix)
        expression=add_colour(material)
        set_colour(expression,colour)
        connect(expression)
        compile_material(material)
        assign_material(slot,material)
        made.append(material)
    return {"materials":made}
