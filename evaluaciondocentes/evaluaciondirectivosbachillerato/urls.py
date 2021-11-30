from django.urls import path

from . import views

urlpatterns = [
    path('autoreview/profesors/all', views.all_profesors_autoreview, name='all_profesors_autoreview_bachillerato'),
    path('autoreview/profesors/detail/<int:profesor_id>', views.detail_autoreview_profesor, name='detail_autoreview_profesor_bachillerato'),

    path('evaluate/profesors/all', views.all_profesors_evaluate, name='all_profesors_evaluate_bachillerato'),
]
