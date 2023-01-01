import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage to scrape
url = "https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/Number_Frequency_Print.html_460673919.html"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find the table that contains the number frequency data
table = soup.find("table", {"class": "table"})

# Find all the rows in the table
rows = table.find_all("tr")

# Create a list of the top 20 sets of numbers
number_sets = []

# Skip the first row (header row)
for row in rows[1:]:
  # Find all the cells in the row
  cells = row.find_all("td")

  # Extract the data from the cells
  number = cells[0].text.strip()
  frequency = cells[1].text.strip()

  # Add the number to the list
  number_sets.append(number)

  # Stop when we have the top 20 numbers
  if len(number_sets) == 20:
    break

# Select the extra number from 1 to 25
extra_number = random.randint
