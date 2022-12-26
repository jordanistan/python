<!-- Here is a Python script that demonstrates how to search JIRA for tickets worked on in the last 24 hours and send the details to a Slack channel: -->

import os
import requests
from datetime import datetime, timedelta

# Set the JIRA URL and authentication credentials
jira_url = 'https://jira.example.com'
jira_username = 'user@example.com'
jira_password = 'password'

# Set the Slack webhook URL and channel
slack_webhook_url = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
slack_channel = '#general'

def search_jira(jql, jira_url, jira_username, jira_password):
    """
    Searches JIRA using the specified JQL query and returns the search results.
    """
    # Set the search URL and headers
    url = f'{jira_url}/rest/api/2/search'
    headers = {'Content-Type': 'application/json'}

    # Set the search payload
    payload = {'jql': jql, 'maxResults': 100}

    # Send the search request to JIRA
    response = requests.post(url, auth=(jira_username, jira_password), headers=headers, json=payload)

    # Return the search results
    return response.json()['issues']

def send_slack_message(text, slack_webhook_url, slack_channel):
    """
    Sends a message to the specified Slack channel using the specified webhook URL.
    """
    # Set the message payload
    payload = {'text': text, 'channel': slack_channel}

    # Send the message to Slack
    requests.post(slack_webhook_url, json=payload)

def main():
    # Set the JQL query to search for tickets worked on in the last 24 hours
    jql = 'worklogDate > start
