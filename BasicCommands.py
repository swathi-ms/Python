print("Hello Swathi!")
if 5 > 2:
    print("five is greater than 2")

# trying to remember all the basic commands

""" multiple line comment"""

x = 5
y = "John"
print(type(x))
print(type(y))
    
# Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
Python allows you to assign values to multiple variables in one line
"""

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


print("Hello, World!")
if 5 > 2:
    print ("5 is greater than 2")

x = 5
y = "Hello World"
# this is a comment
""" Multi line comment
good to know
"""

x = 5
y = "John"
print(x)
print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
print(type(y))
print(type(z))

#String variables can be declared either by using single or double quotes:
"""A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords"""

"""
x = 5
y = "John"
print(x + y)"""


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""