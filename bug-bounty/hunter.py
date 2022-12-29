# This script uses the requests library to send HTTP GET and POST requests to a target URL. It allows you to set the HTTP headers, cookies, parameters, and payload as needed. It also prints the HTTP status code and response body for each request, which can be useful for identifying vulnerabilities and testing exploits.

# Please note that this script is for educational purposes only and should not be used to attack any website without permission. Bug bounty hunting is a legitimate activity, but it should always be done ethically and with the proper authorization.

# Here is a sample Python script that could be used to assist with bug bounty hunting:

import requests

# Set the target URL
url = 'https://example.com'

# Set the HTTP headers
headers = {
    'User-Agent': 'BugBountyHunter/1.0',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close'
}

# Set the HTTP cookies
cookies = {
    'PHPSESSID': '1234567890'
}

# Set the HTTP parameters
params = {
    'param1': 'value1',
    'param2': 'value2'
}

# Set the HTTP payload (for POST requests)
payload = {
    'username': 'test',
    'password': 'password'
}

# Send an HTTP GET request to the target URL
response = requests.get(url, headers=headers, cookies=cookies, params=params)

# Print the HTTP status code
print(response.status_code)

# Print the HTTP response body
print(response.text)

# Send an HTTP POST request to the target URL
response = requests.post(url, headers=headers, cookies=cookies, data=payload)

# Print the HTTP status code
print(response.status_code)

# Print the HTTP response body
print(response.text)
