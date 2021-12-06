from django.core.management.base import BaseCommand
from evaluaciondirectivosbachillerato.models import Profesor, EquipoDirectivo
from django.conf import settings


import csv

class Command(BaseCommand):
    help = 'Read csv directivos file.'
    def handle(self, *args, **options):

        base_dir_path = str(settings.BASE_DIR)
        base_dir_path = base_dir_path + '/evaluaciondocentes'

        with open(base_dir_path + '/load_init/evaluados-equipo-de-direccion-bachillerato.csv') as csvfile_in, open(base_dir_path + '/load_init/evaluados-equipo-de-direccion-bachillerato.csv') as csvfile_evaluadores:
        # with open(base_dir_path + '/load_init/evaluados-equipo-de-direccion-bachillerato_simple.csv') as csvfile_in, open(base_dir_path + '/load_init/evaluados-equipo-de-direccion-bachillerato_simple.csv') as csvfile_evaluadores:
            readCSV = csv.reader(csvfile_in, delimiter=';')
            readCSVevaluadores = csv.reader(csvfile_evaluadores, delimiter=';')

            # autoevaluacion 4 
            # evaluador 5 -> 29 
            not_used_rows = [0, 1, 2, 3, 4, 5, 6]
            columnas_evaluador = list(range(5,6))
            rows_for_evaluadores = list(readCSVevaluadores)
            evaluadores_line = rows_for_evaluadores[6]

            for indice, row in enumerate(readCSV):
                if indice not in not_used_rows: # quit headers
                    nombre_profesor_evaluado =  row[1]
                    materia =  row[3]
                    autoevaluacion =  row[4]

                    # Profesor
                    if autoevaluacion.lower() == "x":
                        obj_profesor_evaluado, created = Profesor.objects.get_or_create(
                            nombre=nombre_profesor_evaluado,
                            materia=materia,
                            autoevaluacion=True
                        )                 
                    else:   
                        obj_profesor_evaluado, created = Profesor.objects.get_or_create(
                            nombre=nombre_profesor_evaluado,
                            materia=materia,
                            autoevaluacion=False
                        )                 
                    if created:
                        self.stdout.write(self.style.SUCCESS('Successfully created "%s"' % obj_profesor_evaluado))
                    else:
                        self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_profesor_evaluado))


                    # EquipoDirectivo
                    for column in columnas_evaluador:
                        col = row[column].lower()
                        if col == "x":
                            obj_gpo, created = EquipoDirectivo.objects.get_or_create(
                                nombre = evaluadores_line[column],
                                profesor=obj_profesor_evaluado,
                            )
                            if created:
                                self.stdout.write(self.style.SUCCESS('Successfully created Grupo "%s"' % obj_gpo))
                            else:
                                self.stdout.write(self.style.WARNING ('Already exists "%s"' % obj_gpo))

