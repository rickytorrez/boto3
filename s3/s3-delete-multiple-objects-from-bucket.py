import boto3
import os
import glob

s3 = boto3.client('s3')

# get the objects stored in the bucket
objects = s3.list_objects(Bucket='boto3bucket070622-2')['Contents']

# iterate through the objects and delete them
for object in objects:
    response = s3.delete_object(
        Bucket='boto3bucket070622-2',
        Key=object['Key']
    )
    print(response)

