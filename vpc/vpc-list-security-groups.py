import boto3

vpc = boto3.client('ec2')

security_groups = vpc.describe_security_groups()['SecurityGroups']

for group in security_groups:
    print(group['GroupId'])