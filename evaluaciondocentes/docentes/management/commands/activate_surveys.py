from django.core.management.base import BaseCommand, CommandError
from docentes.models import Evaluador
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey


import csv

class Command(BaseCommand):
    help = 'Create Surveys in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for evaluador in Evaluador.objects.all():
            if evaluador.id_survey:
                result = api.survey.activate_survey(evaluador.id_survey)
                if result:
                    self.stdout.write(self.style.SUCCESS('Successfully actived survey "%s"' % evaluador.id_survey))
                else:
                    self.stdout.write(self.style.ERROR('Error activating survey "%s"' % evaluador.id_survey))
            else:
                self.stdout.write(self.style.ERROR('Does not have survey id '))
        api.close() 