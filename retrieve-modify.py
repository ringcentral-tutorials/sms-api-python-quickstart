import authentication
import datetime
import time

def retrieve_modify():
    lessXXDays = time.time() - (84600 * 1)
    dateFrom = datetime.datetime.fromtimestamp(lessXXDays).strftime("%Y-%m-%dT00:00:00.000Z")
    platform = authentication.get_platform()
    response = platform.get('/account/~/extension/~/message-store', {
        'dateFrom' : dateFrom
    })
    messages = response.json().records
    count = len(messages)
    print ("We get a list of %d messages" % (count))
    for i in range(count):
        if messages[i].readStatus == "Read":
            messageId = messages[i].id
            response = platform.put("/account/~/extension/~/message-store/%d" % (messageId), {
                'readStatus' : 'Unread'
                });
            readStatus = response.json().readStatus
            print("Message status has been changed to " + readStatus)

    if count:
        response = platform.delete("/account/~/extension/~/message-store/%d" % (messages[0].id))
        print("Message %d has been deleted" % (messages[0].id))

if __name__ == '__main__':
    retrieve_modify()
