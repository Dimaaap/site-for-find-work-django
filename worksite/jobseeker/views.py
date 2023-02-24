import logging

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import JobseekerRegisterForm, JobseekerLoginForm, CodeForm
from .services.custom_errors import *
from .services.session_utils import unpack_session_tuple_in_user
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


@redirect_login_user
def verificate_number_view(request):
    context = {'title': 'Підтвердження номеру'}
    if request.method == 'POST':
        form = CodeForm(request.POST)
        session_tuple = request.session['session_tuple']
        user = unpack_session_tuple_in_user(session_tuple)
        code = request.session.get('session_tuple')[-1]
        if form.is_valid():
            FormProcessor.code_verificate_form_processor(form, request, code, user)
        else:
            messages.error(request, 'Введено неправильний код')
    else:
        form = CodeForm()
    context['form'] = form
    return render(request, template_name='jobseeker/code_verify.html', context=context)


@login_required
def success_register_view(request):
    return render(request, template_name='jobseeker/jobseeker_success_register.html')


@login_required
def jobseeker_logout_view(request):
    logout(request)
    return render(request, template_name='jobseeker/jobseeker_logout.html')
