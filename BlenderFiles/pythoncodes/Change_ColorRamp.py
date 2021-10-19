import bpy

mat = bpy.data.materials['Material']

nodes = mat.node_tree.nodes
print(nodes[0])
ramp = nodes['ColorRamp']
for i in range(4):
    print(ramp.color_ramp.elements[0].color[i])
    
# ColorRampのいじり方
    
ramp.color_ramp.elements[0].color = (1.0,0.5,0.0,1.0)
ramp.color_ramp.elements[1].position = 0.1