import boto3

vpc = boto3.client('ec2')

# provide specific values for GroupId, Ports, Protocols, CIDRUP and Description
res = vpc.revoke_security_group_egress(
    GroupId='sg-04bc984cdfb3f102d',
    IpPermissions=[
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'New description for outbound rule'
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(res)