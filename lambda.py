import boto3

def lambda_handler(event, context):
    ses = boto3.client('ses', region_name='us-east-1')
    subject = 'Thirsty Plant'
    message = 'Hey, it\'s time to water me again! I do not like how dry it is.\nGive me water Give me water Give me water Give me water Give me water'
    recipient = 'TO EMAIL GOES HERE'
    
    
    response = ses.send_email(
        Source = 'FROM EMAIL GOES HERE',
        Destination = {
            'ToAddresses': [recipient]
        },
        Message = {
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': message
                }
            }
        }
        )
