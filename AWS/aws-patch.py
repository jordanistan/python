# To write a Python script using the AWS Systems Manager to patch all instances that are not in a production environment, you can use the following steps:
# This will create a patch baseline that specifies the patches to be installed on the instances, associate the patch baseline with the instances that are not in a production environment, create a maintenance window to perform the patching, and create a task that will run during the maintenance window and patch the instances. The patching will be performed automatically according to the schedule specified in the maintenance window.

# Keep in mind that this is just a basic example, and you may need to customize the script to suit your specific requirements. For example, you may

Install the boto3 library and set up your AWS credentials.
Use the boto3 client to describe the instances in your AWS account:
Copy code
import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()
Filter the list of instances to include only those that are not in a production environment:
Copy code
non_prod_instances = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for tag in instance['Tags']:
            if tag['Key'] == 'environment' and tag['Value'] != 'prod':
                non_prod_instances.append(instance['InstanceId'])
Use the boto3 client to create a patch baseline that specifies the patches to be installed on the instances:
Copy code
ssm = boto3.client('ssm')

response = ssm.create_patch_baseline(
    Name='non-prod-patch-baseline',
    PatchGroup='critical'
)

baseline_id = response['BaselineId']
Use the boto3 client to associate the patch baseline with the instances that are not in a production environment:
Copy code
response = ssm.register_patch_baseline_for_patch_group(
    PatchGroup='non-prod',
    BaselineId=baseline_id
)
Use the boto3 client to create a maintenance window that will be used to perform the patching:
Copy code
response = ssm.create_maintenance_window(
    Name='patching-window',
    Schedule='cron(0 16 ? * MON-FRI *)',
    Duration=120,
    Cutoff=60
)

window_id = response['WindowId']
Use the boto3 client to create a task that will run during the maintenance window and patch the instances:
Copy code
response = ssm.create_maintenance_window_task(
    WindowId=window_id,
    Targets=[
        {
            'Key': 'instanceids',
            'Values': non_prod_instances
        },
    ],
    TaskArn='AWS-RunPatchBaseline',
    ServiceRoleArn='service-role-arn',
    TaskParameters={
        'BaselineId': [baseline_id],
        'Operation': ['ScanAndInstall'],
        'ScanType': ['Auto']
    }
)
