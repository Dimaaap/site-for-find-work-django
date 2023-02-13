from django import forms
from django.forms import ValidationError
from django.conf import settings

from jobseeker.models import JobseekerRegisterInfo


class PasswordRemindRequestForm(forms.Form):

    email = forms.EmailField(label='Введіть ваш email: ',
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        jobseeker = JobseekerRegisterInfo.objects.filter(email=email)
        if not jobseeker or email != settings.DEBUG_EMAIL:
            raise ValidationError('Жоден користувач сайту не зареєстрований з таким email')
        return email
