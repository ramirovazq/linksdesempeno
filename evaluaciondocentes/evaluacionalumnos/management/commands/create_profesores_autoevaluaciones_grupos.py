from django.core.management.base import BaseCommand
from evaluacionalumnos.models import GrupoAlumnos, Profesor
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey
import time

import csv

class Command(BaseCommand):
    help = 'Create Surveys in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for group in GrupoAlumnos.objects.all():
            if not group.id_survey_profesor_autoevaluacion:
                maestro = group.profesor.nombre
                maestro = maestro.title()
                materia = group.profesor.materia
                materia = materia.title()
                idtocopy = settings.SURVEYIDAUTOEVALUACIONDEGRUPOS
                newsurvey_name = f"Autoevaluación </br> Nombre del Maestro: {maestro} </br> Materia: {materia} </br> Grupo:{group.grupo}"
                result = api.survey.copy_survey(idtocopy, newsurvey_name)
                if 'newsid' in result:
                    id_survey = result['newsid']
                    group.id_survey_profesor_autoevaluacion = id_survey
                    group.save()
                    self.stdout.write(self.style.SUCCESS(f'Success saving survey {id_survey} {group.grupo}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Error copiando survey, result: {result}'))                
            else:
                self.stdout.write(self.style.WARNING ('Already exists %s' % (group.id_survey)))

        time.sleep(2)
        #activate token survey
        for group in GrupoAlumnos.objects.all():
            if group.id_survey_profesor_autoevaluacion:
                result = api.survey.activate_survey(group.id_survey_profesor_autoevaluacion)
                self.stdout.write(self.style.WARNING('Activate survey "%s"' % result))
            else:
                self.stdout.write(self.style.ERROR('Does not have survey id '))

        time.sleep(2)
        #activate token survey
        for group in GrupoAlumnos.objects.all():
            if group.id_survey_profesor_autoevaluacion:
                result = api.survey.activate_tokens(group.id_survey_profesor_autoevaluacion)
                self.stdout.write(self.style.WARNING('Activating restricted surkey with tokens: "%s"' % result))
            else:
                self.stdout.write(self.style.ERROR('Does not have survey id '))

        time.sleep(4)
        #create tokens
        grupos = GrupoAlumnos.objects.filter(profesor__autoevaluacion=True)
        for grupo in grupos:
            participant_data = []

            email = f"{grupo.id}@example.com"
            firstname = f"{grupo.profesor.nombre}"
            lastname = f"autoevaluacion"
            dicc_data = {"email":email,"lastname":lastname,"firstname":firstname}
            participant_data.append(dicc_data)
            result_token = api.token.add_participants(grupo.id_survey_profesor_autoevaluacion, participant_data)

            self.stdout.write(self.style.SUCCESS(f'se grega token de idsurvey {grupo.id_survey_profesor_autoevaluacion}'))

            response_type = type(result_token)
            if response_type is list:
                for element_dict in result_token:
                    if 'email' in element_dict.keys():
                        compuesto_email = element_dict['email']
                        token = element_dict['token']
                        list_id_ = compuesto_email.split("@")
                        group_id = list_id_[0]
                        group_update = GrupoAlumnos.objects.get(id=group_id)
                        group_update.token_profesor_autoevaluacion = token
                        group_update.save()
                        self.stdout.write(self.style.SUCCESS('se actualiza el token de autoevaluacion'))
            if response_type is dict:
                self.stdout.write(self.style.ERROR('error: "%s"' % result_token))


        # Close the session.
        api.close() 