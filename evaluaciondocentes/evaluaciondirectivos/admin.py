from django.contrib import admin
from .models import Profesor, EquipoDirectivo

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'materia', 'autoevaluacion', 'id_survey_profesor_autoevaluacion', 'token_profesor_autoevaluacion']
    list_filter = ['materia', 'autoevaluacion']


class EquipoDirectivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'profesor', 'id_survey']
    #list_filter = ['grupo']


admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(EquipoDirectivo, EquipoDirectivoAdmin)