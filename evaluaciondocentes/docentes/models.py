from django.db import models
from django.conf import settings


class ProfesorEvaluado(models.Model):
    nombre  = models.CharField(max_length=300)
    materia = models.CharField(max_length=300)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    instrumento_para_alumnos = models.BooleanField(default=True)
    id_survey_evaluado = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"id {self.id}, nombre: {self.nombre}, materia: {self.materia}"

class Evaluador(models.Model):
    nombre_o_grupo = models.CharField(max_length=300)
    autoevaluacion = models.BooleanField(default=False)
    evaluado = models.ForeignKey(ProfesorEvaluado, on_delete=models.CASCADE)
    id_survey = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    instrumento_para_alumnos = models.BooleanField(default=True)
    director_primaria = models.BooleanField(default=False)
    subdirector_primaria = models.BooleanField(default=False)
    coordinadores_primaria = models.BooleanField(default=False)
    equipo_de_psicologia_primaria = models.BooleanField(default=False)
    token = models.CharField(max_length=300, blank=True, null=True)


    def url_survey(self):
        return settings.URL_SURVEY + self.id_survey

    def url_survey_token(self):
        return f"{settings.URL_SURVEY}{self.evaluado.id_survey_evaluado}&token={self.token}&newtest=Y"

    def __str__(self):
        return f"nombre o gpo: {self.nombre_o_grupo}, autoevaluacion: {self.autoevaluacion}, evaluado {self.evaluado}"