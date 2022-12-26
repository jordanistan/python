# To write a script using AWS Systems Manager to patch all instances that are not in a production environment, you can use the following steps:

# Install and configure the AWS CLI on your local machine.
# Use the describe-instances command to list all the instances in your AWS account:

aws ec2 describe-instances
# Filter the list of instances to include only those that are not in a production environment. You can use the jq command-line tool to do this:

aws ec2 describe-instances | jq '.Reservations[].Instances[] | select(.Tags[].Key=="environment" and .Tags[].Value!="prod")'
# Use the create-patch-baseline command to create a patch baseline that specifies the patches to be installed on the instances:

aws ssm create-patch-baseline --name "non-prod-patch-baseline" --patch-group "critical"
# Use the register-patch-baseline-for-patch-group command to associate the patch baseline with the instances that are not in a production environment:

aws ssm register-patch-baseline-for-patch-group --patch-group "non-prod" --baseline-id "baseline-id"
# Use the create-maintenance-window command to create a maintenance window that will be used to perform the patching:

aws ssm create-maintenance-window --name "patching-window" --schedule "cron(0 16 ? * MON-FRI *)" --duration 120 --cutoff 60
# Use the create-maintenance-window-task command to create a task that will run during the maintenance window and patch the instances:

aws ssm create-maintenance-window-task --window-id "window-id" --targets "Key=instanceids,Values=instance-id-1,instance-id-2,..." --task-arn "AWS-RunPatchBaseline" --service-role-arn "service-role-arn" --task-parameters '{"BaselineId":["baseline-id"],"Operation":["ScanAndInstall"],"ScanType":["Auto"]}'
# This will create a patch baseline that specifies the patches to be installed on the instances, associate the patch baseline with the instances that are not in a production environment, 
# create a maintenance window to perform the patching, and create a task that will run during the maintenance window and patch the instances. 
# The patching will be performed automatically according to the schedule specified in the maintenance window.

# Keep in mind that this is just a basic example, and you may need to customize the script to suit your specific requirements.
# For example, you may want to specify different patch groups or parameters for the patching operation, 
# or add additional tasks to manage other aspects of the maintenance window.