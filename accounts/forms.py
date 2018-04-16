import datetime
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.forms.extras.widgets import SelectDateWidget
from .models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("User Does Not Exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(UserCreationForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)
    birth_date = forms.DateField(
        widget=forms.widgets.SelectDateWidget(years=range(1940, 2010)))

    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "username",
                  "email",
                  "birth_date",
                  "bio",
                  "picture",
                  "password1",
                  "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birth_date = self.cleaned_data['birth_date']
        user.bio = self.cleaned_data['bio']
        if commit:
            user.save()
        return user


class UserProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)
    birth_date = forms.DateField(
        widget=forms.widgets.SelectDateWidget(years=range(1940, 2010)))

    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "email",
                  "bio",
                  "birth_date",
                  "picture")
