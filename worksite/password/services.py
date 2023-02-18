from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from jobseeker.models import JobseekerRegisterInfo


def jobseeker_change_password_service(password: str, jobseeker: JobseekerRegisterInfo):
    jobseeker.set_password(password)
    try:
        jobseeker.save()
        return True
    except Exception:
        return False


def send_email_service(html_context: dict, template_path: str):
    html_content_context = html_context
    html_content = render_to_string(template_path, html_content_context)
    if send_mail(subject='Зміна паролю', message='',
                 from_email=settings.EMAIL_HOST_USER,
                 recipient_list=(settings.DEBUG_EMAIL,), html_message=html_content):
        return True
    return False


def comparing_two_dates(second_time: datetime, period: int | float = 12,
                        first_time: datetime = datetime.now()):
    return first_time >= second_time + timedelta(seconds=3)
