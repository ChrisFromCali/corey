from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #Configurations for this custom form
        model = User
        fields = ['username', 'email', 'password1', 'password2']