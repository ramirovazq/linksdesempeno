# Generated by Django 3.2.8 on 2021-10-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacionalumnos', '0002_grupoalumnos_id_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupoalumnos',
            name='id_survey_profesor_autoevaluacion',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='grupoalumnos',
            name='token_profesor_autoevaluacion',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]