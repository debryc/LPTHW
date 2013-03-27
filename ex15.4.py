from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your %r file: " % filename
print txt.read()

# Why doesn't the script stop and ask me for another argument?
print "Write the file name in the command line again."
from sys import argv

script, filename_again = argv

txt_again = open(filename_again)

print "Here's your %r file again: " % filename
print txt_again.read()