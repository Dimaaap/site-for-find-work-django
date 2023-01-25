from django import forms

from .models import JobseekerProfileInfo


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfileInfo
        exclude = ['jobseeker', 'active_search', 'photo']

    # photo = forms.ImageField(label='Завантажте своє фото', widget=forms.FileInput(attrs={'class': 'form-file'}))
    #header = forms.CharField(label='Напишіть декілька слів про себе',
                             #help_text='Введіть трохи інформації про себе',
                             #widget=forms.Textarea(attrs={'class': 'form-header-input'}))

    expected_job = forms.CharField(label='Вкажіть вашу очікувану роботу',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    telegram = linkedin = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    git_hub = forms.URLField(label='GitHib', widget=forms.URLInput(attrs={'class': 'form-control'}))

    cv = forms.FileField(label='Прикріпіть ваш файл з резюме')
