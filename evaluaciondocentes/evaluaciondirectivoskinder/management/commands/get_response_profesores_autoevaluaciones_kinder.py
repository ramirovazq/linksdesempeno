from django.core.management.base import BaseCommand
from evaluaciondirectivoskinder.models import Profesor
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey
from .utils import decode_msg
from collections import OrderedDict

class Command(BaseCommand):
    help = 'Create Surveys autoevaluacion Kinder in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for profesor in Profesor.objects.filter(autoevaluacion=True):
            method = "export_responses_by_token"
            params = OrderedDict([
                ("sSessionKey", api.session_key),
                ("iSurveyID", profesor.id_survey_profesor_autoevaluacion),
                ("sDocumentType", "json"),
                ("sToken", profesor.token_profesor_autoevaluacion)
            ])
            response = api.query(method=method, params=params)
            if isinstance(response, str):
                response_decode = decode_msg(response)
                self.stdout.write(self.style.SUCCESS(f"iSurveyID {profesor.id_survey_profesor_autoevaluacion} sToken {profesor.token_profesor_autoevaluacion}"))
                profesor.response_boolean_profesor_autoevaluacion = True
            else:
                response_decode = str(response)
                self.stdout.write(self.style.ERROR(f"iSurveyID {profesor.id_survey_profesor_autoevaluacion} sToken {profesor.token_profesor_autoevaluacion}"))
                profesor.response_boolean_profesor_autoevaluacion = False

            profesor.response_profesor_autoevaluacion = response_decode
            profesor.save()


        # Close the session.
        api.close() 