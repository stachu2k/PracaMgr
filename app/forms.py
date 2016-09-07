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


class SemesterForm(forms.Form):
    academic_year = forms.CharField(max_length=7)
    sem_type = forms.ChoiceField(choices=[('z','zimowy'), ('l','letni')], widget=forms.RadioSelect)
    start_date = forms.DateField(input_formats=[
        '%d.%m.%Y',       # '25.10.2006'
        ])
    end_date = forms.DateField(input_formats=[
        '%d.%m.%Y',       # '25.10.2006'
        ])


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name':'Imię',
            'surname':'Nazwisko',
        }