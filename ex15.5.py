filename = raw_input(
	"What file do you want to open and read?: ")
txt = open(filename)

print "Here's your %r file: " % filename
print txt.read()

filename_again = raw_input(
	"What file do you want to open and read again?: ")
txt_again = open(filename_again)

print "Here's your %r file again: " % filename
print txt_again.read()

# Using raw_input instead of command line arguments
# is better for users who need the prompting. Using
# command line arguments instead of raw_input useful
# for speed.

txt.close()
txt_again.close()