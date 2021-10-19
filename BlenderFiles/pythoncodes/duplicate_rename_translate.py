import bpy

def duplicate_move_and_rename(obj_name, new_name, x, y, z):
    for obj in bpy.data.objects:
        obj.select_set(False)
    original_obj = bpy.data.objects[obj_name]
    original_obj.select_set(True)
    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(x,y,z)})
    new_obj = bpy.data.objects[obj_name + ".001"]
    new_obj.name = new_name

#bpy.data.objects['Cup'].select_set(True)
#bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(1,1,1)})
#bpy.data.objects['Cup.001'].name = 'Cup2'
#duplicate_move_and_rename('Cup', 'Cup2', 1, 1, 1)
#duplicate_move_and_rename('Cup2', 'Cup3', 1, 2, 1)
#duplicate_move_and_rename('Cup3', 'Cup4', 1, 3, 1)

#for i in range(10):
#    duplicate_move_and_rename('Cup' + str(i), 'Cup' + str(i+1), 0.5, 0, 0)

