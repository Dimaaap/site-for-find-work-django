from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from werkzeug.security import check_password_hash, generate_password_hash

from .forms import JobseekerRegisterForm, CodeVerifyForm, JobseekerLoginForm
from .models import JobseekerRegisterInfo
from .services.custom_errors import *
from .services.db_functions import *


def jobseeker_login_view(request):
    title = 'Авторизація'
    context = {'title': title}
    if request.method == 'POST':
        form = JobseekerLoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(generate_password_hash(password))
            if user:
                print(user)
            else:
                print('USER IS NONE')
        else:
            form_errors = form.errors.as_data()
            custom_error = custom_error_service(form_errors)
            context['list_first_error'] = custom_error
    else:
        form = JobseekerLoginForm()
        context['form'] = form
    return render(request, template_name='jobseeker/jobseeker_login.html', context=context)


def jobseeker_register_view(request):
    context = {'title': 'Реєстрація'}
    if request.method == 'POST':
        form = JobseekerRegisterForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
        else:
            form_errors = form.errors.as_data()
            custom_error = custom_error_service(form_errors)
            context['list_first_error'] = custom_error
    else:
        form = JobseekerRegisterForm
    context['form'] = form
    return render(request, template_name='jobseeker/jobseeker_register.html', context=context)


@login_required
def success_register_view(request):
    return render(request, template_name='jobseeker/jobseeker_success_register.html')


@login_required
def jobseeker_logout_view(request):
    logout(request)
    return render(request, template_name='jobseeker/jobseeker_logout.html')
