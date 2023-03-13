from django.db import models

# Create your models here.

class Image_en_tete(models.Model):
    titre=models.CharField(max_length=150)
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.titre
                         