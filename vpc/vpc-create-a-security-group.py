import boto3

vpc = boto3.client('ec2')

# assigned to default VPC if not arg is not provided
res = vpc.create_security_group(
    Description='Demo for tutorial 14',
    GroupName='Tutorial14_boto3',
)

print(res)