from django import forms


class PasswordRemindRequestForm(forms.Form):

    email = forms.EmailField(label='Введіть ваш email: ',
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

