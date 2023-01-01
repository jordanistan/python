import requests
from bs4 import BeautifulSoup
import sys

# # Get the item and price from the command line arguments
# item = sys.argv[1]
# price = int(sys.argv[2])

# Function to search Craigslist for a specific item under a specific price
def search_items(item, price):
  # Set the search query to look for the specified item under the specified price
  query = f"{item} under ${price}"

  # Send a GET request to the Craigslist search URL
  response = requests.get(f"https://www.craigslist.org/search/sss?query={query}")

  # Check if the request was successful
  if response.status_code == 200:
    # Parse the response HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the "result-row" divs in the HTML
    results = soup.find_all("div", class_="result-row")

    # Iterate through the results
    for result in results:
      # Find the title and price of the item
      title = result.find("a", class_="result-title").text
      item_price = result.find("span", class_="result-price").text

      # Print the title and price of the item
      print(f"{title}: {item_price}")
  else:
    # Print an error message if the request failed
    print("Error searching Craigslist")

# Call the search_items function
search_items(item, price)
