import boto3

s3_client=boto3.client('s3')
bucket_name="first-buck-25"
folder_prefix="customer-details/"
response=s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix)
if "Contents" in response:
    for obj in response["Contents"]:
        if obj["Key"].startswith(folder_prefix+"sr_1"):
            print(obj["Key"])
            s3_client.copy_object(Bucket=bucket_name, CopySource={"Bucket": bucket_name, "Key":obj["Key"]}, Key="sr1/"+obj["Key"].split("/")[-1])
            s3_client.delete_object(Bucket=bucket_name, Key=obj["Key"])
            print("""File moved successfully to "sr1" folder and deleted from "customer_details" folder!""")

            sns=boto3.client('sns')
            topic_arn="arn:aws:sns:us-west-2:648063383234:MySNSTopic"
            response=sns.publish(TopicArn=topic_arn,Message="File moved from sr1 to customer_details folder",Subject="S3 action notification")
            print("Message sent!")