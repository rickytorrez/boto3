import boto3

vpc = boto3.client('ec2')

security_groups = vpc.describe_security_groups(GroupIds=['sg-0bf5e195c819c45b6'])

print(security_groups)
