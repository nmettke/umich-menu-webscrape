import twilio

from twilio.rest import Client

account_sid = 'ACa1b99017fefaa4d838076cfb209bc9b2'
auth_token = 'bdb9b47df85af70ccf304b3eaa12d03b'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18559064470',
  body='hi chance',
  to='+17342318482'
)

print(message.sid)
