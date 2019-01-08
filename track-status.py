import authentication
import time

def send_mms_message(toNumber, attachment, message):
    sdk = authentication.get_sdk()
    builder = sdk.create_multipart_builder()
    builder.set_body({
        'from': {'phoneNumber': authentication.get_phonenumber()},
        'to': [{'phoneNumber': toNumber}],
        'text': message
        })
    builder.add(attachment)
    try:
        request = builder.request('/account/~/extension/~/sms')
        platform = authentication.get_platform()
        response = platform.send_request(request)
        response = platform.get("/account/~/extension/~/message-store/" + str(response.json().id));
        if response.json().messageStatus == 'Delivered':
            print('Message was sent successfully')
        elif response.json().messageStatus == 'Queued':
            time.sleep(10)
            track_status(messageId)
        else:
            print (response.json().messageStatus)
    except Exception as e:
        print (e)

if __name__ == '__main__':
    image = open ('test.jpg', 'rb')
    attachment = ('test.jpg', image, 'image/jpeg')
    toNumber = 'recipient phone number'
    message = 'Test MMS message from Python'
    send_mms_message(toNumber, attachment, message)
