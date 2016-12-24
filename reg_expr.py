import re

file_object = open("basics.txt")
data = file_object.read()
file_object.close()
first = re.match("Four", data)
liberty = re.search("Liberty", data)
