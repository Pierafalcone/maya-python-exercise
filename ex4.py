# Make a copy of the script above and modify the copy so that it now prints
# how many joints are selected, how many meshes are selected and how many transforms
# are selected.

selected_joint = cmds.ls(sl=True, long=True, type='joint')
print('selected joint: ' + str(len(selected_joint)))

selected_mesh = cmds.ls(sl=True, long=True, type='mesh')
print('selected mesh: ' + str(len(selected_mesh)))

selected_transform = cmds.ls(sl=True, long=True, type='transform')
print('selected transform: ' + str(len(selected_transform)))
