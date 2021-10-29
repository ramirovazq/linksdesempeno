from django.contrib import admin
from .models import Profesor, GrupoAlumnos

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'materia', 'autoevaluacion']
    list_filter = ['materia', 'autoevaluacion']


class GrupoAlumnosAdmin(admin.ModelAdmin):
    list_display = ['id', 'grupo', 'profesor', 'id_survey', 'id_survey_profesor_autoevaluacion', 'token_profesor_autoevaluacion']
    list_filter = ['grupo']


admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(GrupoAlumnos, GrupoAlumnosAdmin)