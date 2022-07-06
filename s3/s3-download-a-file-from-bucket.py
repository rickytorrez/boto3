import boto3

s3 = boto3.client('s3')

s3.download_file(
    Bucket='boto3bucket070622-2',
    Key='testFile.txt',
    Filename='download69.txt'
    )