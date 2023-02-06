import logging

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db.utils import IntegrityError
from twilio.base.exceptions import TwilioRestException

from .forms import JobseekerRegisterForm, JobseekerLoginForm, CodeForm
from .models import JobseekerRegisterInfo
from .services.custom_errors import *
from .services.sms_codes import generate_code, send_sms_code
from .services.db_functions import create_user_login

logger = logging.getLogger(__name__)


def jobseeker_login_view(request):
    if request.user.is_authenticated:
        return redirect('index_page', permanent=True)
    title = 'Авторизація'
    context = {'title': title}
    if request.method == 'POST':
        form = JobseekerLoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            logger.info('Login user form has been validated successful')
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            jobseeker = authenticate(request, email=email, password=password)
            if jobseeker:
                login(request, jobseeker)
                messages.success(request, 'Чудово!Ви успішно авторизувались на сайті')
                logger.info('Successful login')
                return redirect('index_page')
            else:
                messages.error(request, 'Неправильний логін або пароль')
                logger.warning('Failed login because login or password was false')
        else:
            context['list_first_error'] = get_form_errors_service(form)
            logging.warning("Register form wasn`t valid")

    else:
        form = JobseekerLoginForm()
        context['form'] = form
    return render(request, template_name='jobseeker/jobseeker_login.html', context=context)


def jobseeker_register_view(request):
    if request.user.is_authenticated:
        logger.info('Authenticated user tried to download the register page')
        return redirect('index_page', permanent=True)
    context = {'title': 'Реєстрація'}
    if request.method == 'POST':
        form = JobseekerRegisterForm(request.POST)
        context['form'] = form
        if form.is_valid():
            logger.info('Register form validated success')
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            hash_password = make_password(password)
            try:

                ### МОЖЛИВО ВАРТО НАДСИЛАТИ ПОВІДОМЛЕННЯ
                ### ІЗ КОДОМ ДЛЯ ВЕРИФІКАЦІЇ МОБІЛЬНОГО
                ### ПРЯМО ТУТ?????????????????????
                try:
                    code = generate_code()
                except TwilioRestException:
                    messages.error(request, 'Неправильно набраний номер телефону')
                    logger.warning('User input wrong mobile number')
                else:
                    send_sms_code(str(phone_number), code)
                    session_tuple = (full_name, str(phone_number), email, hash_password, code)
                    request.session['session_tuple'] = session_tuple
                    logger.info('Success sent code into a user number')
                    return redirect('code_verification')
            except (IntegrityError, TwilioRestException):
                logging.error('Fail to sent SMS-code to user')
                messages.error(request, 'Користувач з таким email вже зареєстрований на сайті')
        else:
            context['list_first_error'] = get_form_errors_service(form)
            logging.warning("Register form wasn`t valid")
    else:
        form = JobseekerRegisterForm()
    context['form'] = form
    return render(request, template_name='jobseeker/jobseeker_register.html', context=context)


def verificate_number_view(request):
    context = {'title': 'Підтвердження номеру'}
    if request.user.is_authenticated:
        return redirect('index_page', permanent=True)
    form = CodeForm(request.POST or None)
    session_tuple = request.session['session_tuple']
    context['form'] = form
    user_login = create_user_login(session_tuple[2])
    user = JobseekerRegisterInfo(full_name=session_tuple[0],
                                 phone_number=session_tuple[1],
                                 email=session_tuple[2],
                                 password=session_tuple[3],
                                 login=user_login)
    if user.email:
        code = request.session.get('session_tuple')[-1]
        if form.is_valid():
            num = form.cleaned_data.get('number')
            if str(code) == num:
                user.save()
                request.session['login'] = user_login
                login(request, user, backend='jobseeker.authentication.WithoutPasswordBackend')
                return redirect('jobseeker_profile', user.login)
            else:
                messages.error(request, 'Введено неправильний код')

    return render(request, template_name='jobseeker/code_verify.html', context=context)


@login_required
def success_register_view(request):
    return render(request, template_name='jobseeker/jobseeker_success_register.html')


@login_required
def jobseeker_logout_view(request):
    logout(request)
    return render(request, template_name='jobseeker/jobseeker_logout.html')
