import csv
import requests
from bs4 import BeautifulSoup

# Set the URL to Indeed's job search page
url = 'https://www.indeed.com/jobs?q=aws+cloud+engineer&l=Remote'

# Send a GET request to the URL and get the HTML response
response = requests.get(url)

# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize an empty list to store the job data
jobs = []

# Extract the job data from the page
job_cards = soup.select('.jobsearch-SerpJobCard')
for card in job_cards:
    title_element = card.find('h2', class_='title')
    company_element = card.find('span', class_='company')
    location_element = card.find('span', class_='location')

    title = title_element.text.strip()
    company = company_element.text.strip()
    location = location_element.text.strip()

    job = {
        'title': title,
        'company': company,
        'location': location
    }
    jobs.append(job)

# Write the job data to a CSV file
with open('aws+cloud+engineer.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'company', 'location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for job in jobs:
        writer.writerow(job)


# This script first sends a GET request to the specified URL and gets the HTML response. It then uses the BeautifulSoup library to parse the HTML and extract the job data from the page. It stores the job data in a list of dictionaries, and then writes the data to a CSV file using the Python csv module.

# To upload the results to a GitHub repository, you will need to create a repository on GitHub and then push the jobs.csv file to the repository using Git. Here is a brief overview of the steps you will need to follow:

# 1. Create a new repository on GitHub and make a note of the repository's URL.
# 2. Initialize a local Git repository in the same directory as the jobs.csv file by running the following command: git init
# 3. Add the jobs.csv file to the staging area by running the following command: git add jobs.csv
# 4. Commit the changes to the local repository by running the following command: git commit -m "Initial commit"
# 5. Add the remote repository as an upstream repository by running the following command: git remote add origin <repository-url> (replace <repository-url> with the URL of the repository you created on GitHub)
# 6. Push the changes to the remote repository by running the following command: git push -u origin main