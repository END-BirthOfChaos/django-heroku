from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class GeneratorForm(ModelForm):
    class Meta:
        model = models.GenerateTemplate
        fields = ('titre', 'serveur', 'theme','taille')
        labels = {
            'titre' : _('Titre'),
            'serveur' : _('Serveur'),
            'theme' : _('Thème'),
            'taille' : _('Taille'),
        }

class WordForm(ModelForm):
    class Meta:
        model = models.Mot
        fields = ('titre', 'serveur', 'theme')
        labels = {
            'titre' : _('Titre'),
            'serveur' : _('Serveur'),
            'theme' : _('Thème'),
        }













class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
#        fields = ('titre', 'auteur', 'date_parution', 'nombres_pages','resume')
        fields = ('titre', 'auteur', 'bibliotheque','nombres_pages','resume')

        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur') ,
            #'date_parution' : _('date␣de␣parution'),
            'bibliotheque' : _('Bibliotheque'),
            'nombres_pages' : _('Nombres de pages'),
            'resume' : _('Résumé')
        }


class BiblioForm(ModelForm):
    class Meta:
        model = models.Biblio
        fields = ('nom','region','ville','nombre_livre')

        labels = {
            'nom' : _('Nom'),
            'region' : _('Région') ,
            'ville' : _('Ville'),
            'nombre_livre' : _('Nombre de livres')
        }

