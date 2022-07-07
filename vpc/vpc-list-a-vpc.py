import boto3

vpc = boto3.client('ec2')

# describe_vpcs takes a list argument with a single VPC to query
vpc = vpc.describe_vpcs(VpcIds=['vpc-029152843846f5b78'])

print(vpc)