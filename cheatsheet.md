## Variables:

To assign a value to a variable, use the assignment operator (=)
Example: x = 5

## Data Types:
Integer: whole numbers (ex: 5, -2)
Float: decimal numbers (ex: 3.14, -0.5)
String: a sequence of characters (ex: "Hello World!")
Boolean: True or False
Lists: a collection of items (ex: [1, 2, 3])
Dictionaries: a collection of key-value pairs (ex: {"name": "John", "age": 30})

## Arithmetic Operators:

for addition
for subtraction
for multiplication
/ for division
** for exponentiation
% for modulus
// for floor division

## Comparison Operators:

== for equal to
!= for not equal to
for greater than

< for less than
= for greater than or equal to

<= for less than or equal to

## Logical Operators:

and for logical and
or for logical or
not for logical negation

## Conditional Statements:

if-elif-else:
if condition:
statements
elif condition:
statements
else:
statements

## Loops:

for loop:
for variable in range(start, stop):
statements
while loop:
while condition:
statements

## Functions:

To define a function, use the keyword def
Example: def function_name(parameters):
statements
To call a function, use the function name followed by parentheses and any necessary parameters
Example: function_name(parameters)
Input and Output:

To get input from the user, use the input() function
Example: x = input("Enter a number: ")
To print output, use the print() function
Example: print("The number is", x)

## Commonly used modules:

math: provides mathematical functions
random: provides random number generator
datetime: provides classes for manipulating dates and times
json: provides functions for working with JSON data
os: provides functions for interacting with the operating system
sys: provides access to interpreter specific functions

## Note : This is just a brief cheatsheet and not comprehensive. There are many other concepts in python like classes, modules, etc.

## Lists:

To access an item in a list, use the index number in square brackets
Example: my_list = [1, 2, 3]
print(my_list[0]) # prints 1
To add an item to a list, use the append() method
Example: my_list.append(4)
To insert an item at a specific index, use the insert() method
Example: my_list.insert(1, 5)
To remove an item from a list, use the remove() method or the pop() method
Example: my_list.remove(3) or my_list.pop()
To find the length of a list, use the len() function
Example: len(my_list)

## Dictionaries:

To access a value in a dictionary, use the key in square brackets
Example: my_dict = {"name": "John", "age": 30}
print(my_dict["name"]) # prints "John"
To add a key-value pair to a dictionary, use the assignment operator
Example: my_dict["gender"] = "male"
To change a value in a dictionary, use the assignment operator
Example: my_dict["age"] = 31
To remove a key-value pair from a dictionary, use the del keyword
Example: del my_dict["gender"]
To find the length of a dictionary, use the len() function
Example: len(my_dict)

## String manipulation:

To access a specific character in a string, use the index number in square brackets
Example: my_string = "Hello World!"
print(my_string[0]) # prints "H"
To concatenate two strings, use the + operator
Example: my_string = "Hello" + " World!"
To repeat a string, use the * operator
Example: my_string = "Hello" * 3
To slice a string, use the index numbers in square brackets
Example: my_string = "Hello World!"
print(my_string[6:11]) # prints "World"
To find the length of a string, use the len() function
Example: len(my_string)
To change the case of a string, use the lower() and upper() methods
Example: my_string = "Hello World!"
print(my_string.upper()) # prints "HELLO WORLD!"

## Exception handling:

To handle an exception, use the try-except block
Example:
try:
# code that may cause an exception
except ExceptionType:
# code to handle the exception

## Importing modules:

To use a module in a program, use the import keyword
Example: import math
To use a specific function from a module, use the from keyword and import keyword
Example: from math import sqrt
To give a module a different name, use the as keyword
Example: import math as m

## File handling:

To open a file, use the open() function
Example: my_file = open("example.txt", "r")