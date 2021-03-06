import bpy

# 何はともあれオブジェクトを取得
obj = bpy.data.objects['Cube']
# dataでメッシュを取得できる
msh = obj.data

# 頂点どんな感じ？
for vt in msh.vertices:
    print("vertex index:{0:2} co:{1} normal:{2}".format(vt.index, vt.co, vt.normal))
'''
vertex index: 0 co:<Vector (-1.0000, -1.0000, -1.0000)> normal:<Vector (-0.5773, -0.5773, -0.5773)>
vertex index: 1 co:<Vector (-1.0000, -1.0000, 1.0000)> normal:<Vector (-0.5773, -0.5773, 0.5773)>
vertex index: 2 co:<Vector (-1.0000, 1.0000, -1.0000)> normal:<Vector (-0.5773, 0.5773, -0.5773)>
vertex index: 3 co:<Vector (-1.0000, 1.0000, 1.0000)> normal:<Vector (-0.5773, 0.5773, 0.5773)>
vertex index: 4 co:<Vector (1.0000, -1.0000, -1.0000)> normal:<Vector (0.5773, -0.5773, -0.5773)>
vertex index: 5 co:<Vector (1.0000, -1.0000, 1.0000)> normal:<Vector (0.5773, -0.5773, 0.5773)>
vertex index: 6 co:<Vector (1.0000, 1.0000, -1.0000)> normal:<Vector (0.5773, 0.5773, -0.5773)>
vertex index: 7 co:<Vector (1.0000, 1.0000, 1.0000)> normal:<Vector (0.5773, 0.5773, 0.5773)>
'''
# このようにx,y,zの順に比較して小さい順（辞書式）

# 頂点の色は？
# 24と出た・・そうか、やっぱポリゴンごとの彩色になってるみたいね。んー。
print('---------------------------------')
print(msh.vertex_colors['Col'].data)
for vc in msh.vertex_colors['Col'].data:
    _col = vc.color
    print("{0}, {1}, {2}, {3}".format(_col[0],_col[1],_col[2],_col[3]))
# 24と出た・・そうか、やっぱポリゴンごとの彩色になってるみたいね。んー。
# 面ごとの彩色ね。
# じゃあちょっとチュートリアルに沿って色付けてみますかね
# 全部黄色！！
for vc in msh.vertex_colors['Col'].data:
    vc.color[0]=0
    vc.color[1]=1
    vc.color[2]=1
    vc.color[3]=1

