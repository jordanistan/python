# To search for items on Craigslist for office chairs under $200 and export the results to a CSV file, you can use the BeautifulSoup library to scrape the Craigslist website and the csv library to write the results to a CSV file.
# This script will scrape the specified Craigslist page, find all the items on the page that match the search query for office chairs, and write the title, price, and location of the items that are under the specified maximum price to a CSV file.

# Note that this script is just an example and you may need to modify it to meet your specific needs. For example, you may want to search for items in a specific category or location, or you may want to extract additional information from the items.
# Here is an example of how you can do this:
import requests
from bs4 import BeautifulSoup
import csv
import datetime

# Set the URL of the Craigslist page you want to scrape
url = "https://austin.craigslist.org/search/austin-tx/fua?lat=30.242&lon=-97.769&query=office%20chair&search_distance=5.7#search=1~gallery~0~0"

# Set the search query to look for office chairs
query = "office chair"

# Set the maximum price you want to search for
max_price = 200

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
