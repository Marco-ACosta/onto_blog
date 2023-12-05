
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255, label="Email")
    password = forms.CharField(required=True, max_length=255, widget=forms.PasswordInput, label="Senha")

class SingUpForm(forms.Form):
    name = forms.CharField(required=True, max_length=255, label="Nome")
    email = forms.EmailField(required=True, max_length=255, label="Email")
    password = forms.CharField(required=True, max_length=255, widget=forms.PasswordInput, label="Senha")

