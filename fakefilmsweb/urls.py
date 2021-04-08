from django.contrib import admin
from django.urls import path
from . import views

app_name = 'fakefilmsweb'

urlpatterns = [
    path('', views.homeView, name='home'),
]