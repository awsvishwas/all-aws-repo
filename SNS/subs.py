import boto3

sns_client = boto3.client('sns',region_name='us-east-1')
topic_arn = 'arn:aws:sns:us-east-1:124058707612:vishwas-sns-test'

with open('sns.txt') as f:
    for line in f:
        phone_number = line.strip()
        response = sns_client.subscribe(
            TopicArn=topic_arn,
            Protocol='sms',
            Endpoint=phone_number
        )
        print(response)
