import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('boto3bucket070622-2')

response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
)

print(response)