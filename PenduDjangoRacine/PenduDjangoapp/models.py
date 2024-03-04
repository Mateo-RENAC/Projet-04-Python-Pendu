from django.db import models

class ModelScore(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    win = models.CharField(max_length=5, choices=[('oui', 'Oui'), ('non', 'Non')])

