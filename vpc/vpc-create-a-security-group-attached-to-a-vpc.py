import boto3

vpc = boto3.client('ec2')

# VpcId is the argument to provide for a specific attachment to a VPC
res = vpc.create_security_group(
    Description='Security Group on Specific VPC Demo',
    GroupName='Tutorial_boto3',
    VpcId='vpc-0fb98ab93c2cf4934',
)

print(res)