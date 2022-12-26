import requests
from bs4 import BeautifulSoup
import csv
import datetime

# Set the URL of the Craigslist page you want to scrape
url = "https://sfbay.craigslist.org/d/furniture/search/fua"

# Set the search query to look for leather couches
query = "leather couch"

# Set the maximum price you want to search for
max_price = 500

# Set the minimum age of the items you want to search for (in days)
min_age = 30

# Send a request to the Craigslist website and get the HTML response
response = requests.get(url, params={"query": query})

# Use BeautifulSoup to parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the items on the page
items = soup.find_all("li", class_="result-row")

# Open a CSV file to write the results
with open('craigslist_results.csv', 'w', newline='') as csvfile:
  # Create a CSV writer
  writer = csv.writer(csvfile)
  # Write the header row
  writer.writerow(['title', 'price', 'location', 'date'])

  # Iterate through the items and write the relevant information to the CSV file
  for item in items:
    title = item.find("a", class_="result-title").text
    price = item.find("span", class_="result-price").text
    location = item.find("span", class_="result-hood").text
    date_str = item.find("time", class_="result-date")["datetime"]
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M')

    # Check if the price is less than the maximum price and the item is older than the minimum age
    if price and int(price[1:]) <= max_price and (datetime.datetime.now() - date).days >= min_age:
      # Write the item's information to the CSV file
      writer.writerow([title, price, location, date_str])
