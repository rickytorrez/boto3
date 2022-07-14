# allows us to access environment variables
import os
# AWS SDK for python
import boto3

# Global variables
# Amazon Machine Image that we use to provision our EC2 instance
AMI = os.environ['AMI']
# Instance Type = t2.micro
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
# Key Pair name 
KEY_NAME = os.environ['KEY_NAME']
# Public Subnet created by CF template
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

# print("New instance created:", instance[0].id)

# Environment Variables on the Configuration Tab

# AMI = ami-02d1e544b84bf7502
# INSTANCE_TYPE = t2.micro
# KEY_NAME = boto_training
# SUBNET_ID = subnet-0174570ef0b29e65f