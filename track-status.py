from ringcentral import SDK
import os
import time
from dotenv import load_dotenv

load_dotenv(".env")

sdk = SDK( os.getenv("RINGCENTRAL_CLIENT_ID"),
           os.getenv("RINGCENTRAL_CLIENT_SECRET"),
           os.getenv("RINGCENTRAL_SERVER_URL") )

platform = sdk.platform()
platform.login( os.getenv("RINGCENTRAL_USERNAME"),
                os.getenv("RINGCENTRAL_EXTENSION"),
                os.getenv("RINGCENTRAL_PASSWORD") )

def check_status( messageId ):
    response = platform.get("/account/~/extension/~/message-store/" + str(messageId));
    return response.json().messageStatus

def send_sms_message( toNumber, message ):
    try:
        response = platform.post('/restapi/v1.0/account/~/extension/~/sms', {
            'from': {'phoneNumber': os.getenv("RINGCENTRAL_USERNAME")},
            'to': [{'phoneNumber': toNumber}],
            'text': message
        })
        messageId = response.json().id
        print("Message ID: " + str(messageId))
        status = check_status( response.json().id )
        if status == 'Delivered':
            print('Message was sent successfully')
        elif status == 'Queued':
            print("Message is queued. Will check again in 5 seconds...")
            time.sleep(5)
            print("New status is " + check_status(messageId))
        else:
            print( status )

    except Exception as e:
        print(e)

if __name__ == '__main__':
    toNumber = os.getenv("RINGCENTRAL_RECEIVER")
    message = 'This is a test message from Python'
    send_sms_message(toNumber, message)
