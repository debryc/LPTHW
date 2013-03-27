# Now, write it to use for-loops and range instead.
# Do you need the incrementor in the middle anymore?
# What happens if you do not get rid of it?

print "What integer do you want to start with?"
initial = int(raw_input("> "))

print "What step do you want to go up by each time?"
coefficient = int(raw_input("> "))

print "And under what maximum value would you like to stop?"
limit = int(raw_input("> "))

print """
You want to start at %i
Go up by %i every time
and stop at or before %i.""" % (initial, coefficient, limit)

numbers = []

for i in range(initial, limit, coefficient):
	numbers.append(i)

for num in numbers:
	print num