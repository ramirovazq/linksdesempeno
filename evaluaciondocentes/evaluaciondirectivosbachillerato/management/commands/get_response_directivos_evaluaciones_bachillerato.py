from django.core.management.base import BaseCommand
from evaluaciondirectivosbachillerato.models import EquipoDirectivo
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey
from collections import OrderedDict
from .utils import decode_msg


class Command(BaseCommand):
    help = 'Get response Surveys in Lime for open survey.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for equipodirectivo in EquipoDirectivo.objects.all():
            method = "export_responses"
            params = OrderedDict([
                ("sSessionKey", api.session_key),
                ("iSurveyID", equipodirectivo.id_survey),
                ("sDocumentType", "json"),
            ])
            response = api.query(method=method, params=params)
            if isinstance(response, str):
                response_decode = decode_msg(response)
                self.stdout.write(self.style.SUCCESS(f"iSurveyID {equipodirectivo.id_survey} sToken: public, no token"))
                equipodirectivo.response_boolean_survey = True
            else:
                response_decode = str(response)
                self.stdout.write(self.style.ERROR(f"iSurveyID {equipodirectivo.id_survey} sin token"))
                equipodirectivo.response_boolean_survey = False

            equipodirectivo.response_survey = response_decode
            equipodirectivo.save()

        # Close the session.
        api.close() 