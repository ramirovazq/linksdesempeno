# linksdesempeno

# enable instrumentos alumnos, y bachillerato
python manage.py read_csv_alumnos
python manage.py create_alumnos_grupos
python manage.py create_profesores_autoevaluaciones_grupos

# enable instrumentos directivos, y bachillerato
python manage.py read_csv_directivos
python manage.py create_profesores_autoevaluaciones
python manage.py create_directivos_evaluaciones

# enable instrumentos directivos kínder
python manage.py read_csv_directivos_kinder
python manage.py create_profesores_autoevaluaciones_kinder
python manage.py create_directivos_evaluaciones_kinder