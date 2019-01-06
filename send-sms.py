import authentication

def sendSMSMessage(toNumber, message):
    platform = authentication.get_platform()
    params = {
        'from': {'phoneNumber': authentication.get_phonenumber()},
        'to': [{'phoneNumber': toNumber}],
        'text': message
        }
    try:
        response = platform.post('/restapi/v1.0/account/~/extension/~/sms', params)
        print(response.json().uri)
        print(response.json().id)
    except Exception as e:
        print (e)

if __name__ == '__main__':
    toNumber = '16505130930'
    message = 'This is a test message from Python'
    sendSMSMessage(toNumber, message)
