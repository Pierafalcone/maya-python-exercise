# Write a script that will create 3 polySpheres and 3 polyCubes.
# The 3 polySphere should be place 5 units from each other in X. but not moved in Y or Z.
# The 3 polyCubes should be on top of the spheres in the viewport (3 units above)
# The first cube should have a red lambert material assigned to it,
# The second cube should have a green lambert material assigned to it
# The third cube should have a blue blinn material assigned to it.
# Put comments in your code for documentation...

cubes = []

for i in range(3):
    # Create the spheres
    cmds.polySphere()
    cmds.move((i*5), 0, 0)
    # Create cube and add to cubes list
    cubes.append(cmds.polyCube())
    cmds.move((i*5), 3, 0)
            
red_mat = cmds.shadingNode('lambert', asShader=True) 
cmds.setAttr((red_mat + '.color'), 1.0, 0.0, 0.0, type = 'double3')
# Gets the shape of the first cube
cmds.select(maya.cmds.listRelatives(cubes[0])[0])   
cmds.hyperShade(assign=red_mat)

green_mat = cmds.shadingNode('lambert', asShader=True)
cmds.setAttr((green_mat + '.color'), 0.0, 1.0, 0.0, type = 'double3')
# Gets the shape of the second cube
cmds.select(maya.cmds.listRelatives(cubes[1])[0])
cmds.hyperShade(assign=green_mat)

blue_mat = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr((blue_mat + '.color'), 0.0, 0.0, 1.0, type = 'double3')
# Gets the shape of the third cube
cmds.select(maya.cmds.listRelatives(cubes[2])[0])
cmds.hyperShade(assign=blue_mat)