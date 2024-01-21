import time 
import urllib.request, urllib.parse, urllib.error 
import json 
import os.path 
import boto3 
print('Function start (CloudWatch)') 
s3 = boto3.client('s3') 
def lambda_handler(event, context): 
    source_bucket = event['Records'][0]['s3']['bucket']['name'] 
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key']) 
    copy_source = {'Bucket':source_bucket, 'Key':key} 
    print("Log stream name:", context.log_stream_name) 
    print("Log group name:", context.log_group_name) 
    print("Request ID:",context.aws_request_id) 
    print('Start of Try') 
    try: 
        waiter = s3.get_waiter('object_exists') 
        waiter.wait(Bucket=source_bucket, Key=key) 
        extension = os.path.splitext(key)[1] 
        if extension==".png": 
            s3.copy_object(Bucket="pngs3bucketvishwas", Key=key, CopySource=copy_source) 
        if extension==".pdf": 
            s3.copy_object(Bucket="pdfs3bucketvishwas", Key=key, CopySource=copy_source)
        if extension==".txt": 
            s3.copy_object(Bucket="txts3bucketvishwas", Key=key, CopySource=copy_source) 
    except Exception as e: 
        print(e) 
        print('Error while trying to copy the file. Does not exist'.format(key, source_bucket)) 
        raise e 
    print('End of function')
