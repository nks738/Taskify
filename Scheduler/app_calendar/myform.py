from django import forms


class HelloForm(forms.Form):
    Username = forms.CharField(max_length=100)
    Password = forms.PasswordInput()
