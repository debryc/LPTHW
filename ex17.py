# import argv module from system, arguments from command line
from sys import argv
# import exists module from os.path
# exists module tests for existence of a file
from os.path import exists # ?

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

# write # of bytes in decimal point format using len function
# on the data in the from_file
print "The input file is %d bytes long" % len(indata)

# test to see if the to_file exists
# returns TRUE if the to_file exists, FALSE if the to_file does not exist
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# open to_file as file object out_file in write mode
out_file = open(to_file, 'w')
# write indata, the contents of the from_file to the to_file
out_file.write(indata)

print "Alright, all done."

# close the file object of the to_file
out_file.close()
# close the file object of the from_file
# in_file.close()