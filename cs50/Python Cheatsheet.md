## Python Cheatsheet


## Variables
Variables in Python are created when you assign a value to them.
The assignment operator is =.

```python
x = 5
y = "Hello, World!"
z = [1, 2, 3]
```

## Data Types:
Python has several built-in data types, including:
Integer (int)
Floating-point (float)
String (str)
List (list)
Tuple (tuple)
Dictionary (dict)
You can check the data type of a variable using the type() function.

```python
x = 5
print(type(x)) # Output: <class 'int'>
```

## Arithmetic Operations:

Python supports the standard arithmetic operations:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modulus (%), returns the remainder of a division
Exponentiation (**)

```python
x = 5
y = 2
print(x + y) # Output: 7
print(x - y) # Output: 3
print(x * y) # Output: 10
print(x / y) # Output: 2.5
print(x % y) # Output: 1
print(x ** y) # Output: 25
```

## Control Flow:

Python uses indentation to indicate the scope of control flow statements, such as if, for, and while.
The if statement is used to control flow based on a boolean condition.
```python
x = 5
if x > 0:
    print("x is positive")
```
The for loop is used to iterate over a sequence (such as a list or string).

```python
for i in range(5):
    print(i) # Output: 0, 1, 2, 3, 4
```

The while loop is used to repeatedly execute a block of code as long as a condition is true.

```python
x = 5
while x > 0:
    print(x)
    x -= 1
```

## Functions

Functions in Python are defined using the def keyword, and can take one or more parameters.

```python
def greet(name):
    print("Hello, " + name + "!")
greet("John") # Output: Hello, John!
```

## Modules and Packages:

Python code can be organized into modules, which are files containing Python definitions and statements.
You can use the import statement to import a module and use its functions and variables.

```python
import math
print(math.sqrt(16)) # Output: 4.0
```
You can also use the from keyword to import specific functions or variables from a module.

```python
from math import sqrt
print(sqrt(16)) # Output: 4.0
```
Python also has a large number of

## Exception Handling:

Python uses try-except blocks to handle exceptions, which are raised when an error occurs.

```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## File Input/Output:

Python provides several ways to read and write files.
The open() function is used to open a file, and can take several modes, such as 'r' for reading, 'w' for writing, and 'a' for appending.

```python
f = open('example.txt', 'w')
f.write('Hello, World!')
f.close()
```
The with statement can also be used to automatically close a file after it is used.


```python
with open('example.txt', 'r') as f:
    print(f.read())
```

The read() function reads the entire file, while the readline() function reads a single line.

## List comprehension:

List comprehension is a concise way to create a list in Python.

```python
squares = [x**2 for x in range(5)]
print(squares) # Output: [0, 1, 4, 9, 16]
```

## Lambda function:

Lambda function is an anonymous function in Python.

```python
double = lambda x: x*2
print(double(5)) # Output: 10
```

## Zip and Enumerate

zip() is used to combine two or more iterable objects together and enumerate() adds a counter to an iterable and returns it in a form of enumerate object.

```python
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
#zip three lists
combined_list = list(zip(x, y, z))
#iterate over the enumerated object
for index, val in enumerate(combined_list):
    print(index, val)
```

## Map and Filter

map() applies a function to all elements in an input list and filter() filters the elements of an iterable for which the given function returns True.

```python
numbers = [1, 2, 3, 4, 5]
# using map
square_list = list(map(lambda x: x**2, numbers))
print(square_list) # Output: [1, 4, 9, 16, 25]
#using filter
even_list = list(filter(lambda x: x%2==0, numbers))
print(even_list) # Output: [2, 4]
```

## String manipulation

Python provides several ways to manipulate strings, such as string concatenation, slicing, and formatting.

```python
name = "John"
age = 30
#string concatenation
print("My name is " + name + " and I am " + str(age) + " years old.")
#string slicing
print(name[1:
```

## Regular Expressions:

Python provides a module called re for working with regular expressions.

```python
import re
#search for pattern in a string
match = re.search(r'\d{3}-\d{2}-\d{4}', 'The SSN is 123-45-6789')
print(match.group()) # Output: '123-45-6789'
```

## Date and Time:

Python provides a module called datetime for working with dates and times.

```python
from datetime import datetime
#current date and time
now = datetime.now()
print(now) # Output: "2022-11-20 12:30:55.173961"
#formatting date and time
print(now.strftime("%Y-%m-%d %H:%M:%S")) # Output: "2022-11-20 12:30:55"
```

## JSON
Python provides a module called json for working with JSON data.

```python
import json
#convert python object to json
data = {'name': 'John', 'age': 30}
json_data = json.dumps(data)
print(json_data) # Output: {"name": "John", "age": 30}
#convert json to python object
python_data = json.loads(json_data)
print(python_data) # Output: {'name': 'John', 'age': 30}
```

## Decorators
Python decorators are used to modify the behavior of a function without changing its code.

```python
def my_decorator(func):
def wrapper():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called.")
return wrapper
@my_decorator
def say_hello():
    print("hello!")
say_hello()
# Output: Something is happening before the function is called.
#         hello!
#         Something is happening after the function is called.
```

## Generators
Python generators are used to create iterators.

```python
def my_gen():
n = 1
print("This is printed first")
yield n
n += 1
print("This is printed second")
yield n
n += 1
print("This is printed at last")
yield n
a = my_gen()
next(a)
/ Output: This is printed first
/         1
next(a)
/ Output: This is printed second
/         2

```

## Context Managers:

Python context managers are used to simplify the process of acquiring and releasing resources.


```python
with open('example.txt', 'r')
```




## 

```python

```

## 

```python

```

## 

```python

```


## 

```python

```


## 

```python

```

