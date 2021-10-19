import bpy

me = bpy.context.object.data
uv_layer = me.uv_layers.active.data

for poly in me.polygons:
    print("Polygon index: %d, length: %d" % (poly.index, poly.loop_total))

    # range is used here to show how the polygons reference loops,
    # for convenience 'poly.loop_indices' can be used instead.
    for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
        print("    Vertex: %d" % me.loops[loop_index].vertex_index)
        print("    UV: %r" % uv_layer[loop_index].uv)
        
'''
# オブジェクトから名前でアクセスする場合
import bpy

obj = bpy.data.objects.get("Cube")
# もしくは obj = bpy.data.objects['Cube'] でも可
me = obj.data

for v in me.vertices:
    print(v.co)
    
# メッシュの名前から直接アクセスしたりもできる
import bpy

me = bpy.data.meshes.get("Cube");
# もしくは me = bpy.data.meshes['Cube'] でも可

for v in me.vertices:
    print(v.co)

'''