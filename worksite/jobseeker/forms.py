from django import forms
from phonenumber_field.formfields import PhoneNumberField


class JobseekerRegisterForm(forms.Form):
    full_name = forms.CharField(max_length=255, min_length=6)
    phone_number = PhoneNumberField(region='UA')