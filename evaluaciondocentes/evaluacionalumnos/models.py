from django.db import models
from django.conf import settings


class Profesor(models.Model):
    nombre  = models.CharField(max_length=300)
    materia = models.CharField(max_length=300)
    autoevaluacion = models.BooleanField(default=False)

    def __str__(self):
        return f"""id {self.id}, 
                nombre: {self.nombre}, 
                materia: {self.materia},  
                autoevaluacion: {self.autoevaluacion}"""
    def got_autoevaluciones(self):
        return len(GrupoAlumnos.objects.filter(
                profesor__nombre=self.nombre,
                profesor__autoevaluacion=True
                )) > 0


class GrupoAlumnos(models.Model):
    grupo = models.CharField(max_length=300)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_survey = models.CharField(max_length=300, blank=True)
    id_survey_profesor_autoevaluacion = models.CharField(max_length=300, blank=True)
    token_profesor_autoevaluacion = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"gpo: {self.grupo}, profesor {self.profesor}"

    def url_survey(self):
        return settings.URL_SURVEY + self.id_survey

    def url_survey_token(self):
        return f"{settings.URL_SURVEY}{self.id_survey_profesor_autoevaluacion}&token={self.token_profesor_autoevaluacion}&newtest=Y"
