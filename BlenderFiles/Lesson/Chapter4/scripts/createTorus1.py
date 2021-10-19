import bpy
from mathutils import Color
from math import sin, cos, pi

def main():

    verts = []
    faces = []
    colors = []
    
    m = 50
    n = 50
    a = 1
    b = 0.5

    msh = bpy.data.meshes.new(name="myTorus")
    msh.vertex_colors.new(name="myColor")
    
    for j in range(n):
        for i in range(m):
            theta = 2 * pi * i / m
            phi = 2 * pi * j / n
            innerR = b * (0.5 + 0.2 * sin(5 * theta + 10 * phi))
            rx = innerR * cos(theta)
            ry = innerR * sin(theta)
            r = a + ry
            x = r * cos(phi)
            y = r * sin(phi)
            z = rx
            verts.append([x, y, z])

    
    # mathutilsには様々な機能があるけど今回使うのは
    # hsvのやつ。Color()でインスタンスを作り、使い回す。
    # col.hsv=(h,s,v)でhsvでの表示を用意して
    # rgbでアクセスして放り込めばいいので楽ちん!
    
    col = Color()
    
    for j in range(n):
        for i in range(m):
            faces.append([i + m * j, ((i + 1) % n) + m * j, 
                         ((i + 1) % n) + m * ((j + 1) % n), i + m * ((j + 1) % n)])
            x1 = i / m
            y1 = j / n
            col.hsv = (0.1 + 0.05 * sin(y1 * 2 * pi), 0.75 + 0.25 * cos(x1 * 2 * pi), 1.0)
            for id in range(4):
                colors.append([col.r, col.g, col.b, 1.0])

    # 先にメッシュを構成しないといけないらしい
    msh.from_pydata(verts, [], faces)

    # 対応するポリゴンの頂点に色を対応付ける
    for idx, vc in enumerate(msh.vertex_colors['myColor'].data):
        vc.color = colors[idx]

    msh.update()
    obj = bpy.data.objects.new(name="cube", object_data = msh)

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