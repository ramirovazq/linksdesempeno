# Generated by Django 3.2.8 on 2021-10-26 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0010_evaluador_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluador',
            name='token_created',
        ),
    ]
