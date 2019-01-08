import authentication

def send_sms_message(toNumber, message):
    params = {
        'from': {'phoneNumber': authentication.get_phonenumber()},
        'to': [{'phoneNumber': toNumber}],
        'text': message
        }
    try:
        platform = authentication.get_platform()
        response = platform.post('/restapi/v1.0/account/~/extension/~/sms', params)
        print(response.json().id)
    except Exception as e:
        print (e)

if __name__ == '__main__':
    toNumber = 'recipient phone number'
    message = 'This is a test message from Python'
    send_sms_message(toNumber, message)
