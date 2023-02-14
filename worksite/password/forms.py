from django import forms
from django.forms import ValidationError
from django.conf import settings

from jobseeker.models import JobseekerRegisterInfo
from global_services import validators


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


class PasswordChangeForm(forms.Form):
    password = forms.CharField(
        label="Введіть ваш новий пароль ",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=6,
        max_length=100
    )

    password_repeat = forms.CharField(
        label="Повторіть пароль ",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean_password(self):
        password = self.cleaned_data['password']
        if not validators.is_valid_password_symbols(password):
            raise ValidationError('Пароль повинен містити літери(a-zA-Z) і як мінімум одну цифру(1-9)')
        return password

    def clean_password_repeat(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise ValidationError('Значення паролів не співпадають')

        return cleaned_data




