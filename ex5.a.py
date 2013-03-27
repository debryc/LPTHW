name = 'Deborah Chang'
age = 24
height_in = 65 # inches
weight_lb = 120 # lbs
eyes = 'brown'
teeth = 'white'
hair = 'black'

height_cm = height_in * 2.54
weight_kg = weight_lb * 0.453592

print "Let's talk about %s" % name
print "She's %d inches tall." % height_in
print "She's %d centimeters tall." % height_cm
print "She's %f pounds heavy." % weight_lb
print "She's %f kilograms heavy." % weight_kg
print "She's got %s eyes and %s hair." % (eyes, hair)
print "If I add %.1f, %.1f, and %.1f I get %.1f." % (
	age, height_in, weight_kg, age + height_in + weight_kg)