# Python Coding Interview Cheatsheet

## Basic Concepts
- **Dynamic Typing**: Variables can be reassigned to different types at runtime.
- **Indentation**: Python uses indentation to define blocks of code instead of curly braces.
- **Logical Operators**: Use `and`, `or`, and `not` instead of symbols like `&&` and `||`.
- **Division**: `/` for float division, `//` for integer division.
- **None**: Use `None` to represent null or the absence of a value.

## Variable Assignment
- **Multiple Assignments**: `a, b = 1, 2`
- **Type Reassignment**: `n = 0` then `n = "abc"` (types are determined at runtime)
- **Incrementing**: `n += 1` (no `++` operator)

## Conditionals and Loops
- **If Statements**: No parentheses needed; use colons and indentation.
  ```python
  if condition:
      # code block
  elif another_condition:
      # another code block
  else:
      # else block
  ```
- **While Loops**: Similar to if statements.
  ```python
  while condition:
      # code block
  ```
- **For Loops**:
  ```python
  for i in range(5):  # from 0 to 4
      # code block
  for i in range(2, 6):  # from 2 to 5
      # code block
  for i in range(5, 1, -1):  # from 5 to 2, decrementing
      # code block
  ```

## Lists (Arrays)
- **Initialization**: `nums = [1, 2, 3]`
- **Dynamic Arrays**: Use `append` and `pop`.
  ```python
  nums.append(4)
  nums.pop()  # removes last element
  ```
- **Slicing**: `nums[1:3]` (elements at index 1 and 2)
- **List Comprehension**: `[i for i in range(5)]` (creates `[0, 1, 2, 3, 4]`)
- **Unpacking**: `a, b, c = [1, 2, 3]`

## Strings
- **Initialization**: `s = "hello"`
- **Slicing**: `s[1:3]` (elements at index 1 and 2)
- **Immutable**: Strings cannot be modified directly; create new strings instead.
- **Conversion**: `int("123")` and `str(123)`

## Tuples
- **Initialization**: `t = (1, 2, 3)`
- **Immutability**: Cannot change elements once created.
- **Use in Dictionaries**: Can be keys in dictionaries.

## Dictionaries (HashMaps)
- **Initialization**: `d = {"a": 1, "b": 2}`
- **Access**: `d["a"]`
- **Modify**: `d["a"] = 10`
- **Remove**: `del d["a"]`
- **Comprehension**: `{i: i*2 for i in range(3)}` (creates `{0: 0, 1: 2, 2: 4}`)

## Sets
- **Initialization**: `s = {1, 2, 3}`
- **Add/Remove**: `s.add(4)` and `s.remove(3)`
- **Comprehension**: `{i for i in range(5)}`

## Functions
- **Definition**:
  ```python
  def my_function(param1, param2):
      # code block
      return result
  ```
- **Nested Functions**:
  ```python
  def outer_function(a, b):
      def inner_function(c):
          return a + b + c
      return inner_function(5)
  ```

## Classes
- **Definition**:
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def get_value(self):
          return self.value
  ```
- **Instance Methods**: Always include `self` as the first parameter.
- **Create Object**: `obj = MyClass(10)`

## Advanced Topics
- **Enumerate**:
  ```python
  for index, value in enumerate(nums):
      print(index, value)
  ```
- **Zip**:
  ```python
  for a, b in zip(list1, list2):
      print(a, b)
  ```
- **Heaps**:
  ```python
  import heapq
  heap = []
  heapq.heappush(heap, 3)
  heapq.heappop(heap)
  ```
- **Deque**:
  ```python
  from collections import deque
  dq = deque([1, 2, 3])
  dq.append(4)
  dq.appendleft(0)
  dq.pop()
  dq.popleft()
  ```

## One-Sentence Takeaway
Python's concise, dynamic syntax and powerful built-in features make it ideal for coding interviews and data manipulation.


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