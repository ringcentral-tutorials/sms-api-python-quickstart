from multiprocessing import Process
from time import sleep
from ringcentral.subscription import Events
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

def main():

    def pubnub():
        try:
            subscription = sdk.create_subscription()
            subscription.add_events(['/account/~/extension/~/message-store/instant?type=SMS'])
            subscription.on(Events.notification, on_message)
            res = subscription.register()
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

    def on_message(msg):
        senderNumber = msg['body']['from']['phoneNumber']
        response = platform.post('/restapi/v1.0/account/~/extension/~/sms', {
            'from': {'phoneNumber': os.getenv("RINGCENTRAL_USERNAME")},
            'to': [{'phoneNumber': senderNumber}],
            'text' : 'This is an automatic reply'
        })
        print('SMS replied: %d' % (response.json().id))

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
