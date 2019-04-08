# Write a script that based on selection will print how many objects / nodes the user
# has selected.

selected = cmds.ls(sl=True,long=True) or []
print('selected things: ' + str(len(selected)))
for eachSel in selected:
   print(eachSel)