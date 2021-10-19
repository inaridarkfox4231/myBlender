import bpy
from math import sin, cos, pi

# 頂点データと辺データ用の配列を用意しておく
verts = []
edges = []
# メッシュオブジェクトを生成。名前を付けておく。
msh = bpy.data.meshes.new(name = "myStar_11_7_60")
# 頂点と辺のデータを生成
N = 640
for i in range(N):
    t = 2 * pi * i / N
    verts.append([15 * cos(11 * t) - 10 * sin(7 * t), 15 * sin(11 * t) - 10 * cos(7 * t), 0])
    edges.append([i, (i + 1) % N])
# メッシュにデータを登録
msh.from_pydata(verts, edges, [])
msh.update()

# メッシュデータを渡してオブジェクトを生成する
obj = bpy.data.objects.new(name = "star1", object_data = msh)
# シーンにリンクさせる
scene = bpy.context.scene
scene.collection.objects.link(obj)
