from django.core.management.base import BaseCommand, CommandError
from docentes.models import ProfesorEvaluado, Evaluador
from django.conf import settings


import csv

class Command(BaseCommand):
    help = 'Read docentes file.'
    def handle(self, *args, **options):

        base_dir_path = str(settings.BASE_DIR)
        base_dir_path = base_dir_path + '/evaluaciondocentes'

        with open(base_dir_path + '/load_init/evaluados-alumnos.csv') as csvfile_in, open(base_dir_path + '/load_init/evaluados-alumnos_simple.csv') as csvfile_evaluadores:
            readCSV = csv.reader(csvfile_in, delimiter=';')
            readCSVevaluadores = csv.reader(csvfile_evaluadores, delimiter=';')

            # autoevaluacion 4 
            # evaluador 5 -> 29 
            not_used_rows = [0, 1, 2, 3, 4, 5]
            columnas_evaluador = list(range(5,30))
            rows_for_evaluadores = list(readCSVevaluadores)
            evaluadores_line = rows_for_evaluadores[5]

            for indice, row in enumerate(readCSV):
                if indice not in not_used_rows: # quit headers
                    nombre_profesor_evaluado =  row[1]
                    materia =  row[3]

                    # Profesor Evaluado
                    obj_profesor_evaluado, created = ProfesorEvaluado.objects.get_or_create(
                        nombre=nombre_profesor_evaluado,
                        materia=materia,
                    )                    
                    if created:
                        self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_profesor_evaluado))
                    else:
                        self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_profesor_evaluado))

                    # AutoEvaluacion
                    autoevaluacion =  row[4]
                    if autoevaluacion.lower() == "x":
                        obj_autoevaluacion, created = Evaluador.objects.get_or_create(
                            nombre_o_grupo = obj_profesor_evaluado.nombre,
                            autoevaluacion=True,
                            evaluado=obj_profesor_evaluado
                        )
                        if created:
                            self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_autoevaluacion))
                        else:
                            self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_autoevaluacion))

                    # Evaluadores
                    autoevaluacion =  row[4]
                    for column in columnas_evaluador:
                        col = row[column].lower()
                        if col == "x":
                            obj_autoevaluacion, created = Evaluador.objects.get_or_create(
                                nombre_o_grupo = evaluadores_line[column],
                                evaluado=obj_profesor_evaluado
                            )
                            if created:
                                self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_autoevaluacion))
                            else:
                                self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_autoevaluacion))
