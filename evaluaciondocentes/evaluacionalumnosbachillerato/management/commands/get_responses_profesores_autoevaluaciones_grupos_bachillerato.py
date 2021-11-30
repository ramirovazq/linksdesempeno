from django.core.management.base import BaseCommand
from evaluacionalumnosbachillerato.models import GrupoAlumnos, Profesor
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey
from collections import OrderedDict
import time
import csv
import base64

class Command(BaseCommand):
    help = 'Get responses from Surveys with tokens.'

    def handle(self, *args, **options):

        def decode_msg(msg_in_64):
            base64_message = msg_in_64
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            return message

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for group in GrupoAlumnos.objects.all():
            method = "export_responses_by_token"
            params = OrderedDict([
                ("sSessionKey", api.session_key),
                ("iSurveyID", group.id_survey_profesor_autoevaluacion),
                ("sDocumentType", "json"),
                ("sToken", group.token_profesor_autoevaluacion)
            ])
            response = api.query(method=method, params=params)
            if isinstance(response, str):
                response_decode = decode_msg(response)
                self.stdout.write(self.style.SUCCESS(f"iSurveyID {group.id_survey_profesor_autoevaluacion} sToken {group.token_profesor_autoevaluacion}"))
                group.response_boolean_profesor_autoevaluacion = True
            else:
                response_decode = str(response)
                self.stdout.write(self.style.ERROR(f"iSurveyID {group.id_survey_profesor_autoevaluacion} sToken {group.token_profesor_autoevaluacion}"))
                group.response_boolean_profesor_autoevaluacion = False

            group.response_profesor_autoevaluacion = response_decode
            group.save()


        # Close the session.
        api.close() 