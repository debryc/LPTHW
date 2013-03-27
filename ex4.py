# initialize variable cars and assign 100
cars = 100

# initialize variable space_in_a_car and assign 4.0 (floating point calculation)
space_in_a_car = 4.0

# initialize variable drivers and assign 30
drivers = 30

# initialize variable passengers and assign 90
passengers = 90

# initialize variable cars_not_driven and do calculation of cars - drivers because that's how many cars can't be driven. Each driven car has to have one driver per car.
cars_not_driven = cars - drivers

# initialize variable cars_driven and assign that to the value of drivers because each car needs one driver per car.
cars_driven = drivers

# initialize variable carpool_capacity and calculate how many people drivers can drive.
carpool_capacity = cars_driven * space_in_a_car

# initialize variable average_passengers_per_car and calculate how many passengers need to be in each car depending on cars_available.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."