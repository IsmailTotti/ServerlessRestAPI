import json
import os
from boto3.dynamodb.conditions import Key,Attr

from reviews import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all reviews from the database
    result = table.scan(FilterExpression = Attr('color').eq('gray') and Attr('memory(GB)').eq('256'))
    print(result)
    # create a response
    response = {
        "statusCode": 200,
        'headers': {
           'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
            
            
        },
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
