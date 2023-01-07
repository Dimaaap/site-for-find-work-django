from django.shortcuts import render

from .forms import JobseekerRegisterForm


def jobseeker_login_view(request):
    title = 'Авторизація'
    return render(request, template_name='jobseeker/jobseeker_login.html', context={'title': title})


def jobseeker_register_view(request):
    title = 'Реєстрація'
    if request.method == 'POST':
        form = JobseekerRegisterForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = JobseekerRegisterForm
    context = {'title': title, 'form': form}
    return render(request, template_name='jobseeker/jobseeker_register.html', context=context)
