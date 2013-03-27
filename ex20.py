# import arguments from command line
from sys import argv

# initialize variable input_file and assign to 
# name of file given in command line
script, input_file = argv

# define function print_all to read file object f
def print_all(f):
	print f.read()

# define function rewind to reset file object f to
# beginning
def rewind(f):
	f.seek(0)

# define function print_a_line to print line number
# and read that line of file object f
def print_a_line(line_count, f):
	print line_count, f.readline()

# create file object current_file from input_file
current_file = open(input_file)

# call function print_all using current_file
print "First let's print the whole file:\n"
print_all(current_file)

# call function rewind using current_file
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

# call function print_a_line given current_line = 1
current_line = 1
print_a_line(current_line, current_file)

# advance current_line by one
current_line = current_line + 1 # current_line = 2
# call function print_a_line given value of current_line
print_a_line(current_line, current_file)

# advance current_line by one
current_line = current_line + 1 # current_line = 3
# call function print_a_line given value of current_line
print_a_line(current_line, current_file)