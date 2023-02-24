import logging
from random import choice

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.conf import settings
from django.contrib import messages


logger = logging.getLogger(__name__)


def generate_code():
    number_tuple = tuple(range(10))
    code_items = [choice(number_tuple) for i in range(5)]
    code_string = ''.join(str(i) for i in code_items)
    return code_string


def send_sms_code(to_number: str, code: str):
    account_sid = settings.ACCOUNT_SID
    auth_token = settings.AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your authentication code for Find.ua is - {code}',
        from_=settings.TWILIO_NUMBER,
        to=to_number
    )
    print(message.sid)


def send_sms(request, phone_number: str):
    code = generate_code()
    try:
        send_sms_code(phone_number, code)
        logger.info('Success send code info a user number')
    except TwilioRestException:
        messages.error(request, phone_number)
    return code



