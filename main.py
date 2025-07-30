--Concept Code--

import boto3

# Create AWS clients
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

# 1. Check running EC2 instances
instances = ec2.describe_instance_status(IncludeAllInstances=True)
for i in instances['InstanceStatuses']:
    print(f"Instance {i['InstanceId']} is {i['InstanceState']['Name']}")

# 2. Get CloudWatch metrics for MediaLive channel
metric = cloudwatch.get_metric_statistics(
    Namespace='AWS/MediaLive',
    MetricName='ActiveOutputFailover',
    Dimensions=[{'Name': 'ChannelId', 'Value': 'your-channel-id'}],
    StartTime='2025-07-29T00:00:00Z',
    EndTime='2025-07-30T00:00:00Z',
    Period=300,
    Statistics=['Sum']
)

print("MediaLive Failover Events:", metric['Datapoints'])

