import boto3

vpc = boto3.client('ec2')

security_group = vpc.describe_security_groups(
    Filters = [{
        'Name': 'group-name',
        'Values': [
            'aws-cloud9-Cloud9-3bb0152104734e60ae6e68c4590b8dce-InstanceSecurityGroup-8SZRFQ0LSQR0',
            'default'
            ]
        }
    ]
)

print(security_group['SecurityGroups'])


