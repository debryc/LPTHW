# define function add as print adding a + b
# and return a + b to be assigned to variable
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# define function subtract as print a - b
# and return the result to be assigned to variable
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

# define function multiply as print a * b
# and return the result to be assigned to variable
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

# define function divide as print a / b
# and return the result to be assigned to variable
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

# call functions and assign to variables
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# extra credit question 2 and 3

def extra_credit_function(a, b, c, d):
	print "Figuring out the normal function."
	return c - ( a / 2 * b ) + d

what_2 = extra_credit_function(iq, weight, height, age)

print what_2

# extra credit question 4
# common formula P = (nRT)/V

pressure = divide(multiply(3.0, multiply(1, 2)), 4)
print pressure