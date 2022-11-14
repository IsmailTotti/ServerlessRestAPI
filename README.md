<!--
title: 'Laptop Listing Webservice'
description: 'This code demonstrates how to setup a RESTful Web Service allowing you to create, list, get, update and delete laptop listing according to given configuration. DynamoDB is used to store the data.'
platform: AWS
language: Python
framework: Serverless
-->
# Serverless REST API

This code demonstrates how to setup a [RESTful Web Services] allowing you to create, list, get, update and delete laptop listings. DynamoDB is used to store the data. 

## Structure
serverless.yml - yaml file to create the serverless infrastructure in AWS for all the operations 

testfile.csv - test data file with laptop configurations and price 

output folder - screenshots of the infrastructure created in AWS

This service has a separate directory for all the CRUD operations. For each operation exactly one file exists 

e.g. `reviews/delete.py`. 

In each of these files there is exactly one function(lambda) defined.

csv2db.py - reads the laptop listings from csv file stored in S3 and write to DynamoDB table

create.py - creates a dynamodb table with the given partition keys and columns. Writes to table when post request is made

get.py - get an item from the table

list.py - scan the table and gets a list of items from the table matching the given color and memory configuration

update.py - given the color, update the field in the table

delete.py - scan the table given the color or memory configuration and delete the entire row.

## Setup

npm install -g serverless

install python3.9

install aws cli

configure aws cli

## Deploy

In order to deploy the endpoint simply run

serverless deploy


Expected Result:
Deploying serverless-laptop-webservice to stage dev (us-west-2)

✔ Service deployed to stack serverless-laptop-webservice-dev (50s)

endpoints:                                                                                                                                                                    
  POST - https://5frx56psl1.execute-api.us-west-2.amazonaws.com/dev/reviews
  
  
 GET - https://5frx56psl1.execute-api.us-west-2.amazonaws.com/dev/reviews

functions:

create: serverless-laptop-webservice-dev-create (7.4 kB)

list: serverless-laptop-webservice-dev-list (7.4 kB)

get: serverless-laptop-webservice-dev-get (7.4 kB)

update: serverless-laptop-webservice-dev-update (7.4 kB)

delete: serverless-laptop-webservice-dev-delete (7.4 kB)

csv2db: serverless-laptop-webservice-dev-csv2db (7.4 kB)
