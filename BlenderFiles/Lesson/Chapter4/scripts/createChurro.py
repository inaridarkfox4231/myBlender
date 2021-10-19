import bpy
from mathutils import Color
from math import sin, cos, pi
import numpy as np

def func0(t):
    return np.array([sin(7 * t), cos(6 * t), sin(8 * t)])

def normalize(v):
    return v / np.linalg.norm(v)

def main():

    verts = []
    faces = []
    colors = []
    
    n = 640 # 全体の分割
    m = 32 # 断面の分割

    msh = bpy.data.meshes.new(name="Churro2")
    msh.vertex_colors.new(name="myColor2")
    
    for i in range(n):
        for k in range(m):
            phi = 2 * pi * i / n # 全体の曲線上の点を示す角度
            theta = 2 * pi * k / m # 断面の周上の点を指定する角度
            r = 0.1 + 0.02 * sin(5 * theta + 320 * phi)
            v = func0(phi)
            v_next = func0(phi + 2 * pi / n)
            v_prev = func0(phi - 2 * pi / n)
            v1 = normalize(v_next - v)
            v2 = normalize(v - v_prev)
            pn = normalize(v1 - v2)
            bn = np.cross(v1, pn)
            position = v + r * cos(theta) * pn + r * sin(theta) * bn
            verts.append([position[0], position[1], position[2]])

    # mathutilsには様々な機能があるけど今回使うのは
    # hsvのやつ。Color()でインスタンスを作り、使い回す。
    # col.hsv=(h,s,v)でhsvでの表示を用意して
    # rgbでアクセスして放り込めばいいので楽ちん!
    
    col = Color()
    
    for i in range(n):
        for k in range(m):
            faces.append([i * m + k, i * m + ((k + 1) % m), 
                         ((i + 1) % n) * m + ((k + 1) % m), ((i + 1) % n) * m + k])
            phi = 2 * pi * i / n
            theta = 2 * pi * k / m
            col.hsv = (0.07 + 0.02*sin(phi), 0.75 + 0.25 * cos(theta), 1.0)
            for id in range(4):
                colors.append([col.r, col.g, col.b, 1.0])

    # 先にメッシュを構成しないといけないらしい
    msh.from_pydata(verts, [], faces)

    # 対応するポリゴンの頂点に色を対応付ける
    for idx, vc in enumerate(msh.vertex_colors['myColor2'].data):
        vc.color = colors[idx]

    msh.update()
    obj = bpy.data.objects.new(name="Churro2", object_data = msh)

    scene = bpy.context.scene

    scene.collection.objects.link(obj)

if __name__ == "__main__":
    main()
    
'''
普通のトーラス
for j in range(n):
    for i in range(m):
        theta = 2 * pi * i / m
        phi = 2 * pi * j / n
        rx = b * cos(theta)
        ry = b * sin(theta)
        r = a + ry
        x = r * cos(phi)
        y = r * sin(phi)
        z = rx
        verts.append([x, y, z])
'''