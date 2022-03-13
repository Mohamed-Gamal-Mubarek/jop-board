# TO VIEW FORM IN TEMPLATE DON'T FORGET TO CHECK IT AND FOCUS THE FORM YOU CREATED IN TEMPLATE IT COMES FROM DJANGO ADMIN
# https://github.com/zostera/django-bootstrap4
# from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'phone_number', 'img']