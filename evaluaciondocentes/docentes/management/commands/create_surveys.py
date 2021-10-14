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

        for evaluador in Evaluador.objects.all():
            if not evaluador.id_survey:
                grupo = evaluador.nombre_o_grupo
                maestro = evaluador.evaluado.nombre
                idtocopy = settings.SURVEYID2COPY
                newsurvey_name = f"EVALUACIÓN DESEMPEÑO DOCENTE CICLO ESCOLAR 2021-2022 {maestro}, {grupo}"
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