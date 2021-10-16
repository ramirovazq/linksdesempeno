from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('all/', views.list_all, name='list_all'),
    path('docente/<int:profesor_id>/', views.detail_profesor, name='detail_profesor'),
    path('<slug:slug_evaluador>/', views.detail, name='detail'),
]
