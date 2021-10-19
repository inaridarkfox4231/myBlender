'''
はい。
閉曲線を作るスクリプトはこれで良さそう
時間ないのでおしまい
だから手順としては
1:閉曲線を作る
2:メッシュにする
3:それを押し出して好きな形状に伸ばす
って感じじゃない。
'''

import bpy
from math import pi, cos, sin

def main():

  # 最初に、プリミティブを作って編集に行ってそれ削除して、ってのを追加
  bpy.ops.curve.primitive_bezier_curve_add()
  bpy.ops.object.editmode_toggle()
  bpy.ops.curve.delete(type='VERT')

  # ここからがメインスクリプト
  for i in range(0,40):
    t = 2 * pi * i / 40
    x = 4 * cos(t)
    y = 3 * sin(t)
    z = t / 2
    bpy.ops.curve.vertex_add(location = (x, y, z))
  # カーブが作れたらすべての頂点を選択する
  bpy.ops.curve.select_all(action='SELECT')

  # なるほど、これで頭とおしりがくっつくわけね。
  # 日本語使えるんかな・・貼り付けるしかなさそう。
  # https://docs.blender.org/api/current/bpy.ops.curve.html#bpy.ops.curve.select_all
  # https://docs.blender.org/api/current/bpy.ops.curve.html#bpy.ops.curve.make_segment

  bpy.ops.curve.make_segment()
  # 作成し終わったら選択解除
  bpy.ops.curve.select_all(action='DESELECT')
  # オブジェクトモードに戻す
  bpy.ops.object.editmode_toggle()

if __name__ == "__main__":
  main()