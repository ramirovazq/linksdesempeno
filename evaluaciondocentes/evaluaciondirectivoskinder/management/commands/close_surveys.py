from django.core.management.base import BaseCommand
from evaluaciondirectivoskinder.models import Profesor
from evaluaciondirectivoskinder.models import EquipoDirectivo

class Command(BaseCommand):
    help = 'Close Surveys autoevaluacion Kinder in Lime.'

    def handle(self, *args, **options):

        for profesor in Profesor.objects.all():
            profesor.survey_closed = True
            profesor.save()
            self.stdout.write(self.style.SUCCESS(f'Success in close Profesor {profesor.id}'))

        for equipodirectivo in EquipoDirectivo.objects.all():
            equipodirectivo.survey_closed = True
            equipodirectivo.save()
            self.stdout.write(self.style.SUCCESS(f'Success in close EquipoDirectivo {equipodirectivo.id}'))
