from django.db import models


class ProfesorEvaluado(models.Model):
    nombre  = models.CharField(max_length=300)
    materia = models.CharField(max_length=300)

    def __str__(self):
        return f"id {self.id}, nombre: {self.nombre}, materia: {self.materia}"

class Evaluador(models.Model):
    nombre_o_grupo = models.CharField(max_length=300)
    autoevaluacion = models.BooleanField(default=False)
    evaluado = models.ForeignKey(ProfesorEvaluado, on_delete=models.CASCADE)
    id_survey = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"nombre o gpo: {self.nombre_o_grupo}, autoevaluacion: {self.autoevaluacion}, evaluado {self.evaluado}"