from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import Usuario

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2']

class CustomUserAuthenticationForm(AuthenticationForm):
    pass
