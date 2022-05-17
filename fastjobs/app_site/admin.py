from django.contrib import admin
from .models import Vacancies, User, Candidato, Tecnologia
from django.contrib.admin import ModelAdmin

# Register your models here.


class VacanciesAdmin(ModelAdmin):
    model = Vacancies


class UserAdmin(ModelAdmin):
    model = User

class CandidatoAdmin(ModelAdmin):
    model = Candidato

class TecnologiaAdmin(ModelAdmin):
    model = Tecnologia
    
admin.site.register(Vacancies, VacanciesAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
