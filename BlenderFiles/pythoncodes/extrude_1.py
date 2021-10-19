import bpy

bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={
"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False},
TRANSFORM_OT_translate={"value":(0, 0, 0.5), "orient_type":'NORMAL',
"orient_matrix":((0, 1, 0), (-1, 0, 0), (0, 0, 1)), "orient_matrix_type":'NORMAL',
"constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False,
"proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False,
"use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0),
"snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False,
"texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False,
"use_automerge_and_split":False})

'''
単に特定の方向に押し出すだけならこれでいいみたいなんだけど
汎用性考えるとまずそうではあるわね
しかしオプションが膨大すぎる、、、
import bpy

bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0.5)})

押し出しで迷路作ってみたいけど
面の選択をあれこれするのが難しそう。
API叩け！
'''
