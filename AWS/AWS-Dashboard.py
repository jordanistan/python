# Here is a Python script that creates a dashboard of all the AWS resources being used in the past 24 hours and compares the results with the previous 72 hours:

import boto3
import datetime

# Set the time range for the dashboard data
now = datetime.datetime.now()
time_range_end = now.strftime('%Y-%m-%dT%H:%M:%SZ')
time_range_start = (now - datetime.timedelta(hours=24)).strftime('%Y-%m-%dT%H:%M:%SZ')
time_range_start_previous = (now - datetime.timedelta(hours=72)).strftime('%Y-%m-%dT%H:%M:%SZ')

# Create an AWS client for the CloudWatch service
cloudwatch_client = boto3.client('cloudwatch')

# Set the dashboard name and dimensions
dashboard_name = 'AWS Resources Dashboard'
dimensions = [{'Name': 'ServiceName', 'Value': '*'}]

# Get the dashboard data for the past 24 hours
response = cloudwatch_client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/Usage',
                    'MetricName': 'UsageQuantity',
                    'Dimensions': dimensions
                },
                'Period': 3600,
                'Stat': 'Sum',
                'Unit': 'Count'
            },
            'Label': 'AWS Resource Usage (Last 24 Hours)',
            'ReturnData': True
        },
    ],
    StartTime=time_range_start,
    EndTime=time_range_end
)

# Print the dashboard data for the past 24 hours
print(f'Dashboard data for the past 24 hours ({time_range_start} - {time_range_end}):')
for metric_data_result in response['MetricDataResults']:
    print(f'{metric_data_result["Label"]}:')
    for value in metric_data_result['Values']:
        print(f'  {value}')

# Get the dashboard data for the previous 72 hours
response = cloudwatch_client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/Usage',
                    'MetricName': 'UsageQuantity',
                    'Dimensions': dimensions
                },
                'Period': 3600,
                'Stat': 'Sum',
                'Unit': 'Count'
            },
            'Label': 'AWS Resource Usage (Previous 72 Hours)',
            'ReturnData': True
        },
    ],
    StartTime=time_range_start_previous,
    EndTime=time_range_end
)

# Print the dashboard data for the previous 72 hours
print(

