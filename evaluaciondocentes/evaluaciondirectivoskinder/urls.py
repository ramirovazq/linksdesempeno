from django.urls import path

from . import views

urlpatterns = [
    path('autoreview/profesors/all', views.all_profesors_kinder_autoreview, name='all_profesors_kinder_autoreview'),
    path('autoreview/profesors/detail/<int:profesor_id>', views.detail_kinder_autoreview_profesor, name='detail_autoreview_kinder_profesor'),

    path('evaluate/profesors/all', views.all_profesors_kinder_evaluate, name='all_profesors_kinder_evaluate'),
]
