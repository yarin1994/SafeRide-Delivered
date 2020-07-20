from django.forms import ModelForm
from .models import Scooter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ScooterForm(ModelForm):
    class Meta:
        model= Scooter
        fields= ['serial_number','brand', 'city', 'helmet', 'status', 'battery' ]

class createUserForm(UserCreationForm):
    is_staff = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2', 'is_staff']