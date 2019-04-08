# Write a script with a UI that has a textField and a button, where the user
# can enter their name and hitting the button will print a welcome message, addressing
# the user by the name they entered.

# this will work only in maya (dunno why)

window = cmds.window( title="fuck my life", widthHeight=(400, 400) )
cmds.columnLayout( adjustableColumn=True )
ciao = cmds.textField(w=250)
cmds.button( label='Do Nothing', command=('print(cmds.textField(ciao, query=True, text=True))'))
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.setParent( '..' )
cmds.showWindow( window )