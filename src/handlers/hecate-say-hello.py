import json

def hecateFunction(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello my name is Hecate, from Lambda!')
    }
