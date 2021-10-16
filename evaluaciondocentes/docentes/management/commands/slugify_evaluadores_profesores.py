from django.core.management.base import BaseCommand
from docentes.models import Evaluador, ProfesorEvaluado
from django.utils.text import slugify



import csv

class Command(BaseCommand):
    help = 'Slugify evaluadores and profesores.'

    def handle(self, *args, **options):
        for evaluador in Evaluador.objects.all():
            if not evaluador.slug:
                slug = slugify(evaluador.nombre_o_grupo)
                evaluador.slug = slug
                evaluador.save()
                self.stdout.write(self.style.SUCCESS('Successfully slugified "%s"' % evaluador.slug))
            else:
                self.stdout.write(self.style.WARNING('Is already slugyfied "%s" "%s"' % (evaluador.nombre_o_grupo, evaluador.slug)))


        for profesor in ProfesorEvaluado.objects.all():
            if not profesor.slug:
                slug = slugify(profesor.nombre)
                profesor.slug = slug
                profesor.save()
                self.stdout.write(self.style.SUCCESS('Successfully slugified "%s"' % profesor.slug))
            else:
                self.stdout.write(self.style.WARNING('Is already slugyfied "%s" "%s"' % (profesor.nombre, profesor.slug)))
