# line 2-4, use argv to get a filename.
from sys import argv

script, filename = argv
# new command 'open'.
txt = open(filename)

print "Here's your file %r:" % filename
# 输出文件里面的内容
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read
