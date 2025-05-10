import boto3

s3=boto3.client('s3')
bucket_name="first-buck-25"
file_names=["sr_1.txt","sr_2.txt","sr_3.txt"]
s3_keys=["sr_1.txt","sr_2.txt","sr_3.txt"]
folder_name="customer-details/"

for file,key in zip(file_names, s3_keys):
    s3.upload_file(file, bucket_name, f"{folder_name}{key}")
    print(f"The file {file} Uploaded successfully!")