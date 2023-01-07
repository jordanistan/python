# Install the required libraries:
# requests: a library for sending HTTP requests
# bs4: a library for parsing HTML
# slack-sdk: a library for interacting with the Slack API
# You can install these libraries by running the following command:

# pip install requests bs4 slack-sdk




import requests
import bs4
import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set the Craigslist search URL
url = "https://austin.craigslist.org/search/sss?query=macbook"

# Set the minimum and maximum price range
min_price = 1000
max_price = 2000

# Send a request to the Craigslist search URL
response = requests.get(url)

# Parse the response as HTML
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# Find all the ads on the search results page
ads = soup.find_all('li', {'class': 'result-row'})

# Iterate through the ads
for ad in ads:
  # Find the price of the ad
  price_element = ad.find('span', {'class': 'result-price'})
  if price_element:
    # Extract the price from the element
    price = int(re.sub(r'[^\d]', '', price_element.text))
    # Check if the price is within the specified range
    if price >= min_price and price <= max_price:
      # Find the title of the ad
      title_element = ad.find('a', {'class': 'result-title'})
      if title_element:
        # Extract the title from the element
        title = title_element.text
        # Send a notification to Slack
        try:
          # Set the Slack API token
          client = WebClient(token='YOUR_SLACK_API_TOKEN')
          # Send a message to the specified Slack channel
          response = client.chat_postMessage(
            channel='#YOUR_SLACK_CHANNEL',
            text=f'Found a Macbook for ${price} on Craigslist: {title}'
          )
        except SlackApiError as e:
          # Print the error message if the notification failed
          print("Error sending message: {}".format(e))
          
# Replace YOUR_SLACK_API_TOKEN with your Slack API token. You can find your API token by following these instructions:
# Go to the Slack API documentation page: https://api.slack.com/
# Click the "Start Building" button.
# If prompted, sign in to your Slack account.
# Click the "Create a new app" button.
# Give your app a name and select a development workspace.
# Click the "Create App" button.
