import boto3
import os
import glob

# gets path
cwd = os.getcwd()

# files uses glob to get the current working dir and adding the location of the static folder and the wild card for all the test files to upload
files = glob.glob(cwd + '/boto3/s3/static/*.txt')

for file in files:
    s3 = boto3.client('s3')
    s3.upload_file(
        Filename=file,
        Bucket='boto3bucket070622-2',
        Key=file.split('/')[-1])