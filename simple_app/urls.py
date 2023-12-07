# simple_app/urls.py

from django.urls import path
from simple_app import views

urlpatterns = [
path(r'', views.HomePageView.as_view()),
]
