from django import forms

from .models import Code


class CodeForm(forms.ModelForm):

    number = forms.CharField(label='Введіть код',
                             help_text='Введіть код,який ми надіслали на ваш номер',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        models = Code
        fields = ('number', )

