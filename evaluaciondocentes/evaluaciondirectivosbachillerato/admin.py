from django.contrib import admin
from .models import Profesor, EquipoDirectivo

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'materia', 'autoevaluacion', 'id_survey_profesor_autoevaluacion', 'token_profesor_autoevaluacion', 'response_boolean_profesor_autoevaluacion','response_profesor_autoevaluacion']
    list_filter = ['response_boolean_profesor_autoevaluacion','autoevaluacion','materia']


class EquipoDirectivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'profesor', 'id_survey', 'response_boolean_survey', 'response_survey']
    list_filter = ['response_boolean_survey']


admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(EquipoDirectivo, EquipoDirectivoAdmin)