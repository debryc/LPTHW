# challenge: run a function of mine in 10 different ways
def dating_age(age):
	print age / 2.0 + 7.0

# method 1
dating_age(16)

# method 2
my_age = 24
dating_age(my_age)

# method 3
dating_age(5 + 9)

# method 4
a = 5
b = 10
dating_age(a + b)

# method 5
dating_age(a * b)

# method 6
dating_age(a + 50)

# method 7
dating_age(b - a)

# method 8
print "Are you being targeted by a cougar?"
her_age = int(raw_input("How old is she?\n>"))
dating_age(her_age)

# method 9
dating_age(her_age - 4)

# method 10
your_age = int(raw_input("How old are you?\n>"))
dating_age(your_age)