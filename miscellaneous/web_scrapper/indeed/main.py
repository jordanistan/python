import csv
from bs4 import BeautifulSoup
import requests

# Send a GET request to the URL
url = 'https://www.indeed.com/q-Aws-Cloud-Engineer-$155,000-l-Remote-jobs.html?vjk=284ba14f021e6bd6'
page = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(page.content, 'html.parser')

# Find all the job listings on the page
jobs = soup.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result')

# Open a CSV file for writing
with open('jobs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Job Title', 'Company', 'Link'])

    # Iterate over the job listings and extract the information you need
    for job in jobs:
        title_elem = job.find('h2', class_='title')
        company_elem = job.find('span', class_='company')
        if title_elem and company_elem:
            title = title_elem.text.strip()
            company = company_elem.text.strip()

            # Find the link to the company's website
            link_elem = company_elem.find('a')
            if link_elem:
                link = link_elem.get('href')
            else:
                link = ''

            # Write the data to the CSV file
            writer.writerow([title, company, link])
