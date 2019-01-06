from multiprocessing import Process
from time import sleep
from ringcentral.subscription import Events
from ringcentral import SDK

import os
from dotenv import Dotenv
dotenv = Dotenv(".env")
os.environ.update(dotenv)


def main():
    fromNumber = ""
    if os.getenv("ENVIRONMENT_MODE") == "sandbox":
        sdk = SDK(os.getenv("CLIENT_ID_SB"), os.getenv("CLIENT_SECRET_SB"), 'https://platform.devtest.ringcentral.com')
        platform = sdk.platform()
        fromNumber = os.getenv("USERNAME_SB")
        platform.login(os.getenv("USERNAME_SB"), '', os.getenv("PASSWORD_SB"))
    else:
        sdk = SDK(os.getenv("CLIENT_ID_PROD"), os.getenv("CLIENT_SECRET_PROD"), 'https://platform.ringcentral.com')
        platform = sdk.platform()
        fromNumber = os.getenv("USERNAME_PROD")
        platform.login(os.getenv("USERNAME_PROD"), '', os.getenv("PASSWORD_PROD"))

    def on_message(msg):
        sender = msg['body']['from']['phoneNumber']
        response = platform.post('/account/~/extension/~/sms', {
             'from' : {'phoneNumber' : fromNumber},
             'to' : [{'phoneNumber' : sender}],
             'text' : 'This is an automatic reply'
        })
        print('SMS replied: %d' % (response.json().id))

    def pubnub():
        try:
            s = sdk.create_subscription()
            s.add_events(['/account/~/extension/~/message-store/instant?type=SMS'])
            s.on(Events.notification, on_message)
            res = s.register()
            try:
                f = open("subid.txt", "w")
                print (res.json().id)
                f.write(res.json().id)
                f.close()
            except Exception as e:
                print (e)
            while True:
                sleep(0.1)

        except KeyboardInterrupt:
            print("Pubnub listener stopped...")

    def unregister():
        try:
            f = open("subid.txt", "r")
            subId = f.read()
            f.close()
            if (len(subId)):
                response = platform.delete('/restapi/v1.0/subscription/%s' % (subId))
                print ("Cancelled old subscription.")
            else:
                print ("empty")
        except Exception as e:
            print (e)

    p = Process(target=pubnub)

    try:
        unregister()
        p.start()
    except KeyboardInterrupt:
        p.terminate()
        print("Stopped by User")

    print("Wait for notification...")


if __name__ == '__main__':
    main()