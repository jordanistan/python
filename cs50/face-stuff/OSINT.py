import requests
import argparse
import re

def get_details(name):
    # Google search API endpoint
    endpoint = "https://www.google.com/search?q="

    # Build the search query
    query = name + " site:linkedin.com"
    query = query.replace(" ", "+")

    # Get the search results
    response = requests.get(endpoint + query)
    results = response.text

    # Extract relevant information (in this case, just LinkedIn profiles)
    linkedin_profiles = re.findall('(?<=href=")[^"]*linkedin.com[^"]*', results)

    # Print the extracted information
    print(f"LinkedIn profiles for {name}:")
    for profile in linkedin_profiles:
        print(profile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Name of the person to search for")
    args = parser.parse_args()
    get_details(args.name)
