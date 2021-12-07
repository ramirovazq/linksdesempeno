from django.db import models
from django.conf import settings


class Profesor(models.Model):
    nombre  = models.CharField(max_length=300)
    materia = models.CharField(max_length=300)
    autoevaluacion = models.BooleanField(default=False)
    id_survey_profesor_autoevaluacion = models.CharField(max_length=300, blank=True)
    token_profesor_autoevaluacion = models.CharField(max_length=300, blank=True)
    response_boolean_profesor_autoevaluacion = models.BooleanField(default=False)
    response_profesor_autoevaluacion = models.TextField(blank=True, null=True)
    survey_closed = models.BooleanField(default=False)


    def __str__(self):
        return f"""id {self.id}, 
                nombre: {self.nombre}, 
                materia: {self.materia},  
                autoevaluacion: {self.autoevaluacion}"""

    def url_survey_token(self):
        return f"{settings.URL_SURVEY}{self.id_survey_profesor_autoevaluacion}&token={self.token_profesor_autoevaluacion}&newtest=Y"


class EquipoDirectivo(models.Model):
    nombre = models.CharField(max_length=300)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_survey = models.CharField(max_length=300, blank=True)
    response_survey = models.TextField(blank=True, null=True)
    response_boolean_survey = models.BooleanField(default=False)
    survey_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"nombre: {self.nombre}, profesor {self.profesor}"

    def url_survey(self):
        return settings.URL_SURVEY + self.id_survey

