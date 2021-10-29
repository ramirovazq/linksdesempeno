from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('all/alumnos/', views.list_all, name='list_all'),
    path('docente/<int:profesor_id>/', views.detail_profesor, name='detail_profesor'),
    path('<slug:slug_evaluador>/', views.detail, name='detail'),
    # direccion
    path('list/direccion/', views.list_direccion, name='list_direccion'),
    path('evaluador/direccion/<int:evaluador_id>/', views.detail_direccion_evaluador, name='detail_direccion_evaluador'),
]
