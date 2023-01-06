To write a Python script that stores API keys, a username, and a password, you can use a dictionary to hold the variables and then write the dictionary to a file. Here is an example of how you could do this:

```python
import json

# Create a dictionary with the variables
credentials = {
    "api_key": "your_api_key_here",
    "username": "your_username_here",
    "password": "your_password_here"
}

# Write the dictionary to a file
with open("credentials.json", "w") as f:
    json.dump(credentials, f)
```

This script creates a dictionary called credentials with the desired variables, and then uses the json module to write the dictionary to a file called credentials.json. The file will be stored in the same directory as the script.

To retrieve the variables from the file, you can use the following code:

```python
import json

# Read the dictionary from the file
with open("credentials.json", "r") as f:
    credentials = json.load(f)

# Access the variables
api_key = credentials["api_key"]
username = credentials["username"]
password = credentials["password"]

``` 


This code reads the credentials.json file and loads the dictionary into the credentials variable. You can then access the individual variables by using the keys of the dictionary.

Keep in mind that storing sensitive information like API keys, passwords, and other credentials in a file is not a secure way to store them. A better approach would be to use a secure storage solution such as a password manager or a secure configuration management system.