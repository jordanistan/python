<!-- Here is a Python script that demonstrates how to extend the AWS Identity and Access Management (IAM) service with custom resources and actions, and use it to manage permissions for users:

This script defines a custom resource called S3BucketPermissions, which can be used to manage permissions for a specific S3 bucket. It also defines a custom action called GrantPermission, which can be used to grant permissions to a specific user. The script then uses these custom resources and actions to grant permissions to the user user1 to access all S3 resources.

To use this script, you will need to have the boto3 library installed and have your AWS credentials configured on your system. You will also need to have a custom resource Lambda function set up, as indicated by the ServiceToken property in the resource and action definitions. This function will handle the actual creation and modification of resources and permissions. -->

import boto3

# Connect to the IAM service
iam = boto3.client('iam')

# Define a custom resource for managing permissions for a specific S3 bucket
resource = {
  "Type": "Custom::S3BucketPermissions",
  "Properties": {
    "ServiceToken": {"Fn::GetAtt": ["CustomResourceLambdaFunction", "Arn"]},
    "BucketName": "my-bucket",
    "Permissions": {
      "Action": "s3:*",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  }
}

# Define a custom action for granting permissions to a specific user
action = {
  "Type": "Custom::GrantPermission",
  "Properties": {
    "ServiceToken": {"Fn::GetAtt": ["CustomResourceLambdaFunction", "Arn"]},
    "UserName": "user1",
    "PolicyDocument": {
      "Statement": [{
        "Action": "s3:*",
        "Effect": "Allow",
        "Resource": "*"
      }]
    }
  }
}

# Use the custom resource and action to grant permissions to the user
response = iam.create_policy(
  PolicyName='S3BucketPermissions',
  PolicyDocument=resource['Properties']['Permissions'],
  Description='Grants permissions to access the specified S3 bucket'
)

policy_arn = response['Policy']['Arn']

iam.attach_user_policy(
  UserName=action['Properties']['UserName'],
  PolicyArn=policy_arn
)

print('Done')
