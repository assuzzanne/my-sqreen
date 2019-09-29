from app import app

from flask import request, abort
import logging

from app.config import SECRET_KEY
from app.lib.check_signature import check_signature

from app.notification import Notification

@app.route('/webhook', methods=['POST'])
def process_sqreen_webhook():
    if request.method == 'POST':
        request_body = request.get_data()
        request_signature = request.headers['X-Sqreen-Integrity']
        signature_checked = check_signature(SECRET_KEY, request_signature, request_body)

        if signature_checked == True:
            sms = Notification().send_sms(request_body, "+33632941888")
            logging.info(sms)

            slack_message = Notification().send_slack_message(request_body)
            logging.info(slack_message)
            return 'notifications sent!', 200
        else:
            return 'signature checked failed!', abort(400)
    