from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('gerar/', views.generate_file, name="gerarPadrao"),
]