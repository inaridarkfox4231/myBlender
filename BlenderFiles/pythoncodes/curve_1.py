'''
閉じてないカーブはこれでいいみたい
'''

import bpy

def main():
  for i in range(0,10):
    bpy.ops.curve.vertex_add(location = (0,0,i))

if __name__ == "__main__":
  main()
