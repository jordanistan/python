import requests

url = 'https://www.iamjordanrobison.com'

for i in range(10):
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Request {i+1}: {response.content}')
    else:
        print(f'Error: Unable to retrieve analytics data for request {i+1}')

