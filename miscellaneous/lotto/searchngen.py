# This script opens a CSV file for reading and creates a csv.reader object to read the rows of the file. It then iterates over the rows and converts each row to a list of integers using a list comprehension.

# For each row, the script checks if any of the numbers to search for are present in the row. If a number is found, it is printed to the console.

# You can customize the script by modifying the numbers_to_search variable to specify the numbers you want to search for, and by replacing "numbers.csv" with the name of your CSV file.

# Note that this is just a sample script and you may need to adjust it depending on the structure and format of your CSV file. For example, you may need to skip the header row or handle errors if the file does not contain the expected number of columns.

# Here is a sample script that demonstrates how to read a CSV file and search for certain numbers using Python:

import csv

# Set the numbers to search for
numbers_to_search = [1, 5, 10]

# Open the CSV file for reading
with open("numbers.csv", "r") as csv_file:
    # Create a CSV reader
    reader = csv.reader(csv_file)

    # Iterate over the rows in the CSV file
    for row in reader:
        # Convert the row to a list of integers
        numbers = [int(x) for x in row]

        # Check if any of the numbers to search for are present in the row
        for number in numbers_to_search:
            if number in numbers:
                print(f"Found {number} in row {row}")

print("Search complete.")
