import sys
import os
import boto3
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
