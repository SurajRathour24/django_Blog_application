from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email']


class EditProfile(UserChangeForm):
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']