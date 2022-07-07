import boto3

vpc = boto3.client('ec2')

res = vpc.update_security_group_rule_descriptions_ingress(
    GroupId='sg-04bc984cdfb3f102d',
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'Updating the description'
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(res)