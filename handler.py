import datetime
import boto3

def hello(event, context):
  dt_now = datetime.datetime.now()
  print('the object created at ' + str(dt_now) + '.') # 時刻を出力

  s3 = boto3.client('s3')

  response = s3.list_objects_v2(Bucket="photos20220120") # serverless.ymlで定義しているバケット名

  for object in response['Contents']:
      print(object['Key']) #S3バケットにあるオブジェクト名を出力する
