from vpython import *

scene = canvas(width=960, height=450, background=vec(2 / 3, 2 / 3, 2 / 3))
scene.forward = vec(0, -1, 0)

# unit： inch
p_length = 9 * 12  # pool length
p_width = 4.5 * 12  # pool width
thickness = 1
wall_height = 4
bag_size = 4.75
m_bag_size = 5  # according to the rule the middle hole is slightly bigger than corner ones

# Pool Top
my_green = vec(0.25, 0.6, 0.4)
GreenTop = box(pos=vec(0, 0, 0), size=vec(p_length + thickness * 2, 0, p_width + thickness * 2), color=my_green)

# Pool Sides
walls = []
GreenWidth1 = box(pos=vec(p_length / 2 + thickness / 2, wall_height / 2, 0),
                  size=vec(thickness, wall_height, p_width + thickness * 2), color=my_green)
walls.append(GreenWidth1)

GreenWidth2 = box(pos=vec(- p_length / 2 - thickness / 2, wall_height / 2, 0),
                  size=vec(thickness, wall_height, p_width + thickness * 2), color=my_green)
walls.append(GreenWidth2)

GreenLength1 = box(pos=vec(0, wall_height / 2, p_width / 2 + thickness / 2),
                   size=vec(p_length + thickness * 2, wall_height, thickness), color=my_green)
walls.append(GreenLength1)

GreenLength2 = box(pos=vec(0, wall_height / 2, - p_width / 2 - thickness / 2),
                   size=vec(p_length + thickness * 2, wall_height, thickness), color=my_green)
walls.append(GreenLength2)

# Holes
holes = []
# top, bottom; left, middle, right
HoleTL = cylinder(pos=vec(p_length / 2, 0, p_width / 2), size=vec(wall_height, bag_size, bag_size),
                  color=vec(0, 0, 0), axis=vec(0, 1, 0))
holes.append(HoleTL)

HoleTM = cylinder(pos=vec(0, 0, p_width / 2), size=vec(wall_height, m_bag_size, m_bag_size),
                  color=vec(0, 0, 0), axis=vec(0, 1, 0))
holes.append(HoleTM)

HoleTR = cylinder(pos=vec(- p_length / 2, 0, p_width / 2), size=vec(wall_height, bag_size, bag_size),
                  color=vec(0, 0, 0), axis=vec(0, 1, 0))
holes.append(HoleTR)

HoleBL = cylinder(pos=vec(p_length / 2, 0, - p_width / 2), size=vec(wall_height, bag_size, bag_size),
                  color=vec(0, 0, 0), axis=vec(0, 1, 0))
holes.append(HoleBL)

HoleBM = cylinder(pos=vec(0, 0, - p_width / 2), size=vec(wall_height, m_bag_size, m_bag_size),
                  color=vec(0, 0, 0), axis=vec(0, 1, 0))
holes.append(HoleBM)

HoleBR = cylinder(pos=vec(- p_length / 2, 0, - p_width / 2), size=vec(wall_height, bag_size, bag_size),
                  color=vec(0, 0, 0), axis=vec(0, 1, 0))
holes.append(HoleBR)

# Wood Rim
my_brown = vec(0.6, 0.3, 0)
WoodWidth1 = box(pos=vec(p_length / 2 + thickness / 2 + 1, wall_height / 2 + 1, 0),
                 size=vec(thickness, wall_height, p_width + thickness * 2 + 2), color=my_brown)

WoodWidth2 = box(pos=vec(- p_length / 2 - thickness / 2 - 1, wall_height / 2 + 1, 0),
                 size=vec(thickness, wall_height, p_width + thickness * 2 + 2), color=my_brown)

WoodLength1 = box(pos=vec(0, wall_height / 2 + 1, p_width / 2 + thickness / 2 + 1),
                  size=vec(p_length + thickness * 2 + 2, wall_height, thickness), color=my_brown)

WoodLength2 = box(pos=vec(0, wall_height / 2 + 1, - p_width / 2 - thickness / 2 - 1),
                  size=vec(p_length + thickness * 2 + 2, wall_height, thickness), color=my_brown)

# the baulk-line is 29 inches from one end
BaulkLine = box(pos=vec(p_length / 2 - 29, 0, 0),
                size=vec(0.1, 0.1, p_width), color=vec(0.7, 0.7, 0.7))

