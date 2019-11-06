from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('generate/', views.generate, name="generate"),
    path('departament/', views.departament, name="departament"),
    path('new_departament/', views.new_departament, name="new_departament"),
    path('del_departament/<int:id>/', views.del_departament, name="del_departament"),
    path('programs/', views.programs, name="programs"),
    path('my_program/<int:id>/', views.my_program, name="my_program"),
    path('del_program/<int:id>/', views.del_program, name="del_program"),
    path('new_program/<int:id_departament>/', views.new_program, name="new_program"),
]