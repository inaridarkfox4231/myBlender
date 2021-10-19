import bpy

mat = bpy.data.materials['Material']

nodes = mat.node_tree.nodes

wav = nodes['Wave Texture']
ramp = nodes['ColorRamp']
mapp = nodes['Mapping']

# Wave Textureをいじる場合
# scale
wav.inputs[1].default_value = 0.5

# ColorRampをいじる場合
# leftColor:
ramp.color_ramp.elements[0].color = (0.9, 0.2, 0.5, 1.0)
# leftColorPosition
ramp.color_ramp.elements[0].position = 0.1
#rightColor:
ramp.color_ramp.elements[1].color = (0.1, 0.1, 0.8, 1.0)

#Mappingをいじる場合
for i in range(3):
    mapp.inputs[1].default_value[i] = (i+1)*(i+1)