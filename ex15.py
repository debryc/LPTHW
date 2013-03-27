# parse arguments from the command line
from sys import argv

# there will be one argument
# initialize and assign that argument to variable filename
script, filename = argv

# initialize txt variable and assign the file object filename
txt = open(filename)

# print the name of the file object
print "Here's your file %r:" % filename
# print the contents of the file by giving it the
# read command with no parameters
print txt.read()

# print the string "Type the filename again:"
# initialize variable file_again and assign value
# given through raw_input with prompt >
print "Type the filename again:"
file_again = raw_input("> ")

# initialize text variale and assign the file object file_again
txt_again = open(file_again)

# print the contents of file_again using read command
print txt_again.read()