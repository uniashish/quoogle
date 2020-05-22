from django import forms
from userloginapp.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
#class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
    attrs={
    'class': 'form-control',
    'placeholder': 'Choose A Username'
    }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
    attrs={
    'class': 'form-control',
    'placeholder': 'Choose Password'
    }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
    attrs={
    'class': 'form-control',
    'placeholder': 'Your Email Here'
    }
    ))
    class Meta():
        model = User
        fields = ('username','email','password',)

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic',)
