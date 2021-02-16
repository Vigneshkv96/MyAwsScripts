import boto3
import sys
from botocore.exceptions import ClientError

def createBucket(bucket_name,region = None):
    try:
        print(bucket_name)
        if region is None:
           s3_client = boto3.client("s3")
           s3_client.create_bucket(Bucket=bucket_name)
        else:
           s3_client = boto3.client("s3",region_name = region)
           location = { 'LocationConstraint':region}
           s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except ClientError as e:
        print ("ErrorCode:10")
        print ("ErrorName:ClientError")
        print ("ErrorMsg:{0}".format(str(e)))
def viewAllBuckets():
    try:
        s3_client = boto3.client("s3")
        print (dir(s3_client)) ### Get the attributes of s3_client i.e propeties,functions
        res = s3_client.list_buckets()
        print (res)
        for val in res['Buckets']:
            print (val)
    except ClientError as e:
        print ("ErrorCode:10")
        print ("ErrorName:ClientError")
        print ("ErrorMsg:{0}".format(str(e)))
viewAllBuckets()
