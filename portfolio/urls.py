# portfolio/urls.py
from django.urls import path
from .views import project_list, project_detail, project_create, project_edit, project_delete

app_name = 'portfolio'

urlpatterns = [
    path('', project_list, name='project_list'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('project/new/', project_create, name='project_create'),
    path('project/<int:pk>/edit/', project_edit, name='project_edit'),
    path('project/<int:pk>/delete/', project_delete, name='project_delete'),
]