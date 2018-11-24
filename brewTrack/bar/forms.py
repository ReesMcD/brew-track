from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'uk-input text-input',
            'placeholder' : 'username',
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'uk-input text-input',
            'placeholder' : 'email',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'uk-input text-input',
            'placeholder' : 'password',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]

class LoginForm(forms.Form ):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'uk-input text-input',
            'placeholder' : 'username',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'uk-input text-input',
            'placeholder' : 'password',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'password', ]
