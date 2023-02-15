from datetime import datetime, date, timedelta
import functools
from json import dumps

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

from .forms import PasswordRemindRequestForm, PasswordChangeForm
from .services import jobseeker_change_password_service, send_email_service
from jobseeker.models import JobseekerRegisterInfo


def limiter_access_in_time(view_function, redirect_url='jobseeker-profile'):
    # -------------------------------
    # TODO: FIXED IT
    # -------------------------------
    @functools.wraps(view_function)
    def inner(request, *args, **kwargs):
        current_time = datetime.now()
        if (request.session.get('last_access') is None or
                current_time >= datetime.strptime(request.session.get('last_access'),
                                                  settings.DATE_FORMAT) + timedelta(minutes=30)):
            print(f'{datetime.now().isoformat()}-dasdisajdisad')
            request.session['last_access'] = dumps(datetime.now().isoformat())
            print("I`m here")
            return view_function(request, *args, **kwargs)
        else:
            print("Time access")
            return redirect(redirect_url)

    return inner


@login_required
@limiter_access_in_time
def remind_password_view(request, login):
    request_user = JobseekerRegisterInfo.objects.get(login=login)
    token = request_user.get_reset_password_token()
    request.session['login'] = login
    context = {}
    if request.method == 'POST':
        form = PasswordRemindRequestForm(request.POST)
        if form.is_valid():
            email = str(form.cleaned_data.get('email')).strip()
            if email == request_user.email or email == settings.DEBUG_EMAIL:
                result = send_email_service({'username': request_user.login, 'token': token},
                                            'password/email/email_text.html')
                context['success'] = result
            else:
                messages.error(request, 'Введено неправильний email')
        else:
            print(form.errors.as_data())
    else:
        form = PasswordRemindRequestForm()
    context['form'] = form
    return render(request, 'password/remind_password.html', context=context)


@login_required
def change_password_page(request, token):
    context = {}
    jobseeker = JobseekerRegisterInfo.verify_reset_password_token(token)
    if not jobseeker:
        context['wrong_token'] = True
        context['login'] = request.session.get('login')
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.POST)
        password = password_change_form.cleaned_data.get('password').strip()
        if password_change_form.is_valid():
            context['password_save'] = jobseeker_change_password_service(password, jobseeker)
    else:
        password_change_form = PasswordChangeForm()
    context['form'] = password_change_form
    return render(request, 'password/change_password.html', context=context)
