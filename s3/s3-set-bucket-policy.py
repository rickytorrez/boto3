import boto3
import json

s3 = boto3.client('s3')

# policy generated with aws policy generator tool
bucket_policy = {
  "Id": "Policy1657120412635",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1657120404637",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::boto3bucket070622-2/*",
      "Principal": "*"
    }
  ]
}

# convert policy to JSON
b_policy = json.dumps(bucket_policy)

# attach policy to bucket
policy = s3.put_bucket_policy(Bucket='boto3bucket070622-2', Policy=b_policy)







