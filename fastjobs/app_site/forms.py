from .models import Vacancies, User, Candidato
from django.forms import ModelForm
from django import forms



class UserForm(ModelForm):
    class Meta:
        model = User
        widget = {
            'password': forms.PasswordInput()
        }

class VacanciesForm(ModelForm):
    class Meta:
        model = Vacancies

class CandidatoForm(ModelForm):
    class Meta:
        model = Candidato