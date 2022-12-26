# There are many free text message services available on the internet like Twillo, fast2sms, etc.

# Fast2sms provide 50 free messages with a prebuild template to connect your script with their API. This script will let us send text SMS to any number directly through our command-line interface.

import requests
import json
def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'FIND_YOUR_OWN',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    #print(dic)
    return dic.get('return')


num = int(input("Enter The Number:\n"))
msg = input("Enter The Message You Want To Send:\n")
s = send_sms(num, msg)
if s:
    print("Successfully sent")
else:
    print("Something went wrong..")