from django.shortcuts import render, get_object_or_404
from docentes.models import Evaluador
from django.conf import settings


def index(request):
    context = {}
    return render(request, 'docentes/index.html', context)

def detail(request, slug_evaluador):
    list_evaluaciones = Evaluador.objects.filter(slug=slug_evaluador)
    if len(list_evaluaciones) > 0:
        evaluador = list_evaluaciones[0]
    context = {'objetos': list_evaluaciones, 'objeto': evaluador}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT'] = settings.COLLEGE_INSTRUMENT
    return render(request, 'docentes/detail.html', context)

def list(request):
    list_evaluadores = Evaluador.objects.all()
    memo_list = []
    objetos = []
    for evaluador in list_evaluadores:
        if not evaluador.nombre_o_grupo in memo_list:
            memo_list.append(evaluador.nombre_o_grupo)
            objetos.append(evaluador)
    context = {'objetos': objetos}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT'] = settings.COLLEGE_INSTRUMENT
    return render(request, 'docentes/list.html', context)
