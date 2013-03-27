# define function cheese_and_crackers
# and variables cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print cheese_count in string as signed integer decimal
	print "You have %d cheeses!" % cheese_count
	# print boxes_of_crackers in string as signed integer decimal
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	# print with new line at end
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# call function cheese_and_crackers with values 20 and 30
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
# initialize variables and assign values
amount_of_cheese = 10
amount_of_crackers = 50

# call function cheese_and_crackers and feed it 
# variables with values
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# call function cheese_and_crackers and feed it
# math
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# call function cheese_and_crackers and feed it variables
# and math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)