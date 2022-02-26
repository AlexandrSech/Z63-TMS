from django import forms
from .models import MyUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["login", "password", "email"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["login", "password"]
