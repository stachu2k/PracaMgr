from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    """Authentication form."""
    username = forms.CharField(max_length=254, label="Nazwa użytkownika",
                               widget=forms.TextInput({
                                   'placeholder': 'Wpisz nazwę użytkownika'}))
    password = forms.CharField(label="Hasło",
                               widget=forms.PasswordInput({
                                   'placeholder':'Wpis hasło'}))


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name':'Imię',
            'surname':'Nazwisko',
        }