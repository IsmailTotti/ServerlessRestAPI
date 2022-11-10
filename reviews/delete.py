import os
from boto3.dynamodb.conditions import Key,Attr

import boto3
dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.scan(FilterExpression = Attr('color').eq('gray') and Attr('memory(GB)').eq('256'))
    print(result)
    for i in range(len(result)):
        print(result[i]['id'])
    # delete the todo from the database
        table.delete_item(
            Key={
                'id': event['pathParameters']['i']
         }
     )

    # create a response
    response = {
        "statusCode": 200
    }

    return response
