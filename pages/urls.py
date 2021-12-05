# pages/urls.py
from django.urls import path
from .views import HomePageView, DetailsPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('details/', DetailsPageView, name='details'),
    ]