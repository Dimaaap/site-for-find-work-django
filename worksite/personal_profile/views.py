from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jobseeker.models import JobseekerRegisterInfo
from .models import JobseekerProfileInfo
from .forms import ProfileInfoForm, ProfilePhotoForm


@login_required
def main_profile_page_view(request, login):
    jobseeker = JobseekerRegisterInfo.objects.get(login=login)
    context = {'jobseeker': jobseeker, 'full_name': jobseeker.full_name,
               'login': jobseeker.login}
    context['first_form'] = ProfileInfoForm(request.POST or None)
    context['second_form'] = ProfilePhotoForm(request.POST or None)
    return render(request, template_name='personal_profile/main_profile_page.html', context=context)
