import authentication

def retrieve_modify():
    platform = authentication.get_platform()
    response = platform.get('/account/~/extension/~/message-store', {
        'dateFrom' : '2018-05-03T06:33:00.000Z'
    })
    messages = response.json().records
    count = len(messages)
    print ("We get a list of %d messages" % (count))

    #messageId = messages[0].id
    #response = platform.put("/account/~/extension/~/message-store/%d" % (messageId), {
    #    'readStatus' : 'Read'
    #});
    #readStatus = response.json().readStatus;
    #print("Message readStatus has been changed to " + readStatus);
    #
    #response = platform.delete("/account/~/extension/~/message-store/" + str(messageId));
    #print("Message {$messageId} has been deleted");

if __name__ == '__main__':
    retrieve_modify()
