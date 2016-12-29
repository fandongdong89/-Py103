# %d  represents integer.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# %s represents string. And this is the first place where a string is put in a string.
y = "Those who know %s and those who %s." % (binary, do_not)


print x
print y


print "I said: %r." % x
# This is the second place.
print "I also said: '%s'." % y


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Third place
print joke_evaluation % hilarious


w = "This is the left side of..."
e = "a string with a right side."

# Forth place.
print w + e
# I think 'w+e'make a long string is because 'w' and 'e' are two string, and '+' in this sentence tells the computer to put them together. 
