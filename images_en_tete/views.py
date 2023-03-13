from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.shortcuts import render
from images_en_tete.models import Image_en_tete
from images_en_tete.forms import Images_en_teteForm
from annonces.models import Annonce,Horaire_messe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse


class UpdateArticle(LoginRequiredMixin,UpdateView):
    model=Image_en_tete
    form_class=Images_en_teteForm
    template_name='images_en_tete/image_en_tete_form.html'
    success_url='/'