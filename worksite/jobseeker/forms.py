from django import forms
from phonenumber_field.formfields import PhoneNumberField
from captcha.fields import CaptchaField

from .models import JobseekerRegisterInfo, JobseekerProfileInfo
from .services.db_functions import select_field_value_from_model


class JobseekerRegisterForm(forms.Form):
    class Meta:
        model = JobseekerRegisterInfo
        fields = ('full_name', 'phone_number', 'email', 'password')

    full_name = forms.CharField(label="Ваше прізвище та ім'я", max_length=255, min_length=6,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = PhoneNumberField(label="Ваш номер телефону(буде потрібна SMS-верифікація)",
                                    region='UA', initial=380,
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Придумайте пароль', min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_repeat = forms.CharField(label='Повторіть пароль', min_length=6,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='Введіть літери з картинки')

    def clean_password(self):
        password = self.cleaned_data['password']
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
            raise forms.ValidationError('Користувач з таким номером телефону вже '
                                        'зареєстрований на сайті')
        return phone_number


class JobseekerLoginForm(forms.Form):
    email = forms.EmailField(label='Введіть ваш Email: ',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Ваш пароль: ',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        jobseeker = select_field_value_from_model(JobseekerRegisterInfo, 'email', email)
        if not jobseeker:
            raise forms.ValidationError('Неправильний email або пароль')
        return email


class CodeForm(forms.Form):
    number = forms.CharField(label='Введіть код',
                             max_length=5,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfileInfo
        exclude = ['jobseeker']

    photo = forms.ImageField(label='Завантажте своє фото')
    header = forms.CharField(label='Напишіть декілька слів про себе',
                             help_text='Введіть трохи інформації про себе',
                             widget=forms.Textarea())
    telegram = linkedin = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    git_hub = forms.URLField(label='GitHib', widget=forms.URLInput(attrs={'class': 'form-control'}))

    cv = forms.FileField(label='Прикріпіть ваш файл з резюме')
