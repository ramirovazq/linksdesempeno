# Generated by Django 3.2.8 on 2021-10-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0005_evaluador_instrumento_para_alumnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesorevaluado',
            name='instrumento_para_alumnos',
            field=models.BooleanField(default=True),
        ),
    ]
