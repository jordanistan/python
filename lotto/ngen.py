# This script uses the itertools.combinations() function to generate all combinations of 5 numbers from the range 1 to 70. The combinations variable is an iterator that produces the combinations one by one.

# The script then opens a CSV file for writing and creates a csv.writer object to write the combinations to the file. The writerow() method is used to write each combination as a row in the CSV file.

# To generate all combinations of 6 numbers instead of 5, you can simply change the second argument of the combinations() function to 6.

# Note that this script generates a large number of combinations (26,535,300), so it may take some time to run. You may want to consider generating and writing the combinations in smaller batches or using a different approach if you need to process a very large number of combinations.

# Here is a sample script that demonstrates how to generate all combinations of numbers from 1 to 70 and export them to a CSV file using Python:

import itertools
import csv

# Generate all combinations of 5 numbers from 1 to 70
combinations = itertools.combinations(range(1, 71), 5)

# Open a CSV file for writing
with open("combinations.csv", "w", newline="") as csv_file:
    # Create a CSV writer
    writer = csv.writer(csv_file)

    # Write the combinations to the CSV file
    for combination in combinations:
        writer.writerow(combination)

print("Combinations written to combinations.csv")
