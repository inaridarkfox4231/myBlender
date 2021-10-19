import bpy
from math import sin, cos, pi

obj = bpy.data.objects['Cube']
obj.animation_data_clear() # アニメーションのデータをクリアする

bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = 120 # フレームのスタートとエンドを設定する

keyframe_freq = 10 # とりあえず10フレームおきに打ってみる

nStart = bpy.context.scene.frame_start
nEnd = bpy.context.scene.frame_end

mat = obj.material_slots[0].material # オブジェクトからマテリアルを取得
# データパスはnode_tree.nodes["Principled BSDF"].inputs[0].default_value
# なので、それに従ってそこまでいく
baseColor = mat.node_tree.nodes["Principled BSDF"].inputs[0]

for t in range(nStart, nEnd + 1):
    if t % keyframe_freq != 0: continue
    bpy.context.scene.frame_set(t)
    # 位置を変える場合はlocationでアクセスする感じ
    obj.location.x = 3 * cos(t * 0.1)
    obj.location.y = 3 * sin(t * 0.1)
    obj.keyframe_insert(data_path="location")
    # オイラー角をいじるのでrotation_euler. rotationだと失敗する
    obj.rotation_euler.y = t * 0.1
    obj.rotation_euler.z = t * 0.06
    obj.keyframe_insert(data_path="rotation_euler")
    # baseColorをいじる場合はinput[0]まで下りて行ってそこのdefault_valueを操作する
    # 水色から白にグラデーションさせてみる
    ratio = t / (nEnd - nStart + 1)
    baseColor.default_value = (ratio, 0.3 + 0.7 * ratio, 1.0, 1.0)
    baseColor.keyframe_insert(data_path = "default_value")
    
# 実はdata_pathの他にframe=60などのオプションを付けることでframe移動しなくてもキーフレームを打てるが
# フレーム0の時の値が変わってしまうなど作業しづらくなるのでおすすめしない
    
bpy.context.scene.frame_set(0) # フレームを戻しておく

    
    
