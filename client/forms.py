from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Required. Add a valid email address')

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')
