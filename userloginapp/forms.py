from django import forms
from userloginapp.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    #     password = forms.CharField(widget=forms.PasswordInput)
    # #class UserForm(UserCreationForm):
    #     username = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #     'class': 'input-field',
    #     'placeholder': 'Username'
    #     }
    #     ))
    #     password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={
    #     'class': 'input-field',
    #     'placeholder': 'Choose Password'
    #     }
    #     ))
    #     email = forms.EmailField(widget=forms.EmailInput(
    #     attrs={
    #     'class': 'input-field',
    #     'placeholder': 'Email'
    #     }
    #     ))
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserProfileInfoForm(forms.ModelForm):
    profile_pic = forms.FileField(required=False)

    class Meta:
        model = UserProfileInfo
        fields = ("profile_pic",)
