# Generated by Django 3.2.8 on 2021-11-28 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciondirectivos', '0002_auto_20211108_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipodirectivo',
            name='response_boolean_survey',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipodirectivo',
            name='response_survey',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='response_boolean_profesor_autoevaluacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profesor',
            name='response_profesor_autoevaluacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
