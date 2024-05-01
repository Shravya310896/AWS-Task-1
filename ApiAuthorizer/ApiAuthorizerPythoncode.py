import json
import base64

def lambda_handler(event, context):
  # Get the token from the event
  token = event['authorizationToken']

  # Decode the token
  decoded_token = base64.b64decode(token)

  # Verify the token
  # ...

  # If the token is valid, return an IAM policy that allows access to the API
  policy = {
    'principalId': decoded_token['sub'],
    'policyDocument': {
      'Version': '2012-10-17',
      'Statement': [
        {
          'Action': 'execute-api:Invoke',
          'Effect': 'Allow',
          'Resource': event['methodArn']
        }
      ]
    }
  }

  # Otherwise, return an IAM policy that denies access to the API
  policy = {
    'principalId': 'user',
    'policyDocument': {
      'Version': '2012-10-17',
      'Statement': [
        {
          'Action': 'execute-api:Invoke',
          'Effect': 'Deny',
          'Resource': event['methodArn']
        }
      ]
    }
  }

  return policy