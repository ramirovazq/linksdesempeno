from django.shortcuts import render, get_object_or_404
from docentes.models import Evaluador, ProfesorEvaluado
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
    list_evaluadores = Evaluador.objects.filter(instrumento_para_alumnos=True)
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

def list_all(request):
    objetos = ProfesorEvaluado.objects.filter(instrumento_para_alumnos=True)


    context = {'objetos': objetos}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT'] = settings.COLLEGE_INSTRUMENT
    return render(request, 'docentes/profesores.html', context)

def detail_profesor(request, profesor_id):
    profesor = get_object_or_404(ProfesorEvaluado, pk=profesor_id)

    evaluadores = Evaluador.objects.filter(evaluado=profesor)

    context = {'objeto': profesor, 'objetos': evaluadores }
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT'] = settings.COLLEGE_INSTRUMENT
    return render(request, 'docentes/detail.html', context)


def list_direccion(request):
    list_evaluadores = Evaluador.objects.filter(instrumento_para_alumnos=False)

    memo_list = []
    objetos = []
    for evaluador in list_evaluadores:
        if not evaluador.nombre_o_grupo in memo_list:
            memo_list.append(evaluador.nombre_o_grupo)
            objetos.append(evaluador)


    context = {'objetos': objetos}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT'] = settings.COLLEGE_INSTRUMENT_DIRECCION
    # return render(request, 'docentes/profesores_direccion.html', context)
    return render(request, 'docentes/direccion_list.html', context)



def detail_direccion_evaluador(request, evaluador_id):
    evaluador = get_object_or_404(Evaluador, pk=evaluador_id)

    #evaluadores = Profesor.objects.filter(evaluador=profesor)
    objetos = Evaluador.objects.filter(nombre_o_grupo=evaluador.nombre_o_grupo, instrumento_para_alumnos=False)

    context = {'objeto': evaluador, 'objetos': objetos}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT'] = settings.COLLEGE_INSTRUMENT_DIRECCION
    return render(request, 'docentes/detail_evaluador.html', context)
