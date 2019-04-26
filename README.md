# SMS Application Walk-through

Welcome to the SMS Application Walk-through and tour of a fully functional SMS application powered by RingCentral. In this walk through you will learn:

* How to send a SMS message.
* How to send an MMS message
* How to track the delivery status of a message.
* How to modify the message status.
* How to reply to an SMS message.

[![Community][community-img]][community-url]
[![Twitter][twitter-img]][twitter-url]

 [community-img]: https://img.shields.io/badge/dynamic/json.svg?label=community&colorB=&suffix=%20users&query=$.approximate_people_count&uri=http%3A%2F%2Fapi.getsatisfaction.com%2Fcompanies%2F102909.json
 [community-url]: https://devcommunity.ringcentral.com/ringcentraldev
 [twitter-img]: https://img.shields.io/twitter/follow/ringcentraldevs.svg?style=social&label=follow
 [twitter-url]: https://twitter.com/RingCentralDevs


### Clone - Setup - Run the project
```
$ git clone https://github.com/ringcentral-tutorials/sms-api-python-demo
$ cd sms-api-python-demo
$ python setup.py install
$ cp .env-sampledotenv .env
```
Specify your app client id and client secret as well as account login credentials to the .env file.

#### How to send SMS
```
$ python send-sms.py
```
#### How to send MMS
```
$ python send-mms.py
```
#### How to track delivery status of messages
```
$ python track-status.py
```
#### How to retrieve and modify message status
```
$ python retrieve-modify.py
```
#### How to delete a message
```
$ python retrieve-modify.py
```
#### How to receive and reply to SMS messages
```
$ python receive-reply.py
```

## RingCentral Python SDK
The SDK is available at https://github.com/ringcentral/ringcentral-python
