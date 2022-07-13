import boto3

ec2 = boto3.resource('ec2')

res = ec2.create_instances(
    ImageId='ami-02d1e544b84bf7502', #AMI Id
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
)  

print(res)