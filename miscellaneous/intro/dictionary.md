A dictionary in Python is a collection of key-value pairs. It is an unordered data type that is mutable, meaning that you can change the contents of a dictionary after it has been created. Dictionaries are often used to store data that needs to be quickly retrieved using a unique key.

Here are five examples of using dictionaries in Python:

## Creating a dictionary:

```python
# Create a dictionary with key-value pairs
phone_book = {'Alice': '555-1234', 'Bob': '555-5678', 'Charlie': '555-9101'}
print(phone_book)  # {'Alice': '555-1234', 'Bob': '555-5678', 'Charlie': '555-9101'}

```


## Accessing values in a dictionary:

```python
# Get the phone number for 'Bob' from the phone book
phone_number = phone_book['Bob']
print(phone_number)  # '555-5678'

```


## Modifying values in a dictionary:

```python
# Update the phone number for 'Bob' in the phone book
phone_book['Bob'] = '555-2468'
print(phone_book)  # {'Alice': '555-1234', 'Bob': '555-2468', 'Charlie': '555-9101'}

```


## Adding new key-value pairs to a dictionary:

```python
# Add a new entry to the phone book
phone_book['David'] = '555-3333'
print(phone_book)  # {'Alice': '555-1234', 'Bob': '555-2468', 'Charlie': '555-9101', 'David': '555-3333'}

```


## Iterating over a dictionary:

```python
# Print the keys and values of the phone book
for name, phone in phone_book.items():
    print(f"{name}: {phone}")

# Output:
# Alice: 555-1234
# Bob: 555-2468
# Charlie: 555-9101
# David: 555-3333

```