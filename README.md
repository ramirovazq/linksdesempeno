# linksdesempeno

# enable instrumento docentes
python manage.py read_evaluados_profesores
python manage.py create_surveys_docentes
python manage.py activate_surveys_profesores
python manage.py create_surveys_docentes_participants

# enable instrumentos alumnos
python manage.py read_csv_alumnos
python manage.py create_alumnos_grupos
python manage.py create_profesores_autoevaluaciones_grupos