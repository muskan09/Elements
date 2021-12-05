# projects/urls.py
from django.urls import path
from .views import ProjectPageListView

urlpatterns = [
        path('', ProjectPageListView.as_view(), name='project_list'),
    ]