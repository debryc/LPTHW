def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # need colon
    """Prints the first word after popping it off."""
    word = words.pop(0) # misspelled pop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # add end parenthesis
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6 # six not 5
print "This should be five: %d" % five # changed string to integer

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 # changed back-slash to slash
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# one equal sign, not two, _ not -
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# crates, not crabapples
# end parenthesis and spell variable correctly
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# good not god
# wait not weight
sentence = "All good\tthings come to those who wait."

import ex25

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)

# remove period from beginning of line
print_first_word(sorted_words)
print_last_word(sorted_words)

sorted_words = ex25.sort_sentence(sentence)
print sorted_words # print not prin

print_first_and_last(sentence) # print

print_first_and_last_sorted(sentence) # and, not a, no tab; sentence not senence
