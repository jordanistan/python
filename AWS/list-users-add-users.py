import boto3

# Set up the AWS client
client = boto3.client("iam")

# List all the users in the account
response = client.list_users()
users = response["Users"]

# Iterate over the users
for user in users:
  # Get the user's email address
  email = user["Email"]

  # Split the email address into its parts
  username, domain = email.split("@")

  # Construct the new email address with a different domain name
  new_email = f"{username}@companyb.com"

  # Update the user's email address
  client.update_user(UserName=user["UserName"], Email=new_email)

print("Done!")
