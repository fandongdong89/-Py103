# From L.2-9, definition about these specific nouns in L.13-20 are given.
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


# The output of 'cars' in L.12 will be '100' as defined in L.1.
print "There are", cars, "cars available."
# The output from L.14-18 will obey the same rule in L.12.
print "There are only", drivers,"drivers available."
# There is math in L.16-17 and L.19.
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
