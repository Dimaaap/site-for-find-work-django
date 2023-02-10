from django.shortcuts import render

from .forms import PasswordRemindRequestForm


def remind_password_view(request):
    if request.method == 'POST':
        form = PasswordRemindRequestForm(request.POST)
    else:
        form = PasswordRemindRequestForm()
    return render(request, 'password/remind_password.html', {'form': form})
