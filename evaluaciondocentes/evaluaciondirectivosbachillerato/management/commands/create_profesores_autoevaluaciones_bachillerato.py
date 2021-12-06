from django.core.management.base import BaseCommand
from evaluaciondirectivosbachillerato.models import Profesor
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey
import time

import csv

class Command(BaseCommand):
    help = 'Create Surveys autoevaluacion in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for profesor in Profesor.objects.filter(autoevaluacion=True):
            if not profesor.id_survey_profesor_autoevaluacion and not profesor.id_survey_profesor_autoevaluacion:
                maestro = profesor.nombre
                maestro = maestro.title()
                materia = profesor.materia
                materia = materia.title()
                idtocopy = settings.SURVEYIDAUTOEVALUACIONDIRECCION
                newsurvey_name = f"Autoevaluación Docentes Bachillerato </br> Docente: {maestro} </br> Asignatura: {materia} </br>"
                result = api.survey.copy_survey(idtocopy, newsurvey_name)
                if 'newsid' in result:
                    id_survey = result['newsid']
                    profesor.id_survey_profesor_autoevaluacion = id_survey
                    profesor.save()
                    self.stdout.write(self.style.SUCCESS(f'Success saving survey {id_survey} {profesor}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Error copiando survey, result: {result}'))                
            #else:
             #   self.stdout.write(self.style.WARNING ('Already exists %s' % (profesor.id_survey_profesor_autoevaluacion)))

        time.sleep(2)
        #activate token survey
        for profesor in Profesor.objects.filter(autoevaluacion=True):
            if profesor.id_survey_profesor_autoevaluacion and not profesor.token_profesor_autoevaluacion:
                result = api.survey.activate_survey(profesor.id_survey_profesor_autoevaluacion)
                self.stdout.write(self.style.WARNING('Activate survey "%s"' % result))
            #else:
             #   self.stdout.write(self.style.ERROR('Does not have survey id '))

        time.sleep(2)
        #activate token survey
        for profesor in Profesor.objects.filter(autoevaluacion=True):
            if profesor.id_survey_profesor_autoevaluacion and not profesor.token_profesor_autoevaluacion:
                result = api.survey.activate_tokens(profesor.id_survey_profesor_autoevaluacion)
                self.stdout.write(self.style.WARNING('Activating restricted surkey with tokens: "%s"' % result))
            #else:
             #   self.stdout.write(self.style.ERROR('Does not have survey id '))

        time.sleep(4)
        #create tokens
        profesores = Profesor.objects.filter(autoevaluacion=True)
        for profesor in profesores and not profesor.token_profesor_autoevaluacion:
            participant_data = []

            email = f"{profesor.id}@example.com"
            firstname = f"{profesor.nombre}"
            lastname = f"autoevaluacion"
            dicc_data = {"email":email,"lastname":lastname,"firstname":firstname}
            participant_data.append(dicc_data)
            result_token = api.token.add_participants(profesor.id_survey_profesor_autoevaluacion, participant_data)

            self.stdout.write(self.style.SUCCESS(f'se grega token de idsurvey {profesor.id_survey_profesor_autoevaluacion}'))

            response_type = type(result_token)
            if response_type is list:
                for element_dict in result_token:
                    if 'email' in element_dict.keys():
                        compuesto_email = element_dict['email']
                        token = element_dict['token']
                        list_id_ = compuesto_email.split("@")
                        profesor_id = list_id_[0]
                        profesor_update = Profesor.objects.get(id=profesor_id)
                        profesor_update.token_profesor_autoevaluacion = token
                        profesor_update.save()
                        self.stdout.write(self.style.SUCCESS('se actualiza el token de autoevaluacion'))
            if response_type is dict:
                self.stdout.write(self.style.ERROR('error: "%s"' % result_token))


        # Close the session.
        api.close() 