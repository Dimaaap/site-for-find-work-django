import logging

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from jobseeker.models import JobseekerRegisterInfo
from .services.db_utils import *
from .services.utils import (update_form_data, update_cv_field_in_model,
                             create_jobseeker_profile_service, set_field_initial_values)
from .services.file_utils import *
from .models import JobseekerProfileInfo
from .forms import ProfilePhotoForm, WorkCriteriaForm

logger = logging.getLogger(__name__)


@login_required
def main_profile_page_view(request, login):
    jobseeker = get_fields_from_db(JobseekerRegisterInfo, 'login', login)
    context = {'jobseeker': jobseeker, 'full_name': jobseeker.full_name,
               'login': jobseeker.login}
    jobseeker_profile = create_jobseeker_profile_service(jobseeker, 'jobseeker', jobseeker)
    profile_data_form = set_field_initial_values(request, jobseeker_profile)
    context['first_form'] = profile_data_form
    context['view_access'] = request.session.get('view_access')
    second_form = ProfilePhotoForm(request.POST or None)
    context['second_form'] = second_form
    context['jobseeker_profile'] = jobseeker_profile
    if profile_data_form.is_valid():
        cv_file = request.FILES.get('cv_file', False)
        if cv_file and validate_file_extension(str(cv_file)):
            new_data = profile_data_form.save(commit=False)
            new_data.cv_file = cv_file
            new_data.jobseeker = jobseeker
        if jobseeker_profile:
            arguments = ('jobseeker', jobseeker)
            update_form_data(form=profile_data_form, model=JobseekerProfileInfo,
                             filter_args=arguments)
            context['jobseeker_profile'] = jobseeker_profile
            if request.FILES:
                context['request_files'] = request.FILES
                context['cv_file'] = os.path.basename(str(cv_file))
                if update_cv_field_in_model(model=JobseekerProfileInfo, tuple_args=arguments,
                                            cv_file=cv_file):
                    logger.info('success adding a file to db')
                else:
                    logger.error('Error adding file in update_cv_field_in_model function')
            else:
                context['cv_file'] = os.path.basename(str(jobseeker_profile.cv_file))
        else:
            new_data.save()
            logger.info('Successfully adding write to db')
        messages.success(request, '???????? ???????? ?????????????? ????????????')
    return render(request, template_name='personal_profile/main_profile_page.html',
                  context=context)


@login_required
def set_user_image_view(request, login):
    jobseeker = get_fields_from_db(JobseekerRegisterInfo, 'login', login)
    jobseeker_profile = get_fields_from_db(JobseekerProfileInfo, 'jobseeker', jobseeker)
    image_form = ProfilePhotoForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if image_form.is_valid():
            image = request.FILES.get('add-photo')
            if image and validate_image_extension(image):
                context['image'] = image
                context['jobseeker_profile'] = jobseeker_profile
                jobseeker_profile.photo = image
                try:
                    jobseeker_profile.save()
                except Exception as e:
                    print(e)
                    logger.error('Error downloading an image file with form')
            else:
                context['image'] = False
                messages.error(request, '???????????????????????? ????????????.???????? ?????????????? ???????? ???????? '
                                        '???? ????????????????:.png, .jpg, .jpeg')
        else:
            messages.error(request, '?????????????? ??????????????')
    return redirect('jobseeker_profile', login=jobseeker.login)


def work_criteria_view(request, login):
    work_criteria_form = WorkCriteriaForm(request.POST or None)
    return render(request, 'personal_profile/work_criteria.html',
                  context={'form': work_criteria_form})


@login_required
def delete_file_view(request, pk: int):
    profile = get_fields_from_db(JobseekerProfileInfo, 'pk', pk)
    profile.cv_file = None
    profile.save()
    return redirect('jobseeker_profile', login=profile.jobseeker.login)
