from django.shortcuts import render, get_object_or_404
from .models import Profesor, GrupoAlumnos
from django.conf import settings

def all_groups(request):
    groups = GrupoAlumnos.objects.all()
    memo_list = []

    objetos = []
    for group in groups:
        if not group.grupo in memo_list:
            memo_list.append(group.grupo)
            objetos.append(group)

    objetos = sorted(objetos, key=lambda x: x.grupo)
    context = {'objetos': objetos}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT_PRIMARIA'] = settings.COLLEGE_INSTRUMENT_PRIMARIA
    return render(request, 'grupos/list.html', context)

def detail_group(request, group_id):
    group = get_object_or_404(GrupoAlumnos, id=group_id)
    groups = GrupoAlumnos.objects.filter(grupo=group.grupo)    
    context = {'objetos': groups, 'objeto': groups[0]}

    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT_PRIMARIA'] = settings.COLLEGE_INSTRUMENT_PRIMARIA
    return render(request, 'grupos/detail.html', context)


def all_profesors(request):
    profesors = Profesor.objects.all()
    memo_list = []

    objetos = []
    for profesor in profesors:
        if not profesor.nombre in memo_list:
            memo_list.append(profesor.nombre)
            objetos.append(profesor)

    objetos = sorted(objetos, key=lambda x: x.nombre)

    context = {'objetos': objetos}
    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT_AUTOEVALUACION_PRIMARIA'] = settings.COLLEGE_INSTRUMENT_AUTOEVALUACION_PRIMARIA
    return render(request, 'profesors/list.html', context)


def detail_profesor(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    objetos = GrupoAlumnos.objects.filter(profesor__nombre=profesor.nombre)
    context = {'objetos': objetos, 'objeto': profesor}


    context['COLLEGE_NAME'] = settings.COLLEGE_NAME
    context['COLLEGE_URL'] = settings.COLLEGE_URL
    context['COLLEGE_INSTRUMENT_AUTOEVALUACION_PRIMARIA'] = settings.COLLEGE_INSTRUMENT_AUTOEVALUACION_PRIMARIA
    return render(request, 'profesors/detail.html', context)
