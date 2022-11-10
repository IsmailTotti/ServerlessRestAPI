from encodings.utf_8 import encode
import json
import boto3
import os
import csv
import codecs
import sys

import urllib3

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

tableName = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def load(event, context):
   #get() does not store in memory
   try:
       #get the bucket name
       bucket = event['Records'][0]['s3']['bucket']['name']
       print(bucket)
       
       #get the file/key name
       #key = urllib3.parseurl(['Records'][0]['s3']['object']['key'], encode-'utf-8')
       key = 'testfile.csv'
       print(key)
       obj = s3.Object(bucket, key).get()['Body']
   except Exception as error:
       print(error)
       print("S3 Object could not be opened. Check environment variable. ")
   try:
       table = dynamodb.Table(tableName)
   except Exception as error:
       print(error)
       print("Error loading DynamoDB table. Check if table was created correctly and environment variable.")

   batch_size = 100
   batch = []

   #DictReader is a generator; not stored in memory
   for row in csv.DictReader(codecs.getreader('utf-8-sig')(obj)):
      if len(batch) >= batch_size:
         write_to_dynamo(batch)
         batch.clear()

      batch.append(row)

   if batch:
      write_to_dynamo(batch)

   return {
      'statusCode': 200,
      'body': json.dumps('Uploaded to DynamoDB Table')
   }


def write_to_dynamo(rows):
   try:
      table = dynamodb.Table(tableName)
   except Exception as error:
       print(error)
       print("Error loading DynamoDB table. Check if table was created correctly and environment variable.")

   try:
      with table.batch_writer() as batch:
         for i in range(len(rows)):
            batch.put_item(
               Item=rows[i]
            )
   except Exception as error:
       print(error)
       print("Error executing batch_writer")