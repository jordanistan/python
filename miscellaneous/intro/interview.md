Here are 10 examples of problems you might encounter in a Python coding interview, along with explanations and solutions written in a way that should be easy for someone who is new to programming to understand.

Write a function that takes a list of numbers and returns the sum of all the numbers.
```python

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
```

Write a function that takes a string and returns a new string with all the vowels (a, e, i, o, u) removed.
```python

def remove_vowels(string):
    vowels = 'aeiou'
    new_string = ''
    for character in string:
        if character.lower() not in vowels:
            new_string += character
    return new_string
```

Write a function that takes a list of strings and returns a new list with all the strings that are longer than 5 characters.
```python

def get_long_strings(strings):
    long_strings = []
    for string in strings:
        if len(string) > 5:
            long_strings.append(string)
    return long_strings
```

Write a function that takes a list of numbers and returns the smallest number in the list.
```python

def get_smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
```
Write a function that takes a list of words and returns a new list with all the words sorted in alphabetical order.
```python

def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words
```
Write a function that takes a list of numbers and returns True if the list contains any even numbers, and False otherwise.
```python

def has_even_number(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
    return False
```
Write a function that takes a list of words and a letter, and returns a new list with all the words that start with that letter.
```python

def get_words_starting_with(words, letter):
    starting_with = []
    for word in words:
        if word[0] == letter:
            starting_with.append(word)
    return starting_with
```

Write a function that takes a list of numbers and returns a new list with all the numbers squared (raised to the power of 2).
```python

def square_numbers(numbers):
    squared = []
    for number in numbers:
        squared.append(number**2)
    return squared
```

Write a function that takes a list of words and returns a new list with all the words that have at least 3 vowels.
```python

def get_words_with_many_vowels(words):
    many_vowels = []
    for word in words:
        vowel_count = 0
        for letter in word:
            if letter in 'aeiouAEIOU':
                vowel_count += 1
        if vowel_count >= 3:
            many_
```