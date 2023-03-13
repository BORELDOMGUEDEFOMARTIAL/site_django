from django.forms import ModelForm
from .models import Horaire_messe,Annonce
from django import forms


class Horaire_messeForm(forms.ModelForm):
    class Meta:
        model = Horaire_messe
        fields = ['image']
     

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre','contenu']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'contenu':forms.Textarea(attrs={'class':'form-control'})
        }
