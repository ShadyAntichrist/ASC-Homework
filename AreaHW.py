#!/usr/bin/python

length = int(raw_input("What is the length of your rectangle: "))
width = int(raw_input("What is the width of your rectangle: "))
area = length * width
perimeter = 2 * length + 2* width

print "So your width is %d and your length is %d" % (width, length)
print "If would like the area of your rectangle enter [1], [2] for perimeter, and [3] for both"

option = int(raw_input("> "))

while (option != 1 and option != 2 and option != 3):
	print "Please enter either [1] or [2] to continue"
	option = int(raw_input("> "))

if option == 1:
	print "The area of your rectangle is %d." % area

elif option == 2:
	print "The perimeter of your rectangle is %d." % perimeter

elif option == 3:
	print "The perimeter of rectangle is %d and the area is %d." % (perimeter, area)

