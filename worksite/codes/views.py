from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import CodeForm
from jobseeker.models import JobseekerRegisterInfo


def verificate_number_view(request):
    context = {'title': 'Підтвердження номеру'}
    form = CodeForm(request.POST or None)
    context['form'] = form
    pk = request.session.get('pk')
    if pk:
        jobseeker = JobseekerRegisterInfo.objects.get(pk=pk)
        code = jobseeker.code
        code_jobseeker = f'{jobseeker.username}: {jobseeker.code}'
        if not request.POST:
            # send SMS
            pass
        if form.is_valid():
            num = form.cleaned_data.get('number')
            if str(code) == num:
                code.save()
                login(request, jobseeker)
                return redirect('index_page')
            else:
                return redirect('login')

    return render(request, template_name='codes/code_verify.html', context=context)
