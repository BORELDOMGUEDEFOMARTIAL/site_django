from django.forms import ModelForm
from .models import Image_en_tete
from django import forms


class Images_en_teteForm(forms.ModelForm):
    class Meta:
        model = Image_en_tete
        fields = ['titre','image']
        widgets = {
            'titre':forms.TextInput(attrs={'class':'form-control'}),
           
        }
