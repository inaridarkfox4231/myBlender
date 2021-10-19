import bpy
from math import *

def f(t, s):
    return cos(t) - s * sin(t)

def g(t, s):
    return sin(t) + s * cos(t)

def inv(a):
    return tan(a) - a

def createGear(alpha, z, m, vs, es):
    size = (z + 1) * m
    r = z * m * 0.5
    rb = r * cos(alpha)
    ra = r + m
    ri = min(rb, r - 1.25 * m)
    beta = acos(r * cos(alpha) / ra)
    psi = tan(beta)
    phi = pi / (2 * z) + inv(alpha)
    
    points = []
    
    for k in range(z):
        phase = pi * 2 * k / z;
        points.append([ri * cos(phase - pi / z), ri * sin(phase - pi / z), 0]);
        # 歯底円上をスタートまで円弧
        for i in range(11):
            theta = phase - pi / z + (pi / (2 * z) - inv(alpha)) * (i / 10);
            points.append([ri * cos(theta), ri * sin(theta), 0]);

        # 歯底円から基礎円まで浮上
        for i in range(11):
            radius = ri + (rb - ri) * (i / 10);
            theta = phase - pi / (2 * z) - inv(alpha);
            points.append([radius * cos(theta), radius * sin(theta), 0]);

        # 基礎円からインボリュートで外へ
        for i in range(41):
            theta = psi * i / 40;
            points.append([rb * f(phase - phi + theta, -theta), rb * g(phase - phi + theta, -theta), 0]);

        # 歯先円。
        for i in range(11):
            theta = phase + (phi - inv(beta)) * (-1 + 0.2 * i);
            points.append([ra * cos(theta), ra * sin(theta), 0]);

        # 逆インボリュートで再び基礎円へ
        for i in range(41):
            theta = psi * (40 - i) / 40;
            points.append([rb * f(phase + phi - theta, theta), rb * g(phase + phi - theta, theta), 0]);

        # 基礎円から歯底円へ
        for i in range(11):
            radius = ri + (rb - ri) * ((10 - i) / 10);
            theta = phase + pi / (2 * z) + inv(alpha);
            points.append([radius * cos(theta), radius * sin(theta), 0]);

        # 歯底円上をふたたびたどりフィニッシュ
        for i in range(11):
            theta = phase + pi / z - (pi / (2 * z) - inv(alpha)) * ((10 - i) / 10);
            points.append([ri * cos(theta), ri * sin(theta), 0]);
            
    vs = []
    es = []
    for vt in points: vs.append(vt)
    for i in range(len(vs)):
        es.append([i, (i + 1) % len(vs)])

    

# 頂点データと辺データ用の配列を用意しておく
verts = []
edges = []
# メッシュオブジェクトを生成。名前を付けておく。
msh = bpy.data.meshes.new(name = "myStar_11_7_60")

# 頂点と辺のデータを生成
createGear(pi / 9, 11, 4, verts, edges)

# メッシュにデータを登録
msh.from_pydata(verts, edges, [])
msh.update()

# メッシュデータを渡してオブジェクトを生成する
obj = bpy.data.objects.new(name = "star1", object_data = msh)
# シーンにリンクさせる
scene = bpy.context.scene
scene.collection.objects.link(obj)
