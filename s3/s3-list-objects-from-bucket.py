import boto3

s3 = boto3.client('s3')

objects = s3.list_objects(Bucket='boto3bucket070622-2')['Contents']

if len(objects) > 0:
    for object in objects:
        print(object['Key'])
else:
    print('No objects stored in this bucket')
