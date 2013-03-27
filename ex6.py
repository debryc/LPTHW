# initialize variable x as string with integer type insert of 10
x = 'There are %d types of people.' % 10

# initialize variable binary as string binary
binary = "binary"

# initialize variable do_not as string don't
do_not = "don't"

# initialize variable y as string with string type and insert variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# print variables x and y
print x
print y

# print whatever x is.
print "I said: %r." % x

# print whatever y is, need quotes.
print "I also said: '%s'." % y

# initialize variable hilarious as boolean False
hilarious = False

# initialize joke_evaluation variable as string
joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation variable with value of variable hilarious inserted
print joke_evaluation % hilarious

# initialize variables as strings
w = "This is the left side of..."
e = "a string with a right side."

# print a concatenation of strings
print w + e