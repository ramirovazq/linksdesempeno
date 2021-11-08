from django.core.management.base import BaseCommand
from evaluaciondirectivos.models import EquipoDirectivo
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey


import csv

class Command(BaseCommand):
    help = 'Create Surveys in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for equipodirectivo in EquipoDirectivo.objects.all():
            if not equipodirectivo.id_survey:
                maestro = equipodirectivo.profesor.nombre
                maestro = maestro.title()
                materia = equipodirectivo.profesor.materia
                materia = materia.title()
                idtocopy = settings.SURVEYIDEVALUACIONDIRECCION
                newsurvey_name = f"Evaluación Equipo Directivo </br> Docente: {maestro} </br> Asignatura: {materia} </br>"
                result = api.survey.copy_survey(idtocopy, newsurvey_name)
                if 'newsid' in result:
                    id_survey = result['newsid']
                    equipodirectivo.id_survey = id_survey
                    equipodirectivo.save()
                    self.stdout.write(self.style.SUCCESS(f'Success saving survey {id_survey} {equipodirectivo.nombre}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Error copiando survey, result: {result}'))                
            else:
                self.stdout.write(self.style.WARNING ('Already exists %s' % (equipodirectivo.id_survey)))

        for equipodirectivo in EquipoDirectivo.objects.all():
            if equipodirectivo.id_survey:
                result = api.survey.activate_survey(equipodirectivo.id_survey)
                self.stdout.write(self.style.WARNING('Activating result "%s"' % result))
            else:
                self.stdout.write(self.style.ERROR('Does not have survey id '))

        # Close the session.
        api.close() 