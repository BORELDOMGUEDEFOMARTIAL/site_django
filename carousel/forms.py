from django.forms import ModelForm
from .models import Carousel,Article_eglise,Article_paroissiale,Article_paroissiale_pdf,Article_paroissiale_pdf_word,Article_paroissiale_word
from django import forms


class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['titre','image']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'})
        }
   
class Article_egliseForm(forms.ModelForm):
    class Meta:
        model = Article_eglise
        fields = ['titre','image','contenu','lien_article']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'contenu':forms.Textarea(attrs={'class':'form-control'})
        }
class Article_paroissialeForm(forms.ModelForm):
    class Meta:
        model = Article_paroissiale
        fields = ['titre','image','contenu','lien_article']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'contenu':forms.Textarea(attrs={'class':'form-control'})
        }
class Article_paroissiale_wordForm(forms.ModelForm):
    class Meta:
        model = Article_paroissiale_word
        fields = ['titre','image','contenu','lien_article','document_word']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'contenu':forms.Textarea(attrs={'class':'form-control'})
        }
class Article_paroissiale_pdfForm(forms.ModelForm):
    class Meta:
        model = Article_paroissiale_pdf
        fields = ['titre','image','contenu','lien_article','document_pdf']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'contenu':forms.Textarea(attrs={'class':'form-control'})
        }
class Article_paroissiale_pdf_wordForm(forms.ModelForm):
    class Meta:
        model = Article_paroissiale_pdf_word
        fields = ['titre','image','contenu','lien_article','document_word','document_pdf']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'contenu':forms.Textarea(attrs={'class':'form-control'})
        }
