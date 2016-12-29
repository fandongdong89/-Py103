from sys import argv

script, filename = argv

txt = open(filename)

print "Here's my newly created file %r:" % filename

print txt.read()
