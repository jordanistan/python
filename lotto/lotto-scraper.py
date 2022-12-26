# 
# Here is a Python script that uses the BeautifulSoup library to scrape the Texas Lottery website for past Mega Millions winning numbers:

import csv
import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage to scrape
url = "https://www.texaslottery.com/export/sites/lottery/Games/Mega_Millions/index.html#PastResults"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find the table that contains the past winning numbers
table = soup.find("table", {"class": "past-results-table"})

# Create a CSV file to store the data
with open("winning_numbers.csv", "w", newline="") as csv_file:
  # Create a CSV writer
  writer = csv.writer(csv_file)

  # Write the header row
  writer.writerow(["Draw Date", "Winning Numbers", "Mega Ball", "Megaplier"])

  # Find all the rows in the table
  rows = table.find_all("tr")

  # Iterate over the rows
  for row in rows:
    # Find all the cells in the row
    cells = row.find_all("td")

    # Skip rows that do not have enough cells
    if len(cells) < 4:
      continue

    # Extract the data from the cells
    draw_date = cells[0].text.strip()
    winning_numbers = cells[1].text.strip()
    mega_ball = cells[2].text.strip()
    megaplier = cells[3].text.strip()

    # Write the data to the CSV file
    writer.writerow([draw_date, winning_numbers, mega_ball, megaplier])

print("Done!")

# This script sends a GET request to the Texas Lottery website and uses BeautifulSoup to parse the HTML content of the webpage. 
# It then finds the table that contains the past winning numbers, extracts the data from the table cells, and writes the data to a CSV file.