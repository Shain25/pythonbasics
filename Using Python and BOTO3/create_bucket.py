import boto3

s3=boto3.client('s3')
bucket_names=["first-buck-25","second-buck-25"]
region="us-west-2"

for bucket_name in bucket_names:
    s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': region})
    print(f"Bucket {bucket_name} created successfully!")