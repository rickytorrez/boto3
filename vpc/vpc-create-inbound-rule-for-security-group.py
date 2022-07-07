import boto3

vpc = boto3.client('ec2')

res = vpc.authorize_security_group_ingress(
    GroupId='sg-04bc984cdfb3f102d',
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'boto3_tutorial'
                },
            ],
            'ToPort': 22,
        },
    ],
)

print(res)