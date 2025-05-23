from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
