import boto3
import sys
import datetime
iam = boto3.client('iam')

def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60

for user in iam.list_users()['Users']:
 #print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(user['UserName'],user['UserId'],user['Arn'],user['CreateDate']))
 ct = user['CreateDate'].replace(tzinfo=None)
 dt = datetime.datetime.now()
 diff = dt-ct
 diff = days_hours_minutes(diff)
 retention = int(sys.argv[1]) - int(diff[0])
 print("User: {0}\nCreatedOn: {1}\nRetention: {2}\n".format(user['UserName'],user['CreateDate'],retention))
 #print(dt)
 
