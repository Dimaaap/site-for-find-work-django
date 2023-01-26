from django import forms

from .models import JobseekerProfileInfo


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfileInfo
        exclude = ['jobseeker', 'active_search', 'photo']

    expected_job = forms.CharField(label='Вкажіть вашу очікувану роботу',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    telegram = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    linkedin = forms.URLField(label='LinkedIn', widget=forms.URLInput(attrs={'class': 'form-control'}))
    git_hub = forms.URLField(label='GitHub', widget=forms.URLInput(attrs={'class': 'form-control'}))

    cv = forms.FileField(label='Прикріпіть ваш файл з резюме')


class ProfilePhotoForm(forms.Form):
    photo = forms.ImageField(label='Завантажити нове фото', widget=forms.FileInput(attrs={'class': 'user-avatar'}))

