from django.db import models

# Create your models here.
class Taches(models.Model):
    tache = models.CharField(max_length=100)
    etat = models.BooleanField(default=False)