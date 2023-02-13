from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .forms import PasswordRemindRequestForm
from jobseeker.models import JobseekerRegisterInfo


@login_required
def remind_password_view(request, login):
    request_user = JobseekerRegisterInfo.objects.get(login=login)
    print(request_user.login)
    if request.method == 'POST':
        form = PasswordRemindRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if email == request_user.email or email == settings.DEBUG_EMAIL:
                print("I`m here")
                html_content_context = {'username': request_user.login}
                html_content = render_to_string('password/email/email_text.html', html_content_context)
                send_mail(subject='Зміна паролю', message='dsadadsad', from_email=settings.EMAIL_HOST_USER,
                          recipient_list=(settings.DEBUG_EMAIL, ), html_message=html_content)
            else:
                messages.error(request, 'Введено неправильний email')
                print('dasdsa')
        else:
            print(form.errors.as_data())
    else:
        form = PasswordRemindRequestForm()
    return render(request, 'password/remind_password.html', {'form': form})
