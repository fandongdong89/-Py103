my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth


# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)


His_name = 'Zhou Hua'
His_age = 28.0 # not a lie
His_height = round(165.12) # centimeters
His_weight = 72.0 # kilograms
His_eyes = 'Blue'
His_teeth = 'White'
His_hair = 'Brown'

print "Let's talk about %s." % His_name
print "He's %r centimeters tall." % His_height
print "He's %d kilograms heavy." % His_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (His_eyes, His_hair)
print "His teeth are usually %s depending on the coffee." % His_teeth


# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
His_age, His_height, His_weight, His_age + His_height + His_weight)
