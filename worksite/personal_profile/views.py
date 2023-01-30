from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from jobseeker.models import JobseekerRegisterInfo
from .services.custom_errors import *
from .models import JobseekerProfileInfo
from .forms import ProfileInfoForm, ProfilePhotoForm


@login_required
def main_profile_page_view(request, login):
    jobseeker = JobseekerRegisterInfo.objects.get(login=login)

    # context = {'jobseeker': jobseeker, 'full_name': jobseeker.full_name, 'login': jobseeker.login,
    #            'first_form': ProfileInfoForm(request.POST or None),
    #            'second_form': ProfilePhotoForm(request.POST or None)}
    #
    context = {'jobseeker': jobseeker, 'full_name': jobseeker.full_name, 'login': jobseeker.login}
    first_form = ProfileInfoForm(request.POST or None)
    context['first_form'] = first_form
    second_form = ProfilePhotoForm(request.POST or None)
    context['second_form'] = second_form
    if first_form.is_valid():
        new_data = first_form.save(commit=False)
        new_data.jobseeker = jobseeker
        print("I`m here")
        new_data.save()
        messages.success(request, 'Ваші дані успішно додано')
        print(first_form.cleaned_data['telegram'])
    else:
        form_errors = first_form.errors.as_data()
        custom_errors = custom_error_service(form_errors)
        context['list_first_error'] = custom_errors

    return render(request, template_name='personal_profile/main_profile_page.html', context=context)
