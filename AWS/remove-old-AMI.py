<!-- Here is a Python script that demonstrates how to remove Amazon Machine Images (AMIs) that are older than 180 days:
This script uses the boto3 library to connect to the EC2 service and retrieve a list of all AMIs owned by the current user. It then iterates over the AMIs and calculates the age of each one in days. If the age is greater than 180 days, it deletes the AMI using the deregister_image function.

To use this script, you will need to have the boto3 library installed, and you will need to have your AWS credentials configured on your system. You can then run the script using the following command:

python remove_old_amis.py -->

import boto3
import datetime

# Connect to the EC2 service
ec2 = boto3.client('ec2')

# Get a list of all AMIs
response = ec2.describe_images(Owners=['self'])
images = response['Images']

# Iterate over the AMIs and delete those that are older than 180 days
for image in images:
	creation_date = image['CreationDate']
	age = datetime.datetime.now(datetime.timezone.utc) - creation_date
	if age.days > 180:
		image_id = image['ImageId']
		print(f'Deleting AMI {image_id}')
		ec2.deregister_image(ImageId=image_id)

print('Done')
