import bpy
from mathutils import Color
from math import sin, cos, pi

def main():

    verts = []
    faces = []
    colors = []
    
    m = 20
    n = 20

    msh = bpy.data.meshes.new(name="cubemesh")
    msh.vertex_colors.new(name="myColor")

    for i in range(n):
        for k in range(m):
            z = 1 - 2*i/(n-1)
            phi = 2 * pi * k / m
            r = 1
            verts.append([r * cos(phi), r * sin(phi), z])
    
    # mathutilsには様々な機能があるけど今回使うのは
    # hsvのやつ。Color()でインスタンスを作り、使い回す。
    # col.hsv=(h,s,v)でhsvでの表示を用意して
    # rgbでアクセスして放り込めばいいので楽ちん!
    
    col = Color()

    for i in range(n - 1):
        for k in range(m):
            faces.append([i * m + k, (i + 1) * m + k, (i + 1) * m + ((k + 1) % m), i * m + ((k + 1) % m)])
            z = 1 - 2*i/(n-1)
            col.hsv = (0.55, 0.5 + 0.5 * z, 1.0)
            for id in range(4):
                colors.append([col.r, col.g, col.b, 1.0])

    # data input.
    #verts = [[-1.0, -1.0,  1.0], [1.0, -1.0,  1.0], [1.0, 1.0,  1.0], [-1.0, 1.0,  1.0],
    #         [-1.0, -1.0, -1.0], [1.0, -1.0, -1.0], [1.0, 1.0, -1.0], [-1.0, 1.0, -1.0], ]
    #faces = [[0,1,2,3], [0,4,5,1], [1,5,6,2], [2,6,7,3], [0,3,7,4], [4,7,6,5]]
    #colors = [[1.0,0.5,0.5,1.0]]*4+[[0.0,1.0,0.0,1.0]]*4+[[0.0,0.0,1.0,1.0]]*4+[[0.0,1.0,1.0,1.0]]*4+[[1.0,0.0,1.0,1.0]]*4+[[1.0,1.0,0.0,1.0]]*4

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