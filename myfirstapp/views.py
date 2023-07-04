from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from .forms import GeneratorForm, WordForm, LivreForm, BiblioForm


import api
import engine


# Create your views here.
def accueil(request):

    api.getMenu("seasonskyV3", "noel", "fffff", 6).save("myfirstapp/static/images/generated.png")
    return render(request, "myfirstapp/accueil.html")


def formulaire(request):
    if request.method == "POST":
        form = GeneratorForm(data=request.POST)
        if form.is_valid():
            datas = form.save()
            data_serveur = datas.serveur
            data_theme = datas.theme
            data_taille = datas.taille
            data_titre = datas.titre
            api.getMenu(data_serveur, data_theme, data_titre, data_taille).save("myfirstapp/static/images/generated.png")
            return render(request, 'myfirstapp/formulaire.html', {'form': form, 'datas': datas})
        else:
            return render(request, 'myfirstapp/formulaire.html', {'form': form})
    else:
        form = GeneratorForm()
        return render(request, 'myfirstapp/formulaire.html', {'form': form})


def wordgenerator(request):
    if request.method == "POST":
        form = WordForm(data=request.POST)
        if form.is_valid():
            datas = form.save()
            data_serveur = datas.serveur
            data_theme = datas.theme
            data_titre = datas.titre
            engine.createWordImage(data_serveur, data_theme, data_titre)[0].save("myfirstapp/static/images/wordgenerated.png")
            return render(request, 'myfirstapp/wordgenerator.html', {'form': form, 'datas': datas})
        else:
            return render(request, 'myfirstapp/wordgenerator.html', {'form': form})
    else:
        form = WordForm()
        return render(request, 'myfirstapp/wordgenerator.html', {'form': form})

def index(request):
    Biblio =models.Biblio.objects.get(pk=id)
    liste=list(models.Livre.objects.filter(bibliotheque_id=id))
    return render(request,"myfirstapp/testaffiche.html",{"biblio": Biblio, "liste": liste})
