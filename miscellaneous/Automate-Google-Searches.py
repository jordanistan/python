# Get the top google searches with this Killer automation script that uses the Request module to fetch the Google search page and the BS4 module that will extract the search results data.

# This handy script will allow you to fetch top searches and even crawl page by page too.

# Automate Google Searches
# pip install requests
import requests
from bs4 import BeautifulSoup
def GoogleSearch(query):
    url = "https://www.google.com/search?q=" + query
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    for item in soup.find_all("div", {"class": "g"}):
        link = item.find("h3").find("a")["href"]
        title = item.find("h3").find("a").text
        description = item.find("span", {"class": "aCOpRe"}).text
        print("Title: ", title)
        print("Description: ", description)
        print("Link: ", link)
GoogleSearch("python")