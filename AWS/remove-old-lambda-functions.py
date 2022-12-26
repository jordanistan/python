# Here is a Python 3 script that removes unwanted AWS Lambda functions that have not been used in a specified number of days:

import boto3
import datetime

# Set the number of days after which to delete unused functions
MAX_DAYS_UNUSED = 30

# Create an AWS client for the Lambda service
lambda_client = boto3.client('lambda')

# Get a list of all the functions in the account
response = lambda_client.list_functions()
functions = response['Functions']

# Iterate through the functions and delete any that have not been used in the specified number of days
for function in functions:
    # Get the function name and the last time it was invoked
    function_name = function['FunctionName']
    last_modified = function['LastModified']

    # Calculate the number of days since the function was last modified
    days_since_modified = (datetime.datetime.now() - last_modified).days

    # If the function has not been used in the specified number of days, delete it
    if days_since_modified > MAX_DAYS_UNUSED:
        print(f'Deleting function {function_name} because it has not been used in {MAX_DAYS_UNUSED} days')
        lambda_client.delete_function(FunctionName=function_name)
    else:
        print(f'Skipping function {function_name} because it has been used in the past {MAX_DAYS_UNUSED} days')


# This script uses the boto3 library to interact with the AWS Lambda service. 
# It first lists all the functions in the account using the list_functions method, and then iterates through the functions to delete any that have not been modified in the specified number of days.