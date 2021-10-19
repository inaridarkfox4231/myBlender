import bpy

me = bpy.data.meshes['Cube.001']

for p in me.polygons:
    print(p)
    
bpy.ops.object.mode_set(mode="OBJECT")
me.polygons[0].select=True
bpy.ops.object.mode_set(mode="EDIT")

