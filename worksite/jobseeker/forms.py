from django import forms
from phonenumber_field.formfields import PhoneNumberField
from captcha.fields import CaptchaField

from .models import JobseekerRegisterInfo


class JobseekerRegisterForm(forms.ModelForm):

    class Meta:
        model = JobseekerRegisterInfo
        fields = ['full_name', 'phone_number', 'email', 'hashed_password']

    full_name = forms.CharField(label="Ваше прізвище та ім'я", max_length=255, min_length=6,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = PhoneNumberField(label="Ваш номер телефону(буде потрібна SMS-верифікація)",
                                    region='UA', initial=380,
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    hashed_password = forms.CharField(label='Придумайте пароль', min_length=6,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_repeat = forms.CharField(label='Повторіть пароль', min_length=6,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='Введіть літери з картинки')

    def clean_password(self):
        password = self.cleaned_data['hashed_password']
        if all([i.isdigit() for i in password]) or all([i.isalpha() for i in password]):
            raise forms.ValidationError('Надто простий пароль.'
                                        'Він має містити хоча б 6 символів,літери і цифри')
        return password

    def clean_password_repeat(self):
        password_repeat = self.cleaned_data['password_repeat']
        password = self.clean_password()
        if password != password_repeat:
            raise forms.ValidationError('Значення паролів не співпадають')
        return password