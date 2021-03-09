import json
import numpy

def hecateFunction(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello my name is Hecate, from Lambda whats up!' + str(numpy.array((1,2,3))))
    }
