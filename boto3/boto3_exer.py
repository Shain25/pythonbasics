#Exercise 1:
import boto3

s3=boto3.client('s3')
bucket_name="student-shai-bucket"
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

print(f"The bucket {bucket_name} created successfully!")

file_name="team_image.png"
s3.upload_file(file_name, bucket_name, file_name)
print(f"The File {file_name} uploaded successfully!")

response=s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("The bucket is empty!")

#Exercise 2 and 3:
import boto3
import os

s3=boto3.client('s3')
bucket_name="student-shai-bucket"

buckets= [bucket["Name"] for bucket in s3.list_buckets()["Buckets"]]
if bucket_name not in buckets:
    s3.create_bucket(Bucket=bucket_name)
    print(f"The bucket {bucket_name} created successfully")
else:
    print(f"The bucket {bucket_name} already exists!")

daily_documents_path="/home/ec2-user/daily_documents"
existing_files = [obj["Key"] for obj in s3.list_objects_v2(Bucket=bucket_name).get("Contents", [])]
print("Starting upload of daily documents")

for file_name in os.listdir(daily_documents_path):
    file_path=os.path.join(daily_documents_path, file_name)
    if file_name not in existing_files:
        if os.path.isfile(file_path):
            s3.upload_file(file_path, bucket_name, file_name)
            print(f"The File {file_name} uploaded successfully!")
        else:
            print(f"{file_path} is a folder!")
    else:
        print(f"The file {file_name} already exists!")