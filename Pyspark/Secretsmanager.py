
import boto3
import pprint

def get_secrets()
            client = boto3.client('secretsmanager')
    
            response = client.get_secret_value(SecretID='snowflake/capstone/login')
        return response
    
pp = pprint.PrettyPrinter(indent=4) 
pp.pprint(get_secrets())
#pprint is just to print it out in a nice structured file format