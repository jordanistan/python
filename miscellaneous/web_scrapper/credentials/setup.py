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
