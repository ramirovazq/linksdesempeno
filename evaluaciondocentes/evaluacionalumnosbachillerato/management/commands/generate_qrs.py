from django.core.management.base import BaseCommand
from evaluacionalumnosbachillerato.models import GrupoAlumnos
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey
import qrcode
from django.conf import settings

import csv

class Command(BaseCommand):
    help = 'Create Surveys in Lime.'

    def handle(self, *args, **options):

        for group in GrupoAlumnos.objects.all():
            url = group.url_survey()
            qr = qrcode.make(url)
            ruta_creacion = f"{settings.MEDIA_ROOT}qrs/{group.id}_qr.png"
            ruta_creacion_url = f"qrs/{group.id}_qr.png"
            qr_image = qr.save(ruta_creacion)
            group.qr_survey = ruta_creacion_url
            group.save()
            self.stdout.write(self.style.SUCCESS(f'QR generado {group.id} en {ruta_creacion_url}'))
