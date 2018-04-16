from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(max_length=140)
    password = forms.CharField(max_length=140)


