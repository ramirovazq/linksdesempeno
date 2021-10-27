from django.core.management.base import BaseCommand, CommandError
from docentes.models import ProfesorEvaluado, Evaluador
from django.conf import settings


import csv

class Command(BaseCommand):
    help = 'Read docentes file, for students.'
    def handle(self, *args, **options):

        base_dir_path = str(settings.BASE_DIR)
        base_dir_path = base_dir_path + '/evaluaciondocentes'

        with open(base_dir_path + '/load_init/evaluados-equipo-de-direccion.csv') as csvfile_in, open(base_dir_path + '/load_init/evaluados-equipo-de-direccion.csv') as csvfile_evaluadores:
      # with open(base_dir_path + '/load_init/evaluados-equipo-de-direccion_simple.csv') as csvfile_in, open(base_dir_path + '/load_init/evaluados-equipo-de-direccion_simple.csv') as csvfile_evaluadores:
            readCSV = csv.reader(csvfile_in, delimiter=';')
            readCSVevaluadores = csv.reader(csvfile_evaluadores, delimiter=';')

            # autoevaluacion 4 
            # evaluador 5 -> 29 
            not_used_rows = [0, 1, 2, 3, 4, 5, 6]
            columnas_evaluador = list(range(5,18))
            cols_coordinador = list(range(7,15))
            cols_equipo_de_psicologia = list(range(15,19))
            rows_for_evaluadores = list(readCSVevaluadores)
            evaluadores_line = rows_for_evaluadores[6]

            for indice, row in enumerate(readCSV):
                if indice not in not_used_rows: # quit headers
                    nombre_profesor_evaluado =  row[1]
                    materia =  row[3]
                    autoevaluacion =  row[4]
                    director =  row[5]
                    subdirector =  row[6]
                    # cols_coordinador
                    # cols_equipo_de_psicologia

                    # Profesor Evaluado
                    obj_profesor_evaluado, created = ProfesorEvaluado.objects.get_or_create(
                        nombre=nombre_profesor_evaluado,
                        materia=materia,
                        instrumento_para_alumnos=False
                    )                    
                    if created:
                        self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_profesor_evaluado))
                    else:
                        self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_profesor_evaluado))

                    # AutoEvaluacion
                    if autoevaluacion.lower() == "x":
                        obj_autoevaluacion, created = Evaluador.objects.get_or_create(
                            nombre_o_grupo = obj_profesor_evaluado.nombre,
                            autoevaluacion=True,
                            evaluado=obj_profesor_evaluado,
                            instrumento_para_alumnos=False
                        )
                        if created:
                            self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_autoevaluacion))
                        else:
                            self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_autoevaluacion))


                    # director
                    if director.lower() == "x":
                        el_director = evaluadores_line[5]
                        el_director = " ".join(el_director.strip().split())
                        obj_autoevaluacion, created = Evaluador.objects.get_or_create(
                            nombre_o_grupo = el_director,
                            director_primaria=True,
                            evaluado=obj_profesor_evaluado,
                            instrumento_para_alumnos=False
                        )
                        if created:
                            self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_autoevaluacion))
                        else:
                            self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_autoevaluacion))

                    # subdirector
                    if subdirector.lower() == "x":
                        el_subdirector = evaluadores_line[6]
                        el_subdirector = " ".join(el_subdirector.strip().split())
                        obj_autoevaluacion, created = Evaluador.objects.get_or_create(
                            nombre_o_grupo = el_subdirector,
                            subdirector_primaria=True,
                            evaluado=obj_profesor_evaluado,
                            instrumento_para_alumnos=False
                        )
                        if created:
                            self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_autoevaluacion))
                        else:
                            self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_autoevaluacion))


                    for column in cols_coordinador:
                        col = row[column].lower()
                        if col == "x":
                            el_evaluador = evaluadores_line[column]
                            el_evaluador = " ".join(el_evaluador.strip().split())
                            obj_autoevaluacion, created = Evaluador.objects.get_or_create(
                                nombre_o_grupo = el_evaluador,
                                evaluado=obj_profesor_evaluado,
                                instrumento_para_alumnos=False,
                                coordinadores_primaria=True
                            )
                            if created:
                                self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_autoevaluacion))
                            else:
                                self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_autoevaluacion))


                    for column in cols_equipo_de_psicologia:
                        #print(column)
                        col = row[column].lower()
                        if col == "x":
                            el_equipo_psico = evaluadores_line[column]
                            el_equipo_psico = " ".join(el_equipo_psico.strip().split())
                            obj_autoevaluacion, created = Evaluador.objects.get_or_create(
                                nombre_o_grupo = el_equipo_psico,
                                evaluado=obj_profesor_evaluado,
                                instrumento_para_alumnos=False,
                                equipo_de_psicologia_primaria=True
                            )
                            if created:
                                self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_autoevaluacion))
                            else:
                                self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_autoevaluacion))

