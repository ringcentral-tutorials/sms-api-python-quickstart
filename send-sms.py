from ringcentral import SDK
import os
from dotenv import load_dotenv

load_dotenv(".env")

sdk = SDK( os.getenv("RINGCENTRAL_CLIENT_ID"),
           os.getenv("RINGCENTRAL_CLIENT_SECRET"),
           os.getenv("RINGCENTRAL_SERVER_URL") )

platform = sdk.platform()
platform.login( os.getenv("RINGCENTRAL_USERNAME"),
                os.getenv("RINGCENTRAL_EXTENSION"),
                os.getenv("RINGCENTRAL_PASSWORD") )

def send_sms_message( toNumber, message ):
    try:
        response = platform.post('/restapi/v1.0/account/~/extension/~/sms', {
            'from': {'phoneNumber': os.getenv("RINGCENTRAL_USERNAME")},
            'to': [{'phoneNumber': toNumber}],
            'text': message
        })
        print("Message ID: " + str(response.json().id))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    toNumber = os.getenv("RINGCENTRAL_RECEIVER")
    message = 'This is a test message from Python'
    send_sms_message(toNumber, message)
