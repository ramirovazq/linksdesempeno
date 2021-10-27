from django.core.management.base import BaseCommand, CommandError
from docentes.models import ProfesorEvaluado
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey


import csv

class Command(BaseCommand):
    help = 'Create Surveys in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for evaluado in ProfesorEvaluado.objects.all():
            if evaluado.id_survey_evaluado:
                result = api.survey.activate_survey(evaluado.id_survey_evaluado)
                if result:
                    self.stdout.write(self.style.SUCCESS('Successfully actived survey "%s"' % evaluado.id_survey_evaluado))
                else:
                    self.stdout.write(self.style.ERROR('Error activating survey "%s"' % evaluado.id_survey_evaluado))
            else:
                self.stdout.write(self.style.ERROR('Does not have survey id '))

        for evaluado in ProfesorEvaluado.objects.all():
            if evaluado.id_survey_evaluado:
                result = api.survey.activate_tokens(evaluado.id_survey_evaluado)
                if result:
                    self.stdout.write(self.style.SUCCESS('Successfully actived survey for tokens "%s"' % evaluado.id_survey_evaluado))
                else:
                    self.stdout.write(self.style.ERROR('Error activating survey for tokens "%s"' % evaluado.id_survey_evaluado))
            else:
                self.stdout.write(self.style.ERROR('Does not have survey id '))


        api.close() 