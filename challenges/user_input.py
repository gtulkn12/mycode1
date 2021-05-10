#!/usr/bin/python3
# print question
day= input("What day of the week is it?\n>")
name= input("What is your name?\n>")
print(f"Hello, {name}! Happy {day}!")


# PRINT OBJECTS
print("Hello, ",name,"! Happy ",day,"!", sep="")
# CONCATENATION
print("Hello, " + name + "! Happy " + day + "!")
# FORMAT METHOD
print("Hello, {}! Happy {}!".format(name, day))
# F-STRING
print(f"Hello, {name}! Happy {day}!")

