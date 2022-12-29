<!-- This script uses the requests library to send a request to a URL and get the response, and the BeautifulSoup library to parse the HTML content of the response. It then uses the find_all() method of BeautifulSoup to find all the span elements in the HTML and extract the text content of each element. If the text content is a number, it is added to the list of numbers.

The script then opens a CSV file for reading and reads the rows of the file, adding the numbers from the file to the list as well.

Here is a sample script that demonstrates how to scrape a website and read a CSV file to find the numbers that show up the most using Python: -->

import csv
import requests
from bs4 import BeautifulSoup

# Set the URL to scrape
url = "https://www.example.com"

# Send a request to the URL and get the response
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# Find all the numbers in the HTML content
numbers = [int(x.text) for x in soup.find_all("span") if x.text.isdigit()]

# Open the CSV file for reading
with open("numbers.csv", "r") as csv_file:
    # Create a CSV reader
    reader = csv.reader(csv_file)

    # Read the rows of the CSV file and add the numbers to the list
    for row in reader:
        numbers += [int(x) for x in row]

# Count the frequency of each number
counts = {}
for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

# Find the number with the highest frequency
most_common = max(counts, key=counts.get)

print(f"The most common number is {most_common} with {counts[most_common]} occurrences.")
