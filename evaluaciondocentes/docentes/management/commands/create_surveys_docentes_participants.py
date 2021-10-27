from django.core.management.base import BaseCommand, CommandError
from docentes.models import ProfesorEvaluado, Evaluador
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey

import json
import re


class Command(BaseCommand):
    help = 'Create Surveys in Lime.'

    def handle(self, *args, **options):

        api = LimeSurvey(url=settings.URL_API, username=settings.USERNAME_API)
        api.open(password=settings.PASSWORD_API)

        for evaluado in ProfesorEvaluado.objects.filter(instrumento_para_alumnos=False):
            if evaluado.id_survey_evaluado:

                participant_data = []
                for evaluador in Evaluador.objects.filter(instrumento_para_alumnos=False, evaluado=evaluado):

                    if evaluador.autoevaluacion == True:
                        email = f"{evaluador.id}@example.com"
                        firstname = f"{evaluador.nombre_o_grupo}"
                        lastname = f"autoevaluacion"
                        dicc_data = {"email":email,"lastname":lastname,"firstname":firstname}
                        participant_data.append(dicc_data)

                    if evaluador.director_primaria == True:
                        email = f"{evaluador.id}@example.com"
                        firstname = f"{evaluador.nombre_o_grupo}"
                        lastname = f"director-primaria"
                        dicc_data = {"email":email,"lastname":lastname,"firstname":firstname}
                        participant_data.append(dicc_data)

                    if evaluador.subdirector_primaria == True:
                        email = f"{evaluador.id}@example.com"
                        firstname = f"{evaluador.nombre_o_grupo}"
                        lastname = f"subdirector-primaria"
                        dicc_data = {"email":email,"lastname":lastname,"firstname":firstname}
                        participant_data.append(dicc_data)

                    if evaluador.coordinadores_primaria == True:
                        email = f"{evaluador.id}@example.com"
                        firstname = f"{evaluador.nombre_o_grupo}"
                        lastname = f"coordinador-primaria"
                        dicc_data = {"email":email,"lastname":lastname,"firstname":firstname}
                        participant_data.append(dicc_data)

                    if evaluador.equipo_de_psicologia_primaria == True:
                        email = f"{evaluador.id}@example.com"
                        firstname = f"{evaluador.nombre_o_grupo}"
                        lastname = f"equipo-de-psicologia-primaria"
                        dicc_data = {"email":email,"lastname":lastname,"firstname":firstname}
                        participant_data.append(dicc_data)

                self.stdout.write(self.style.SUCCESS('Evaluador "%s"' % evaluador))
                
                result2 = api.token.add_participants(evaluado.id_survey_evaluado, participant_data)
                # self.stdout.write(self.style.WARNING('Result "%s"' % result2))

                response_type = type(result2)
                if response_type is list:
                    for element_dict in result2:
                        if 'email' in element_dict.keys():
                            compuesto_email = element_dict['email']
                            token = element_dict['token']
                            list_id_ = compuesto_email.split("@")
                            evaluador_id = list_id_[0]
                            evaluador_update = Evaluador.objects.get(id=evaluador_id)
                            evaluador_update.token = token
                            evaluador_update.save()
                            self.stdout.write(self.style.SUCCESS('se actualiza el token'))
                if response_type is dict:
                    self.stdout.write(self.style.ERROR('error: "%s"' % result2))


            else:
                self.stdout.write(self.style.ERROR('Necessary to have a limesurve object'))


        # Close the session.
        api.close() 