from django.db import models
from django import forms
import json

class GenerateTemplate(models.Model):

    # Opening JSON file
    f = open('module-config.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    THEME_CHOICES = ()
    SERVER_CHOICES = ()
    SIZE_CHOICES = (
        (4, 4),
        (5, 5),
        (6, 6),
    )
    for i in data:
        SERVER_CHOICES = list(SERVER_CHOICES)
        SERVER_CHOICES.append((i, i))
        for i in data["seasonskyV3"]["themes"]:
            THEME_CHOICES = list(THEME_CHOICES)
            THEME_CHOICES.append((i, i))



    titre = models.CharField(max_length=100)
    serveur = models.CharField(max_length=100, choices=SERVER_CHOICES)
    theme = models.CharField(max_length=100, choices=THEME_CHOICES)
    taille = models.IntegerField(max_length=100, choices=SIZE_CHOICES)




    def __str__(self):
        chaine = f"Titre : {self.titre} | Taille : {self.taille} | Theme : {self.theme} | Serveur : {self.serveur}"
        return chaine

    def dico(self):
        return {"titre":self.titre, "serveur": self.serveur, "theme":self.theme, "taille":self.taille}


class Mot(models.Model):

    # Opening JSON file
    f = open('module-config.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    THEME_CHOICES = (('', 'Sélectionnez'), )
    SERVER_CHOICES = (('', 'Sélectionnez'), )

    for i in data:
        SERVER_CHOICES = list(SERVER_CHOICES)
        SERVER_CHOICES.append((i, i))
        for j in data["seasonskyV3"]["themes"]:
            THEME_CHOICES = list(THEME_CHOICES)
            THEME_CHOICES.append((j, j))



    titre = models.CharField(max_length=100)
    serveur = models.CharField(max_length=100, choices=SERVER_CHOICES)
    theme = models.CharField(max_length=100, choices=THEME_CHOICES)


    def __str__(self):
        chaine = f"Titre : {self.titre} | Taille :  | Theme : {self.theme} | Serveur : {self.serveur}"
        return chaine

    def dico(self):
        return {"titre":self.titre, "serveur": self.serveur, "theme":self.theme}













class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length = 100)
    #date_parution = models.DateField(blank=True, null=True)
    bibliotheque = models.ForeignKey("Biblio", on_delete=models.CASCADE, null=True)
    nombres_pages = models.IntegerField(blank=False)
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"Titre : {self.titre} | Auteur : {self.auteur}"
        return chaine

    def dico(self):
        return {"titre":self.titre, "auteur": self.auteur, "nombres_pages":self.nombres_pages, "resume":self.resume}



class Biblio(models.Model):
    nom = models.CharField(max_length=100)
    region = models.CharField(max_length = 100)
    #date_parution = models.DateField(blank=True, null=True)
    ville = models.CharField(max_length = 100)
    nombre_livre = models.IntegerField(blank=False)

    def __str__(self):
        chaine = f"Bibliothèque '{self.nom}' | Située dans la région {self.region}"
        return chaine

    def dico(self):
        return {"nom":self.nom, "ville": self.ville, "nombre_livre":self.nombre_livre, "region":self.region}