import logging

from app.config import ACCOUNT_SID, AUTH_TOKEN, SLACK_TOKEN, SLACK_CHANNEL

from twilio.rest import Client
from slackclient import SlackClient

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)
slack_client = SlackClient(SLACK_TOKEN)

class Notification:
    def send_sms(self, sms_body, addressee):
        message = twilio_client.messages \
                        .create(
                            body=sms_body,
                            from_='+12054650317',
                            to= addressee
                        )
        if message.sid:
            return message.sid, 'sms sent succesfully!'
        else:
            return 'failed to send sms!'

    def send_slack_message(self, slack_message_body):
        response = slack_client.api_call(
            "chat.postMessage",
            channel=SLACK_CHANNEL,
            text=slack_message_body,
            username='alertsBot',
            icon_emoji=':robot_face:'
        )
        
        if response.ok == True:
            return response, 'slack messaged sent succesfully!'
        else:
            return response, 'failed to send slack message!'
