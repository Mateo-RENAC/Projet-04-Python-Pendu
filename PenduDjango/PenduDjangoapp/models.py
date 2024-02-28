from django.db import models

# Create your models here.

# Dans le fichier models.py de votre application

from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=10)

class Score(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    win = models.CharField(max_length=3, choices=[("oui", "oui"), ("non", "non")])

class Mot(models.Model):
    mot = models.CharField(max_length=20)
