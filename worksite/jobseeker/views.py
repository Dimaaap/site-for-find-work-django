from django.shortcuts import render


def jobseeker_login_view(request):
    title = 'Авторизація'
    return render(request, template_name='jobseeker/jobseeker_login.html', context={'title': title})


def jobseeker_register_view(request):
    title = 'Реєстрація'
    return render(request, template_name='jobseeker/jobseeker_register.html', context={'title': title})
