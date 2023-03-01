from django import forms
from django.conf import settings

from .models import JobseekerProfileInfo, WorkCriteria, City, Country


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfileInfo
        exclude = ['jobseeker', 'active_search', 'photo']

    expected_job = forms.CharField(label='Ваша очікувана посада: ',
                                   required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    telegram = forms.CharField(label='Telegram: ',
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkedin = forms.URLField(required=False,
                              label='LinkedIn: ',
                              widget=forms.URLInput(attrs={'class': 'form-control'}))
    git_hub = forms.URLField(required=False,
                             label='GitHub: ',
                             widget=forms.URLInput(attrs={'class': 'form-control'}))

    cv_file = forms.FileField(required=False,
                              label='Прикріпіть ваш файл з резюме: ',
                              widget=forms.FileInput(attrs={'class': 'cv_file',
                                                            'name': 'cv-file'}))


class ProfilePhotoForm(forms.Form):
    photo = forms.ImageField(required=False,
                             label='Завантажити нове фото',
                             widget=forms.FileInput(attrs={'class': 'user-avatar'}))


class WorkCriteriaForm(forms.ModelForm):
    class Meta:
        model = WorkCriteria
        fields = ('position', 'salary_expectations', 'hourly_rate', 'experience', 'country', 'city',
                  'moving_to_another_city', 'category', 'work_experience',
                  'expectations', 'achievements', 'questions_to_employers')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].empty_label = ''
        self.fields['city'].empty_label = ''

    ALL_COUNTRIES = Country.objects.all()
    UKRAINE = Country.objects.get(title='Україна')
    ALL_CITIES = City.objects.all()
    KYIV = City.objects.get(title='Київ')

    position = forms.CharField(required=False, label='Посада',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary_expectations = forms.IntegerField(required=False, label='Зарплатні очікування',
                                             widget=forms.NumberInput(attrs={'class':
                                                                                 'form-control'}),
                                             min_value=0)
    hourly_rate = forms.IntegerField(required=False, label='Погодинна ставка',
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))

    experience = forms.ChoiceField(choices=settings.EXPERIENCE_CHOICE)
    country = forms.ModelChoiceField(label='Країна', queryset=ALL_COUNTRIES, initial=UKRAINE,
                                     required=False,
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    city = forms.ModelChoiceField(label='Місто', queryset=ALL_CITIES, initial=KYIV,
                                  required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    moving_to_another_city = forms.BooleanField(label='Розглядаю переїзд в інше місто')
