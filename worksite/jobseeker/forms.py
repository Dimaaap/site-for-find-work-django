from django import forms
from phonenumber_field.formfields import PhoneNumberField
from captcha.fields import CaptchaField
from werkzeug.security import check_password_hash

from .models import JobseekerRegisterInfo, Code
from .services.db_functions import (select_all_fields_from_model, select_field_value_from_model,
                                    get_write_from_model)


class JobseekerRegisterForm(forms.ModelForm):
    class Meta:
        model = JobseekerRegisterInfo
        fields = ('full_name', 'phone_number', 'email', 'hashed_password')

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

    def clean_email(self):
        email = self.cleaned_data['email']
        if email in select_field_value_from_model(JobseekerRegisterInfo, 'email', email):
            raise forms.ValidationError('Користувач з таким email вже зареєстрований на сайті')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number in select_field_value_from_model(JobseekerRegisterInfo, 'phone_number',
                                                         phone_number):
            raise forms.ValidationError('Користувач з таким номером телефону вже зареєстрований на сайті')
        return phone_number


class JobseekerLoginForm(forms.Form):
    email = forms.EmailField(label='Введіть ваш Email: ',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Ваш пароль: ',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        # if not select_field_value_from_model(JobseekerRegisterInfo, 'email', email):
        if not JobseekerRegisterInfo.objects.filter(email=email):
            raise forms.ValidationError('Неправильно введені email або пароль')
        return email

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     jobseeker = get_write_from_model(JobseekerRegisterInfo, 'email', email)
    #     if not jobseeker and not check_password_hash(jobseeker.hashed_password, password):
    #         raise forms.ValidationError('Не правильний логін або пароль')
    #     return password


class CodeVerifyForm(forms.ModelForm):
    code = forms.CharField(label='Код,який ми надіслали вам у SMS',
                           help_text='Введіть код,який ми надіслали на ваш телефон',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Code
        fields = ('code',)
