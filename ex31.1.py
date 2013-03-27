print """
It's September and you're a college senior. 
Does 1, 2, or 3 describe your current career search the best?

1. I've already got a job offer in my pocket from a summer internship.
2. I'm not sure what I want to do, yet, so I guess I'll apply to consulting.
3. Career, what career? I'm going to travel the world.
"""

career = raw_input("> ")

if career == "1":
	
	print "Do you consider yourself a tool?"
	
	tool = raw_input("Yes or No? ")
	
	if tool == "Yes":
		print "At least you're honest with yourself."
	else:
		print "Who are you kidding?"

elif career == "2":

	print """
	Which of the following conditions best describes you?
	
	1. I'm doing what my friends are doing.
	2. I've tried to get more resources but couldn't find any.
	"""
	
	condition = raw_input("> ")
	
	if condition == "1":
		print "Search elsewhere!"
	
	else:
		print "Don't give up!"

elif career == "3":

	print """
	Oh cool, where?
	1. Helsinki
	2. Asia
	3. Everywhere
	4. Nowhere
	"""
	
	place = raw_input("> ")
	
	if place == "1":
		print "It's cold, bundle up."
		
	elif place == "2":
		print "You do know that's a huge place, right?"
		
	elif place == "3":
		print "Great, take me along!"
		
	else:
		print "Good luck with that."
		
else:

	print "Free."
