from django.core.management.base import BaseCommand
from evaluacionalumnosbachillerato.models import GrupoAlumnos
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey


import csv

class Command(BaseCommand):
    help = 'Create Surveys in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for group in GrupoAlumnos.objects.all():
            if not group.id_survey:
                maestro = group.profesor.nombre
                maestro = maestro.title()
                materia = group.profesor.materia
                materia = materia.title()
                #idtocopy = settings.SURVEYIDEVALUACIONALUMNOSAMAESTROS
                idtocopy = "147957"
                # newsurvey_name = f"Nombre del Maestro: {maestro} </br> Materia: {materia} </br> Grupo:{group.grupo}"
                newsurvey_name = f"Bachillerato </br> Maestro: {maestro} </br> Materia: {materia} </br> Grupo:{group.grupo}"
                result = api.survey.copy_survey(idtocopy, newsurvey_name)
                if 'newsid' in result:
                    id_survey = result['newsid']
                    group.id_survey = id_survey
                    group.save()
                    self.stdout.write(self.style.SUCCESS(f'Success saving survey {id_survey} {group.grupo}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Error copiando survey, result: {result}'))                
            #else:
                #self.stdout.write(self.style.WARNING ('Already exists %s' % (group.id_survey)))

        for group in GrupoAlumnos.objects.all():
            if group.id_survey and (not group.id_survey_profesor_autoevaluacion):
                result = api.survey.activate_survey(group.id_survey)
                self.stdout.write(self.style.WARNING('Activating result "%s"' % result))
            else:
                self.stdout.write(self.style.ERROR('Does not have survey id '))

        # Close the session.
        api.close() 