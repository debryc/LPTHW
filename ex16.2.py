# Assignment: Write a script similar to the last exercise
# that uses read and argv to read the file you just created.

from sys import argv
script, filename = argv

txt = open(filename)

print txt.read()
txt.close()