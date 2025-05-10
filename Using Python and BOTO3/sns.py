import boto3

sns=boto3.client('sns')

response=sns.create_topic(Name="MySNSTopic")
topic_arn=response['TopicArn']
print(f"Topic created: {topic_arn}")

subscription=sns.subscribe(TopicArn=topic_arn,Protocol='email',Endpoint='shaineeman@outlook.com')

print("Email subscription created successfully!")