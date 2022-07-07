import boto3

vpc = boto3.client('ec2')

res = vpc.delete_vpc(
    VpcId='vpc-0fb98ab93c2cf4934'
)

print(res)