from sys import argv

script, user_name = argv
prompt = "> "

print "Hi %s, welcome to Adventureland." % user_name
print """Which direction would you like to move in?
	North
	South
	East
	or West?"""
direction = raw_input(prompt)
print """And which tool would you like to bring with you?
	a knife
	a gun
	or a lasso?"""
tool = raw_input(prompt)

print """
You have chosen to walk %s with %s.""" % (direction, tool)