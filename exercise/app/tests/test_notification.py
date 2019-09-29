import unittest
import responses

from app.notification import Notification

class TestClassNotification(unittest.TestCase):
    @responses.activate
    def test_notification_send_sms_successfully(self):
        payload = {
            'account_sid': 'account_sid',
            'api_version': 'api_version',
            'body': 'body',
            'date_created': '2019-01-23T06:17:59.273519',
            'date_updated': '2019-01-23T06:17:59.273519',
            'date_sent': '2019-01-23T06:17:59.273519',
            'direction': 'direction',
            'error_code': 0,
            'error_message': 'error_message',
            'from': 'from',
            'messaging_service_sid': 'messaging_service_sid',
            'num_media': 'num_media',
            'num_segments': 'num_segments',
            'price': 'price',
            'price_unit': 'price_unit',
            'sid': 'sid',
            'status': 'status',
            'subresource_uris': 'subresource_uris',
            'to': 'to',
            'uri': 'uri',
        }
           
        responses.add(responses.POST, 'https://api.twilio.com/2010-04-01/Accounts/AC713aafaa8fa6b70c48200b322434dbb9/Messages.json',
            json=payload, status=201)

        result = Notification().send_sms('Hello', '+33632941888')
        self.assertEqual(result, ('sid', 'sms sent succesfully!'))
        self.assertEqual(responses.calls[0].request.body, 'To=%2B33632941887&From=%2B12054650317&Body=Hello')

    @responses.activate
    def test_notification_send_sms_failed(self):
        payload = {
            'account_sid': 'account_sid',
            'api_version': 'api_version',
            'body': '',
            'date_created': '2019-01-23T06:17:59.273519',
            'date_updated': '2019-01-23T06:17:59.273519',
            'date_sent': '2019-01-23T06:17:59.273519',
            'direction': 'direction',
            'error_code': 1,
            'error_message': 'error_message',
            'from': 'from',
            'messaging_service_sid': 'messaging_service_sid',
            'num_media': 'num_media',
            'num_segments': 'num_segments',
            'price': 'price',
            'price_unit': 'price_unit',
            'sid': '',
            'status': 'status',
            'subresource_uris': 'subresource_uris',
            'to': 'to',
            'uri': 'uri',
        }
           
        responses.add(responses.POST, 'https://api.twilio.com/2010-04-01/Accounts/AC713aafaa8fa6b70c48200b322434dbb9/Messages.json',
            json=payload, status=201)

        result = Notification().send_sms('Hello', '+33632941888')
        self.assertEqual(result, ('failed to send sms!'))


if __name__ == '__main__':
  unittest.main()