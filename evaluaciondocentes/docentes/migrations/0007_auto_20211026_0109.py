# Generated by Django 3.2.8 on 2021-10-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0006_profesorevaluado_instrumento_para_alumnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluador',
            name='coordinadores_primaria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluador',
            name='director_primaria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluador',
            name='equipo_de_psicologia_primaria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluador',
            name='subdirector_primaria',
            field=models.BooleanField(default=False),
        ),
    ]