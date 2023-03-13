from django.db import models

# Create your models here.

class Annonce(models.Model):
    titre=models.CharField(max_length=150)
    contenu = models.TextField()
    image = models.ImageField(default='default.jpg')

class Horaire_messe(models.Model):
    image = models.ImageField(default='default.jpg')

