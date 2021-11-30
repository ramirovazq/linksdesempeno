from django.urls import path

from . import views

urlpatterns = [
    path('group/all', views.all_groups, name='all_groups_bachillerato'),
    path('group/detail/<int:group_id>', views.detail_group, name='detail_group_bachillerato'),

    path('profesors/all', views.all_profesors, name='all_profesors_bachillerato'),
    path('profesors/detail/<int:profesor_id>', views.detail_profesor, name='detail_profesor_bachillerato'),
]
