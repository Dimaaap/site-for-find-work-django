import logging

from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import login
from django.db.utils import IntegrityError
from twilio.base.exceptions import TwilioRestException

from .login_users import login_jobseeker_service
from .sms_codes import send_sms
from .db_functions import create_user_login
from .session_utils import write_session_args_as_tuple
from ..forms import JobseekerLoginForm, JobseekerRegisterForm, CodeForm

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
        phone_number = str(form.cleaned_data['phone_number'])
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        hash_password = make_password(password)

        try:
            code = send_sms(request, phone_number)
            write_session_args_as_tuple(request, full_name, phone_number, email,
                                        hash_password, code)
            request.session['valid'] = True
        except (TwilioRestException, IntegrityError) as e:
            request.session['valid'] = False
            logging.error('Fail to sent SMS-code')
            if e == TwilioRestException:
                messages.error(request, 'Неправильний формат номеру телефону.Введіть номер у форматі 380#########')
            else:
                messages.error(request, 'Користувач з таким email вже зареєстрований на сайті')

    @staticmethod
    def code_verificate_form_processor(form: CodeForm, request, code: str, user):
        session_tuple = request.session.get('session_tuple')
        user_login = create_user_login(session_tuple[2])
        number = form.cleaned_data.get('number')
        if code == number:
            user.login = user_login
            user.save()
            request.session['login'] = user_login
            login(request, user, backend='jobseeker.authentication.WithoutPasswordBackend')
            return True
        return False
