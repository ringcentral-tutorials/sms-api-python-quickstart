import authentication

def sendMMSMessage(toNumber, attachment, message):
    platform = authentication.get_platform()
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
        response = platform.send_request(request)
        print (response.json().uri)
        print (response.json().id)
    except Exception as e:
        print (e)

if __name__ == '__main__':
    image = open ('test.jpg', 'rb')
    attachment = (
        'test.jpg',
        image,
        'image/jpeg'
        )
    sendMMSMessage('16505130930', attachment, 'Test MMS message from Python')
