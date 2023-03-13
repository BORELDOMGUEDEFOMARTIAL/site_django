from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.shortcuts import render
from annonces.models import Annonce,Horaire_messe
from .forms import AnnonceForm,Horaire_messeForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse


class UpdateHoraire_messe(LoginRequiredMixin,UpdateView):
    model=Horaire_messe
    form_class=Horaire_messeForm
    template_name='annonces/horaire_messe_form.html'
    success_url='/horaire_messe'

class UpdateAnnonce(LoginRequiredMixin,UpdateView):
    model=Annonce
    form_class=AnnonceForm
    template_name='annonces/annonce_form.html'
    success_url='/annonces'

class DeleteAnnonce(LoginRequiredMixin,DeleteView):
    model = Annonce
    success_url = "/annonces"
class AddAnnonce(LoginRequiredMixin,CreateView):
    model= Annonce
    form_class = AnnonceForm
    template_name="add-annonce.html"
    success_url = "/annonces"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
