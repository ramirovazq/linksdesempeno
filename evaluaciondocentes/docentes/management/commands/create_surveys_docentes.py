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

        for evaluado in ProfesorEvaluado.objects.filter(instrumento_para_alumnos=False):
            if not evaluado.id_survey_evaluado:
                idtocopy = settings.SURVEYID2COPYPROFESORS
                profesor = evaluado.nombre.title()
                materia = evaluado.materia.title()
                newsurvey_name = f"Evaluación de Clase Docentes {materia} {profesor} Ciclo Escolar 2021-2022"
                result = api.survey.copy_survey(idtocopy, newsurvey_name)
                if 'newsid' in result:
                    print("ok")
                    id_survey = result['newsid']
                    evaluado.id_survey_evaluado = id_survey
                else:
                    print("bad")
                    evaluado.id_survey_evaluado = result
                evaluado.save()
                if result:
                    self.stdout.write(self.style.SUCCESS('Successfully created survey "%s"' % evaluado.id_survey_evaluado))
                else:
                    self.stdout.write(self.style.ERROR('Error creating survey'))
            else:
                self.stdout.write(self.style.WARNING ('Already exists "%s" for "%s"' % (evaluado.id_survey_evaluado, evaluado)))


        # Close the session.
        api.close() 