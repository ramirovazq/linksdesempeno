from django.contrib import admin


from .models import ProfesorEvaluado, Evaluador

class ProfesorEvaluadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'materia', 'instrumento_para_alumnos']
    list_filter = ['materia', 'instrumento_para_alumnos']

class EvaluadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_o_grupo', 'autoevaluacion', 'evaluado', 'id_survey', 'instrumento_para_alumnos', 'director_primaria', 'subdirector_primaria','coordinadores_primaria','equipo_de_psicologia_primaria']
    list_filter = ['autoevaluacion', 'evaluado', 'instrumento_para_alumnos', 'director_primaria', 'subdirector_primaria','coordinadores_primaria','equipo_de_psicologia_primaria']


admin.site.register(ProfesorEvaluado, ProfesorEvaluadoAdmin)
admin.site.register(Evaluador, EvaluadorAdmin)