from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

from .forms import PasswordRemindRequestForm, PasswordChangeForm
from jobseeker.models import JobseekerRegisterInfo


@login_required
def remind_password_view(request, login):
    request_user = JobseekerRegisterInfo.objects.get(login=login)
    context = {}
    if request.method == 'POST':
        form = PasswordRemindRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if email == request_user.email or email == settings.DEBUG_EMAIL:
                html_content_context = {'username': request_user.login}
                html_content = render_to_string('password/email/email_text.html', html_content_context)
                send_mail(subject='Зміна паролю', message='dsadadsad', from_email=settings.EMAIL_HOST_USER,
                          recipient_list=(settings.DEBUG_EMAIL,), html_message=html_content)
                context['success'] = 1
            else:
                messages.error(request, 'Введено неправильний email')
                print('dasdsa')
        else:
            print(form.errors.as_data())
    else:
        form = PasswordRemindRequestForm()
    context['form'] = form
    return render(request, 'password/remind_password.html', context=context)


@login_required
def change_password_page(request, token):
    context = {}
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.POST)
        if password_change_form.is_valid():
            pass
    else:
        password_change_form = PasswordChangeForm()
    context['form'] = password_change_form
    return render(request, 'password/change_password.html', context=context)
