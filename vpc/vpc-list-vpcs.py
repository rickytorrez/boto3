import boto3

vpc = boto3.client('ec2')

# describe_vpcs gives information about all vpcs in the region
vpcs = vpc.describe_vpcs()["Vpcs"]

for vpc in vpcs:
    print(vpc['VpcId'])