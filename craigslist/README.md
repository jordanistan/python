<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Scrape Craigslist for items" />

  &#xa0;

  <!-- <a href="https://Scrape Craigslist for items.netlify.app">Demo</a> -->
</div>

<h1 align="center">Scrape Craigslist for items</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jordanistan/python-1?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jordanistan/python-1?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jordanistan/python-1?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/jordanistan/python-1?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/jordanistan/python-1?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/jordanistan/python-1?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/jordanistan/python-1?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Scrape Craigslist for items 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/jordanistan" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

To write a Dockerfile with a Python script to search Craigslist for a specific item under a specific price, you can use the FROM and COPY directives to include the necessary dependencies and files in the Docker image. Here is an example of how you could do this:

```bash
# Use the official Python image as the base image
FROM python:3

# Install the requests and beautifulsoup4 libraries
RUN pip install requests beautifulsoup4

# Copy the search_items.py script to the Docker image
COPY search_items.py /app/search_items.py

# Set the working directory to the app directory
WORKDIR /app

# Run the search_items.py script when the Docker container starts
CMD ["python", "search_items.py"]

```

The search_items.py script should contain the code to search Craigslist for a specific item under a specific price, using the requests and beautifulsoup4 libraries. Here is an example of what the script might look like:

```bash
import requests
from bs4 import BeautifulSoup
import sys

# Get the item and price from the command line arguments

item = sys.argv[1]
price = int(sys.argv[2])


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
```

This will build the Docker image using the specified Dockerfile and search_items.py script, and will run the script inside a Docker container, passing the specified item and price as command line arguments. The script will search Craigslist for the specified item under the specified price and print the results to the console.


## :sparkles: Features ##

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies ##



## :white_check_mark: Requirements ##


## :checkered_flag: Starting ##


To build the Docker image and run the script, you can use the following commands:

```bash
# Download the code
git clone blah
cd blah
# Build the Docker image
docker build -t craigslist-search .

# Run the Docker container, specifying the item and price as command line arguments

docker run craigslist-search safe 300
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/jordanistan" target="_blank">Jordanistan</a>

&#xa0;

<a href="#top">Back to top</a>
