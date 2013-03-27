# import argument from command line
from sys import argv

# initialize the variable filename and
# assign it to the argument from the command line
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# allow user to input ^C to cancel or RETURN to continue
# use raw_input to have a pause in the program
raw_input("?")

print "Opening the file..."
# make file object target by opening filename with
# parameter w
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# truncate the target file with no parameters
target.truncate()

print "Now I'm going to ask you for three lines."

# initialize variables line1-line3 
# and assign it to raw_input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write contents of line1-line3 to file object target
# with a new line for each
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it."
# close the file object target
target.close()