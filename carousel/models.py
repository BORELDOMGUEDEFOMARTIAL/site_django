from django.db import models

# Create your models here.

class Carousel(models.Model):
    titre=models.CharField(max_length=150)
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')


    def __str__(self):
        return self.titre

class Article_eglise(models.Model):
    titre=models.CharField(max_length=150)
    contenu = models.TextField()
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')
    lien_article =models.URLField(blank=True)
    
    def __str__(self):
        return self.titre

class Article_paroissiale(models.Model):
    titre=models.CharField(max_length=150)
    contenu = models.TextField()
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')
    lien_article =models.URLField(blank=True)
    document_word = models.FileField(upload_to='public', max_length=254, blank=True,null=True, default='default.doc')
    document_pdf = models.FileField(upload_to='public', max_length=254, blank=True, null=True, default='default.pdf')
        
    def __str__(self):
        return self.titre
class Article_paroissiale_word(models.Model):
    titre=models.CharField(max_length=150)
    contenu = models.TextField()
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')
    lien_article =models.URLField(blank=True)
    document_word = models.FileField(upload_to='public', max_length=254, blank=True,null=True, default='default.doc')
   
        
    def __str__(self):
        return self.titre
class Article_paroissiale_pdf(models.Model):
    titre=models.CharField(max_length=150)
    contenu = models.TextField()
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')
    lien_article =models.URLField(blank=True)
    document_pdf = models.FileField(upload_to='public', max_length=254, blank=True, null=True, default='default.pdf')
        
    def __str__(self):
        return self.titre
class Article_paroissiale_pdf_word(models.Model):
    titre=models.CharField(max_length=150)
    contenu = models.TextField()
    date_publication= models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')
    lien_article =models.URLField(blank=True)
    document_word = models.FileField(upload_to='public', max_length=254, blank=True,null=True, default='default.doc')
    document_pdf = models.FileField(upload_to='public', max_length=254, blank=True, null=True, default='default.pdf')
        
    def __str__(self):
        return self.titre
