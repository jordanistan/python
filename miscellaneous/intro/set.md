A set in Python is an unordered collection of unique elements. Sets are useful for storing data when you only need to know whether an element is present or absent, and you don't need to store any additional information about the element.

Here are five examples of using sets in Python:

## Creating a set:

```python
# Create a set with elements 1, 2, and 3
s = {1, 2, 3}
print(s)  # {1, 2, 3}

```

## Adding elements to a set:

```python
# Add an element to the set
s.add(4)
print(s)  # {1, 2, 3, 4}

```

## Removing elements from a set:

```python
# Remove an element from the set
s.remove(4)
print(s)  # {1, 2, 3}

```

## Checking the membership of an element in a set:

```python
# Check if the set contains the element 2
contains_2 = 2 in s
print(contains_2)  # True

# Check if the set contains the element 4
contains_4 = 4 in s
print(contains_4)  # False

```

## Iterating over a set:

```python
# Print the elements of the set
for element in s:
    print(element)

# Output:
# 1
# 2
# 3

```
