from random import choice

from twilio.rest import Client
from django.conf import settings


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


