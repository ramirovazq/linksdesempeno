from django.urls import path

from . import views

urlpatterns = [
    path('group/all', views.all_groups, name='all_groups'),
    path('group/detail/<int:group_id>', views.detail_group, name='detail_group'),

    path('profesors/all', views.all_profesors, name='all_profesors'),
    path('profesors/detail/<int:profesor_id>', views.detail_profesor, name='detail_profesor'),
]
