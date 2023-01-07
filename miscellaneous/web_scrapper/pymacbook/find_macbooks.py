import requests
from bs4 import BeautifulSoup

# Set the location and search keyword
location = 'austin-tx'
keyword = 'macbook'

# Set the base URL and the parameters for the HTTP request
base_url = 'https://{}.craigslist.org/search/sss?query={}'.format(location, keyword)
params = {
    'min_price': '100',
    'max_price': '2000'
}

# Send the HTTP request and get the response
response = requests.get(base_url, params=params)

# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the ads on the page
ads = soup.find_all('li', class_='result-row')

# Iterate over the ads
for ad in ads:
    # Extract the title, price, and location
    title = ad.find('a', class_='result-title').text
    price = ad.find('span', class_='result-price').text
    location = ad.find('span', class_='result-hood').text
    
    # Print the information for each ad
    print(title)
    print(price)
    print(location)
    print()