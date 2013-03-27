# print question and add comma to prevent new line after printing
print "How old are you?",

# initialize variable age as whatever someone inputs
age = raw_input()

print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# print inputs
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
# using %r prints '5\'5"' instead of 5'5" because the escape key is 
# needed in programming to allow printing ' instead of closing the string.