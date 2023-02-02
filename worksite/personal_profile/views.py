import logging

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from jobseeker.models import JobseekerRegisterInfo
from .services.check_cleaned_data import check_cleaned_data
from .services.db_utils import *
from .models import JobseekerProfileInfo
from .forms import ProfileInfoForm, ProfilePhotoForm

logger = logging.getLogger(__name__)


@login_required
def main_profile_page_view(request, login):
    logger.warning('dlskdlsakdlsakdladlsakdlsa')
    jobseeker = get_fields_from_db(JobseekerRegisterInfo, 'login', login)
    context = {'jobseeker': jobseeker, 'full_name': jobseeker.full_name, 'login': jobseeker.login}
    jobseeker_profile = get_fields_from_db(JobseekerProfileInfo, 'jobseeker', jobseeker)
    initial_values = {'expected_job': jobseeker_profile.expected_job,
                      'telegram': jobseeker_profile.telegram,
                      'linkedin': jobseeker_profile.linkedin,
                      'git_hub': jobseeker_profile.git_hub}
    profile_data_form = ProfileInfoForm(request.POST or None, initial=initial_values)
    context['first_form'] = profile_data_form
    second_form = ProfilePhotoForm(request.POST or None)
    context['second_form'] = second_form
    if profile_data_form.is_valid():
        cv_file = request.FILES['cv']
        new_data = profile_data_form.save(commit=False)
        new_data.jobseeker = jobseeker
        new_data.cv = cv_file
        if jobseeker_profile:
            fields = ('expected_job', 'telegram', 'linkedin', 'git_hub', 'cv')
            check_cleaned_data(fields, profile_data_form.cleaned_data)
            try:
                jobseeker_profile_filter = filter_fields_from_db(JobseekerProfileInfo, 'jobseeker',
                                                                 jobseeker)
                context['jobseeker_profile'] = jobseeker_profile
                if cv_file:
                    jobseeker_profile_filter.update(jobseeker=jobseeker, **profile_data_form.cleaned_data, cv=cv_file)
                else:
                    jobseeker_profile_filter.update(jobseeker=jobseeker, **profile_data_form.cleaned_data)
            except Exception as e:
                print(e)
                messages.error(request, 'Виникла помилка додавання даних')
        else:
            new_data.save()
        messages.success(request, 'Ваші дані успішно додано')
    return render(request, template_name='personal_profile/main_profile_page.html', context=context)
