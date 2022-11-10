import json
import logging
import os
import time
import uuid
import random

import boto3
dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])
    if ('color' not in data) and ('memory' not in data):
        logging.error("Validation Failed")
        raise Exception("Couldn't create the item")
    
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'model':data['model'],
        'review': data['review'],
        'color':data['color'],
        'memory(GB)':data['memory(GB)'],
        'price':data['price'],
        'os':data['os'],
        'cpu':data['cpu']
    }

    # write the review to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        'headers': {
           'Access-Control-Allow-Origin': '*',
           'Access-Control-Allow-Credentials': True
            
            
        },
        "body": json.dumps(item)
    }

    return response
