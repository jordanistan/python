import random

def select_numbers():
  # Create an empty list to store the numbers
  numbers = []

  # Select the numbers
  for i in range(5):
    number = random.randint(1, 70)
    numbers.append(number)

  extra_number = random.randint(1, 25)

  # Return the selected numbers
  return numbers, extra_number

# Generate a list of 20 sets of numbers
number_sets = []
for i in range(20):
  numbers, extra_number = select_numbers()
  number_sets.append((numbers, extra_number))

# Print the list of number sets, with each set on a new line
for number_set in number_sets:
  print(number_set)

