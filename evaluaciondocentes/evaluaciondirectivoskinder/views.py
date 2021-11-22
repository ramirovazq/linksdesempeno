from django.shortcuts import render, get_object_or_404
from .models import Profesor, EquipoDirectivo
from django.conf import settings


def all_profesors_kinder_evaluate(request):
    equipodirectivo = EquipoDirectivo.objects.all()
    objetos = equipodirectivo

    objetos = sorted(objetos, key=lambda x: x.nombre)

    context = {'objetos': objetos}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT_AUTOEVALUACION_KINDER'] = "Evaluación Desempeño Docente equipo directivo kínder"
    return render(request, 'directivos_evalua_kinder/list.html', context)

def all_profesors_kinder_autoreview(request):

    profesores = Profesor.objects.all()


    objetos = profesores
    objetos = sorted(objetos, key=lambda x: x.nombre)


    context = {'objetos': objetos}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT_AUTOEVALUACION_KINDER'] = "Autoevaluación Desempeño Docente Kinder"

    return render(request, 'profesors_autoevaluacion_kinder/list.html', context)


def detail_kinder_autoreview_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    context = {'objeto': profesor}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT_AUTOEVALUACION_KINDER'] = "Autoevaluación Desempeño Docente Kinder"
    return render(request, 'profesors_autoevaluacion_kinder/detail.html', context)