from django import forms

from .models import Code


class CodeForm(forms.ModelForm):

    number = forms.CharField(label='Введіть код: ',
                             help_text='Введіть код, який ми надіслали на ваш номер '
                                       'телефону в SMS-повідомленні',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Code
        fields = ('number', )
