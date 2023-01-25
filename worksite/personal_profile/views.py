from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jobseeker.models import JobseekerRegisterInfo
from .forms import ProfileInfoForm


@login_required
def main_profile_page_view(request, login):
    jobseeker = JobseekerRegisterInfo.objects.get(login=login)
    context = {'jobseeker': jobseeker, 'full_name': jobseeker.full_name,
               'login': jobseeker.login}
    if request.method == 'POST':
        form = ProfileInfoForm(request.POST)
        context['form'] = form
    context['form'] = ProfileInfoForm()
    return render(request, template_name='personal_profile/main_profile_page.html', context=context)

