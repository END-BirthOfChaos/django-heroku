from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('formulaire/', views.formulaire, name='formulaire'),
    path('wordgenerator/', views.wordgenerator, name='wordgenerator'),
]
