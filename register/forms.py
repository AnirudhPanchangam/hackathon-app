from django import forms

class RegistrationForm(forms.Form):
    fname = forms.CharField(max_length=140)
    lname = forms.CharField(max_length=140)
    email = forms.EmailField()
    pwd1 = forms.CharField(widget = forms.PasswordInput())
    pwd2 = forms.CharField(widget = forms.PasswordInput())
    user_group = forms.ChoiceField(choices=(('teacher','Teacher'),('student','Student')))
    phone = forms.IntegerField()
    
 	