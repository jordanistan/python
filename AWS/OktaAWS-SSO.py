# This script first obtains an access token from Okta using the client ID and client secret. It then uses the access token to make a request to the Okta API to get the AWS SSO URL. Finally, it prints the AWS SSO URL, which you can use to redirect the user to the AWS SSO login page.
import requests
import json

# Replace these values with your Okta credentials and AWS SSO application details
client_id = "your_client_id"
client_secret = "your_client_secret"
base_url = "https://your_okta_domain.com"
aws_sso_app_url = "https://aws.amazon.com/console"

# Obtain an access token from Okta
auth_response = requests.post(
    f"{base_url}/oauth2/default/v1/token",
    auth=(client_id, client_secret),
    headers={
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    },
    data={
        "grant_type": "client_credentials",
        "scope": "access_as_user",
    },
)

access_token = auth_response.json()["access_token"]

# Use the access token to get the AWS SSO URL from Okta
sso_response = requests.get(
    f"{base_url}/api/v1/apps/{aws_sso_app_url}/sso/saml",
    headers={
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
    },
)

sso_url = sso_response.json()["ssoUrl"]

# Use the AWS SSO URL to redirect the user to the AWS SSO login page
print(f"Redirecting to: {sso_url}")
