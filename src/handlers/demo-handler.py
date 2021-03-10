import json

def demoFunction(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('hey we are doing a demo')
    }
