import boto3

# used os.getcwd() to get working directory to grab the path for the testFile
import os

s3 = boto3.client('s3')

cwd = os.getcwd() 

s3.upload_file(
    Filename='./boto3/s3/static/testFile.txt',
    Bucket='boto3bucket070622-2',
    Key='uploadtest.txt')

