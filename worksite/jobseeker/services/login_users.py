from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_jobseeker_service(request, email: str, password: str):
    jobseeker = authenticate(request, email=email, password=password)
    if jobseeker:
        login(request, jobseeker)
        messages.success(request, 'Чудово!Ви успішно авторизувались на сайті')
    else:
        messages.error(request, 'Неправильний логін або пароль')
