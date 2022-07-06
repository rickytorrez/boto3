import boto3

s3 = boto3.client('s3')

# gets S3 bucket policy
bucketPolicy = s3.get_bucket_policy(Bucket='boto3bucket070622-2')['Policy']

print(bucketPolicy)