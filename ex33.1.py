# Convert the while loop to a function that I can call
# and replace 6 in the test (i < 6) with a variable.

print "What integar do you want to start with?"
initial = int(raw_input("> "))

print "How much do you want to add each time to %i?" % initial
coefficient = int(raw_input("> "))

print "And how big do you want to number to get until you stop adding?"
limit_value = int(raw_input("> "))

print """
You chose to start with integer %d, 
going up by %d everytime, 
until you reach %d.""" % (initial, coefficient, limit_value)

numbers = []

def adduntil(start, step, limit, list):
	
	list = []
	
	while start < limit:
		print "At the top initial is %d" % start
		list.append(start)
		
		start = start + step
		print "Numbers now: ", list
		print "At the bottom initial is %d" % start
	
	print "The numbers: "
	
	for lis in list:
		print lis

adduntil(initial, coefficient, limit_value, numbers)
