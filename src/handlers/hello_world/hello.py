import json
# this path is valid from the api instance
from src.handlers.hello_world.world import myString

def helloFunction(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello my name is HELLO, from Lambda whats up!' + myString() + event['hello'])
    }