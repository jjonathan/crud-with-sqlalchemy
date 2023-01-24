import json
import ast

def lambda_handler(event, context):
    # TODO implement
    causa = json.loads(event['Cause'])
    errorMessage = ast.literal_eval(causa['errorMessage'])
    return {
        'statusCode': 200,
        'message': errorMessage[0],
        'objeto': errorMessage[1]
    }
