import bpy

me = bpy.data.meshes['Cylinder.001']

for p in me.polygons:
    print(p)
    
bpy.ops.object.mode_set(mode="OBJECT")

# 上の面だけ選択する場合は%2==0だけでいい（上下交互に番号が振られる）
'''
上に面を押し出した場合、それらの頂点はまとめて新しい番号が振られるので、
>47みたいにすればそれらだけ選択される。
'''
for v in me.vertices:
    if(v.index < 48 and v.index % 2 == 1): v.select= True

bpy.ops.object.mode_set(mode="EDIT")

