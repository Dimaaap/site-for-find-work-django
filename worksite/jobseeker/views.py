from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate

from .forms import JobseekerRegisterForm, CodeVerifyForm, JobseekerLoginForm
from .services.custom_errors import *


def jobseeker_login_view(request):
    title = 'Авторизація'
    context = {'title': title}
    if request.method == 'POST':
        form = JobseekerLoginForm(request.POST)
        context['form'] = form
        if form.is_valid():
            pass
        else:
            pass
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
            messages.success(request, 'Реєстрація успішна')
            form.save()
            return redirect('login')
        else:
            form_errors = form.errors.as_data()
            custom_error = custom_error_service(form_errors)
            context['list_first_error'] = custom_error
    else:
        form = JobseekerRegisterForm
    context['form'] = form
    return render(request, template_name='jobseeker/jobseeker_register.html', context=context)



