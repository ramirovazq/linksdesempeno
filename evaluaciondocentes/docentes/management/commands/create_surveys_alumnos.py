from django.core.management.base import BaseCommand, CommandError
from docentes.models import ProfesorEvaluado, Evaluador
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey


import csv

class Command(BaseCommand):
    help = 'Create Surveys in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for evaluador in Evaluador.objects.filter(instrumento_para_alumnos=True):
            if not evaluador.id_survey:
                grupo = evaluador.nombre_o_grupo
                maestro = evaluador.evaluado.nombre
                maestro = maestro.title()
                materia = evaluador.evaluado.materia
                materia = materia.title()
                idtocopy = settings.SURVEYID2COPYSTUDENTS
                newsurvey_name = f" Evaluación de Clase Alumnos {materia} {maestro} Grupo {grupo} Ciclo escolar 2021-2022"
                result = api.survey.copy_survey(idtocopy, newsurvey_name)
                evaluador.id_survey = result
                evaluador.save()
                if result:
                    self.stdout.write(self.style.SUCCESS('Successfully created survey "%s"' % evaluador.id_survey))
                else:
                    self.stdout.write(self.style.ERROR('Error creating survey'))
            else:
                self.stdout.write(self.style.WARNING ('Already exists "%s" for "%s"' % (evaluador.id_survey, evaluador)))
        # Close the session.
        api.close() 