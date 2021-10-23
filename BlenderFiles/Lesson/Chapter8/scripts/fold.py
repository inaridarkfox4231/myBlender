import bpy

obj = bpy.ops.object

obj.origin_set(type = 'ORIGIN_CURSOR', center = 'MEDIAN')

mirrorNames = ['PlaneX', 'PlaneY', 'PlaneZ']

for mirrorName in mirrorNames:
    obj.modifier_add(type='MIRROR')
    mirror = bpy.context.object.modifiers["Mirror"]
    mirror.use_axis[0] = False
    mirror.use_axis[2] = True
    mirror.mirror_object = bpy.data.objects[mirrorName]
    obj.modifier_apply(modifier = "Mirror")
    
msh = bpy.context.object.data
for v in msh.vertices:
    v.select = True

obj.mode_set(mode = "EDIT")
bpy.ops.mesh.remove_doubles() # 重複する頂点を削除
obj.mode_set(mode = "OBJECT")
