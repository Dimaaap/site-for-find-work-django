from django import forms

from .models import JobseekerProfileInfo


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfileInfo
        exclude = ['jobseeker', 'active_search', 'photo']

    expected_job = forms.CharField(label='Ваша очікувана посада: ',
                                   required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    telegram = forms.CharField(required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkedin = forms.URLField(required=False,
                              label='LinkedIn', widget=forms.URLInput(attrs={'class': 'form-control'}))
    git_hub = forms.URLField(required=False,
                             label='GitHub', widget=forms.URLInput(attrs={'class': 'form-control'}))

    cv = forms.FileField(required=False,
                         label='Прикріпіть ваш файл з резюме', widget=forms.FileInput(attrs={'class': 'cv_file'}))


class ProfilePhotoForm(forms.Form):
    photo = forms.ImageField(label='Завантажити нове фото', widget=forms.FileInput(attrs={'class': 'user-avatar'}))

