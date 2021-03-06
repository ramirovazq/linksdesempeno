# Generated by Django 3.2.8 on 2021-11-29 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('materia', models.CharField(max_length=300)),
                ('autoevaluacion', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoAlumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=300)),
                ('id_survey', models.CharField(blank=True, max_length=300)),
                ('response_survey', models.TextField(blank=True, null=True)),
                ('response_boolean_survey', models.BooleanField(default=False)),
                ('id_survey_profesor_autoevaluacion', models.CharField(blank=True, max_length=300)),
                ('token_profesor_autoevaluacion', models.CharField(blank=True, max_length=300)),
                ('response_boolean_profesor_autoevaluacion', models.BooleanField(default=False)),
                ('response_profesor_autoevaluacion', models.TextField(blank=True, null=True)),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacionalumnosbachillerato.profesor')),
            ],
        ),
    ]
