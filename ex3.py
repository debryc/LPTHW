print "I will now count my chickens:" # prints "I will now count my chickens:"

print "Hens", 25 + 30 / 6 # prints "Hens" and then lists the number of hens as a function of the calculation 25 + 30 / 6. Python follows order of operations so 30 / 6 = 5 and 25 + 5 = 30.
print "Roosters", 100 - 25 * 3 % 4 # prints "Roosters" and then lists the number of Roosters as a function of the calculation 100 - 25 * 3 % 4. Python follows order of operations so 25 * 3 = 75. 75 % 4 has a remainder of 3. 100 - 3 = 97.

print "Now I will count the eggs:" # prints "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4.0 + 6 # prints the number of eggs according to the function 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6. Python follows order of operations so 4 % 2 = 0. 1 / 4 = 0. 3 + 2 + 1 - 5 + 0 - 0 + 6 = 6.75. Python prints calculates 1 / 4 as 0 because it just drops the decimals in integer calculations.

print "Is it true that 3 + 2 < 5 - 7?" # prints "Is it true that 3 + 2 < 5 - 7?


print 3 + 2 < 5 - 7 # prints True if inequality is true and False if inequality is false.

print "What is 3 + 2?", 3 + 2 # prints 3 + 2
print "What is 5 - 7?", 5 - 7 # prints 5 - 7

print "Oh, that's why it's False." # prints "Oh, that's why it's False."

print "How about some more." # prints "How about some more."

print "Is it greater?", 5 > -2 # prints True because 5 is greater than -2
print "Is it greater or equal?", 5 >= -2 # prints True because 5 is greater than or equal to -2
print "Is it less or equal?", 5 <= -2 # prints False because 5 is not less than or equal to -2
