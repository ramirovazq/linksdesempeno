from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('<slug:slug_evaluador>/', views.detail, name='detail'),
]
