<!-- In these examples, the first loop uses a for loop to iterate over a list of numbers and print each element. The second loop uses a while loop to repeat an action until a condition is met. The third loop uses a for loop to iterate over a dictionary and print each key-value pair. The fourth loop uses a for loop to iterate over a string and print each character. The fifth loop uses a nested loop to iterate over a list of lists and print each element.
Here is an example of how to use a loop in Python, along with five examples of different types of loops: -->

# Use a for loop to iterate over a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
  print(number)

# Use a while loop to repeat an action until a condition is met
count = 0
while count < 10:
  print(count)
  count += 1

# Use a for loop to iterate over a dictionary
employees = {
  'Alice': 'Manager',
  'Bob': 'Developer',
  'Charlie': 'Salesperson'
}
for employee, role in employees.items():
  print(f"{employee} is a {role}")

# Use a for loop to iterate over a string
string = "Hello, World!"
for char in string:
  print(char)

# Use a nested loop to iterate over a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
  for element in row:
    print(element)
