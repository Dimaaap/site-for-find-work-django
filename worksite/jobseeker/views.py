import logging

from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import JobseekerRegisterForm, JobseekerLoginForm, CodeForm
from .models import JobseekerRegisterInfo
from .services.custom_errors import *
from .services.db_functions import create_user_login
from .services.form_processor import FormProcessor
from .decorators import redirect_login_user

logger = logging.getLogger(__name__)


@redirect_login_user
def jobseeker_login_view(request):
    page_title = 'Авторизація'
    context = {'title': page_title}
    if request.method == 'POST':
        form = JobseekerLoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            FormProcessor.form_login_processor(form, request)
        else:
            context['list_first_error'] = get_form_errors_service(form)
            logging.warning("Register form wasn`t valid")
    else:
        form = JobseekerLoginForm()
        context['form'] = form
    return render(request, template_name='jobseeker/jobseeker_login.html', context=context)


@redirect_login_user
def jobseeker_register_view(request):
    context = {'title': 'Реєстрація'}
    if request.method == 'POST':
        form = JobseekerRegisterForm(request.POST)
        context['form'] = form
        if form.is_valid():
            FormProcessor.form_register_processor(form, request)
            if request.session.get('valid'):
                return redirect('code_verification')
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
