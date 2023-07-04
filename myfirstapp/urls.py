from django.urls import path

from . import views

urlpatterns = [
    path('accueil/', views.accueil),
    path('formulaire/', views.formulaire),
    path('wordgenerator/', views.wordgenerator),
]
