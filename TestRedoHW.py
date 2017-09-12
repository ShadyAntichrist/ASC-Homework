#!/usr/bin/python

name = raw_input("What is your name? ")
age = str(int(raw_input("What is your age? ")))
birthmonth = raw_input("What is your birthmonth? ")

with open("customers.txt", 'a') as file_name:
	file_name.write("Your name is %s\n" % name) 
	file_name.write("Your age is %s years old\n" % age) 
	file_name.write("Your month of birth is %s" % birthmonth) 
	file_name.close

print "So your name is %s, your age is %s years old, and your birthmonth is %s" % (name, age, birthmonth)

