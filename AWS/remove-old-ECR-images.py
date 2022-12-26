# Here is a Python script that removes old AWS Elastic Container Registry (ECR) images, but does not remove anything with "prod" in the name:

import boto3
import datetime

# Set the number of days after which to delete old images
MAX_DAYS_OLD = 30

# Create an AWS client for the ECR service
ecr_client = boto3.client('ecr')

# Set the repository name
repository_name = 'my-repository'

# List the images in the repository
response = ecr_client.list_images(repositoryName=repository_name)
images = response['imageIds']

# Iterate through the images and delete any that are older than the specified number of days
for image in images:
    # Get the image digest and creation date
    image_digest = image['imageDigest']
    image_created_at = image['imagePushedAt']

    # Calculate the number of days since the image was created
    days_since_created = (datetime.datetime.now() - image_created_at).days

    # Check if the image digest includes "prod"
    if "prod" in image_digest:
        print(f'Skipping image {image_digest} because it includes "prod" in the name')
        continue

    # If the image is older than the specified number of days, delete it
    if days_since_created > MAX_DAYS_OLD:
        print(f'Deleting image {image_digest} because it is {days_since_created} days old')
        ecr_client.batch_delete_image(
            repositoryName=repository_name,
            imageIds=[
                {
                    'imageDigest': image_digest
                },
            ]
        )
    else:
        print(f'Skipping image {image_digest} because it is only {days_since_created} days old')

# This script uses the boto3 library to interact with the AWS ECR service. It lists the images in the specified repository using the list_images method, and then iterates through the images to delete any that are older than the specified number of days. It also checks the image digest for the string "prod" and skips any images that contain it.

