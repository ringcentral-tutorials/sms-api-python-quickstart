from ringcentral import SDK
import os
import datetime
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

def retrieve_modify():
    lessXXDays = time.time() - (84600 * 1)
    dateFrom = datetime.datetime.fromtimestamp(lessXXDays).strftime("%Y-%m-%dT00:00:00.000Z")
    response = platform.get('/account/~/extension/~/message-store', {
        'dateFrom' : dateFrom,
        'readStatus' : "Read"
    })
    messages = response.json().records
    count = len(messages)
    print ("We get a list of %d messages" % (count))
    if count:
        messageId = messages[0].id
        response = platform.put("/account/~/extension/~/message-store/%d" % (messageId), {
            'readStatus' : 'Unread'
            });
        readStatus = response.json().readStatus
        print("Message status has been changed to " + readStatus)

        response = platform.delete("/account/~/extension/~/message-store/%d" % (messages[0].id))
        print("Message %d has been deleted" % (messages[0].id))

if __name__ == '__main__':
    retrieve_modify()
