import boto3
import os

s3 = boto3.client('s3')
cwd = os.getcwd()

# download path
downloadDir = cwd + '/boto3/s3/static/downloads/'

# listing the files 
files = s3.list_objects(Bucket='boto3bucket070622-2')['Contents']

for file in files:
    s3.download_file(
        Bucket='boto3bucket070622-2',
        Key=file['Key'],
        Filename=downloadDir+'download_'+file['Key']
    )

