# Generated by Django 3.2.8 on 2021-11-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacionalumnosbachillerato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupoalumnos',
            name='qr_survey',
            field=models.ImageField(default=True, null=True, upload_to='qrs/'),
        ),
    ]
