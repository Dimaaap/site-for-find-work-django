from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from jobseeker.models import JobseekerRegisterInfo
from .services.check_cleaned_data import check_cleaned_data
from .services.db_utils import *
from .models import JobseekerProfileInfo
from .forms import ProfileInfoForm, ProfilePhotoForm


@login_required
def main_profile_page_view(request, login):
    jobseeker = get_fields_from_db(JobseekerRegisterInfo, 'login', login)
    context = {'jobseeker': jobseeker, 'full_name': jobseeker.full_name, 'login': jobseeker.login}
    jobseeker_profile = get_fields_from_db(JobseekerProfileInfo, 'jobseeker', jobseeker)
    initial_values = {'expected_job': jobseeker_profile.expected_job,
                      'telegram': jobseeker_profile.telegram,
                      'linkedin': jobseeker_profile.linkedin,
                      'git_hub': jobseeker_profile.git_hub}
    first_form = ProfileInfoForm(request.POST or None, initial=initial_values)
    context['first_form'] = first_form
    second_form = ProfilePhotoForm(request.POST or None)
    context['second_form'] = second_form
    if first_form.is_valid():
        new_data = first_form.save(commit=False)
        new_data.jobseeker = jobseeker
        if jobseeker_profile:
            fields = ('expected_job', 'telegram', 'linkedin', 'git_hub', 'cv')
            check_cleaned_data(fields, first_form.cleaned_data)
            try:
                jobseeker_profile_filter = filter_fields_from_db(JobseekerProfileInfo, 'jobseeker',
                                                                 jobseeker)
                jobseeker_profile_filter.update(jobseeker=jobseeker, **first_form.cleaned_data)
            except Exception as e:
                print(e)
                messages.error(request, 'Виникла помилка додавання даних')
        else:
            new_data.save()
        messages.success(request, 'Ваші дані успішно додано')
    else:
        messages.error(request, 'Помилка додавання даних')

    return render(request, template_name='personal_profile/main_profile_page.html', context=context)
