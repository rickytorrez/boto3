import boto3

vpc = boto3.client('ec2')

res = vpc.delete_security_group(
    GroupId='sg-04bc984cdfb3f102d'
)

print(res)  