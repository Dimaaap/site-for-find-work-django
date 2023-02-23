import logging

from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.utils import IntegrityError
from twilio.base.exceptions import TwilioRestException

from .login_users import login_jobseeker_service
from .sms_codes import generate_code, send_sms_code
from ..forms import JobseekerLoginForm, JobseekerRegisterForm


logger = logging.getLogger(__name__)


class FormProcessor:

    @staticmethod
    def form_login_processor(form: JobseekerLoginForm, request):
        logger.info('Login user form has been validated successful')
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        login_jobseeker_service(request, email, password)

    @staticmethod
    def form_register_processor(form: JobseekerRegisterForm, request):
        logger.info('Register form validated success')
        full_name = form.cleaned_data['full_name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        hash_password = make_password(password)

        try:
            code = generate_code()
            send_sms_code(str(phone_number), code)
            session_tuple = (full_name, str(phone_number), email, hash_password, code)
            request.session['session_tuple'] = session_tuple
            logger.info('Success send code info a user number')
            request.session['valid'] = True

        except (TwilioRestException, IntegrityError) as e:
            request.session['valid'] = False
            logging.error('Fail to sent SMS-code')
            if e == TwilioRestException:
                messages.error(request, 'Неправильний формат номеру телефону.Введіть номер у форматі 380#########')
            else:
                messages.error(request, 'Користувач з таким email вже зареєстрований на сайті')
