# スクリプトで頂点選択するコード
# オブジェクトモードじゃないとだめなんだ！
# ref:https://stackoverflow.com/questions/20349361/selected-vertex-did-not-highlight-in-blender-3d

import bpy

bpy.ops.mesh.primitive_cube_add()
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="DESELECT")
bpy.context.tool_settings.mesh_select_mode = (True , False , False)
bpy.ops.object.mode_set(mode="OBJECT")
#bpy.context.object.data.vertices[0].select = True
#bpy.context.object.data.vertices[0].co = (-3,-2,-3)
me = bpy.context.object.data
for v in me.vertices:
    v.select = True
bpy.ops.object.mode_set(mode="EDIT")