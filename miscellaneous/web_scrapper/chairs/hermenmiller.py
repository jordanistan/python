import requests
from bs4 import BeautifulSoup
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_notification(chair_price):
  client = WebClient(token=os.environ['SLACK_API_TOKEN'])

  try:
      # Call the chat.postMessage method using the WebClient
      response = client.chat_postMessage(
          channel="#general",
          text=f"A Herman Miller Aeron chair is available for less than ${chair_price}!"
      )
      print(response)
  except SlackApiError as e:
      # You will get a SlackApiError if "ok" is False
      # (caused by an error returned by the Slack API)
      print("Error sending message: {}".format(e))

# Send an HTTP request to the webpage
response = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2047675.m570.l1311&_nkw=herman+miller+aeron&_sacat=0')

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the details and prices of the chairs
chairs = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
for chair in chairs:
  price = chair.find('span', {'class': 's-item__price'}).text
  price = int(price[1:]) # Extract the price from the string and convert it to an integer
  if price < 200:
    send_slack_notification(price)
