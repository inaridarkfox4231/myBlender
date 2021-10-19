import bpy
from mathutils import Color
from math import sin, cos, pi

'''
"vec3 getRGB(float h, float s, float b){" +
"    vec3 c = vec3(h, s, b);" +
"    vec3 rgb = clamp(abs(mod(c.x * 6.0 + vec3(0.0, 4.0, 2.0), 6.0) - 3.0) - 1.0, 0.0, 1.0);" +
"    rgb = rgb * rgb * (3.0 - 2.0 * rgb);" +
"    return c.z * mix(vec3(1.0), rgb, c.y);" +
"}" +
'''

def main():

    verts = []
    faces = []
    colors = []
    
    m = 20
    n = 20

    msh = bpy.data.meshes.new(name="cubemesh")
    msh.vertex_colors.new(name="myColor")

    verts.append([0, 0, 1])
    for i in range(1, n + 1):
        for k in range(m):
            theta = pi * i / (n + 1)
            phi = 2 * pi * k / m
            verts.append([sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)])
    verts.append([0, 0, -1])
    
    # mathutilsには様々な機能があるけど今回使うのは
    # hsvのやつ。Color()でインスタンスを作り、使い回す。
    # col.hsv=(h,s,v)でhsvでの表示を用意して
    # rgbでアクセスして放り込めばいいので楽ちん!
    
    col = Color()

    for k in range(1, m + 1):
        faces.append([0, k, 1 + (k % m)])
        col.hsv = (0.55, 1, 1)
        for id in range(3):
            colors.append([col.r, col.g, col.b, 1.0])

    for i in range(n - 1):
        for k in range(1, m + 1):
            faces.append([i * m + k, (i + 1) * m + k, (i + 1) * m + 1 + (k % m), i * m + 1 + (k % m)])
            col.hsv = (0.55, 0.5 + 0.5 * cos(pi * i / (n - 1)), 1.0)
            for id in range(4):
                colors.append([col.r, col.g, col.b, 1.0])

    for k in range(1, m + 1):
        faces.append([(n - 1) * m + k, n * m + 1, (n - 1) * m + 1 + (k % m)])
        col.hsv = (0.55, 0, 1)
        for id in range(3):
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