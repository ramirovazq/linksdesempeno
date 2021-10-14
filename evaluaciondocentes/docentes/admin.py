from django.contrib import admin


from .models import ProfesorEvaluado, Evaluador

class ProfesorEvaluadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'materia']
    list_filter = ['materia']

class EvaluadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_o_grupo', 'autoevaluacion', 'evaluado', 'id_survey', 'slug']
    list_filter = ['autoevaluacion', 'evaluado']


admin.site.register(ProfesorEvaluado, ProfesorEvaluadoAdmin)
admin.site.register(Evaluador, EvaluadorAdmin)