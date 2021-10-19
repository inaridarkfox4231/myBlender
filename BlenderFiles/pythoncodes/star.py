import bpy
from math import pi, cos, sin

x=[]
y=[]
N=640
for i in range(N):
    t = 2 * pi * i / N
    x.append(15 * cos(11*t)- 10 * sin(7*t))
    y.append(15 * sin(11*t)- 10 * cos(7*t))
    
for i in range(N-1):
    bpy.ops.mesh.extrude_region_move(
    TRANSFORM_OT_translate={"value":(x[i+1]-x[i],y[i+1]-y[i],0)})