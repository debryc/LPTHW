from sys import argv

script, filename = argv
target = open(filename, "w")

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Now I'm going to write these three lines to the file."
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# Open file for reading, not just writing
target = open(filename, "r")
print target.read()

target.close