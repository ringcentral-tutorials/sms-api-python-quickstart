# Messages API Python Quickstart

[![Community][community-img]][community-url]
[![Twitter][twitter-img]][twitter-url]

 [community-img]: https://img.shields.io/badge/dynamic/json.svg?label=community&colorB=&suffix=%20users&query=$.approximate_people_count&uri=http%3A%2F%2Fapi.getsatisfaction.com%2Fcompanies%2F102909.json
 [community-url]: https://devcommunity.ringcentral.com/ringcentraldev
 [twitter-img]: https://img.shields.io/twitter/follow/ringcentraldevs.svg?style=social&label=follow
 [twitter-url]: https://twitter.com/RingCentralDevs

A quickstart tutorial to teach users to use RingCentral Messages API. The following topics are included:

- How to send SMS
- How to send MMS
- How to track delivery status of messages
- How to retrieve and modify message history
- How to receive and reply to SMS messages

### Clone - Setup - Run the project
```
$ git clone https://github.com/ringcentral-tutorials/sms-api-python-quickstart

$ cd sms-api-python-quickstart

$ pip install ringcentral

$ pip install python-dotenv

$ cp dotenv .env
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
$ python tract-status.py
```
#### How to retrieve and modify message history
```
$ python retrieve-modify.py
```
#### How to receive and reply to SMS messages
```
$ python receive-reply.py
```

## RingCentral Python SDK
The SDK is available at https://github.com/ringcentral/ringcentral-python
