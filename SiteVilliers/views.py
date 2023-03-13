from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.shortcuts import render
from images_en_tete.models import Image_en_tete
from images_en_tete.forms import Images_en_teteForm
from carousel.models import Carousel,Article_eglise,Article_paroissiale,Article_paroissiale_word,Article_paroissiale_pdf,Article_paroissiale_pdf_word
from galerie.models import Eglise_jacques_christophe, Accueil,Les_soeurs,Sacre_coeur_bois_gaumont,Jeune_18_35,Sainte_anne
from .forms import ContactForm 
from annonces.models import Annonce,Horaire_messe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    actualites_paroissiale= Article_paroissiale.objects.all()
    actualites_eglise= Article_eglise.objects.all()
    carousels = Carousel.objects.all()
    images_en_tete= Image_en_tete.objects.all()
    k = 0
    context = {
        'actualites_paroissiale':actualites_paroissiale,
        'actualites_eglise':actualites_eglise,
        'images_en_tete':images_en_tete,
        'k': k,
        'carousels':carousels
    }
    return render(request,'home.html', context)

def annonces(request):
    annonces=Annonce.objects.all()

    return render(request, 'annonces.html', context={'annonces':annonces})

def faire_un_don(request):
    return render(request, 'faire_un_don.html')
def contact(request):
    form = ContactForm()
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom= form.cleaned_data['nom']
            prenom= form.cleaned_data['prenom']
            email= form.cleaned_data['email']
            message= form.cleaned_data['message']
            print(nom, prenom, email,message)
            titre=f'Blog | {nom} {prenom} {email}'
            send_mail(titre,message,'martialdomgue@gmail.com',
            ['martialdomgue@gmail.com'])
        return HttpResponseRedirect(reverse('remerciements'))
    return render(request,'contact.html',{"form":form})

def actualites(request):
    actualites_eglise= Article_eglise.objects.all()
    actualites_paroissiale = Article_paroissiale.objects.all()
    context={
        'actualites_eglise':actualites_eglise,
        'actualites_paroissiale': actualites_paroissiale
    }
    return render(request, 'actualites.html',context)
def actualites_eglise(request):
    actualites_eglise= Article_eglise.objects.all()
    context={
        'actualites_eglise':actualites_eglise
        
    }
    return render(request, 'actualites_eglise.html',context)
def actualites_paroissiale(request):
    actualites_paroissiale = Article_paroissiale.objects.all()
    actualites_paroissiale_word = Article_paroissiale_word.objects.all()
    actualites_paroissiale_pdf = Article_paroissiale_pdf.objects.all()
    actualites_paroissiale_pdf_word = Article_paroissiale_pdf_word.objects.all()
    context={
        'actualites_paroissiale': actualites_paroissiale,
        'actualites_paroissiale_word': actualites_paroissiale_word,
        'actualites_paroissiale_pdf': actualites_paroissiale_pdf,
        'actualites_paroissiale_pdf_word': actualites_paroissiale_pdf_word
    }
    return render(request, 'actualites_paroissiale.html',context)
def horaire_messe(request):
    horaire_messe=Horaire_messe.objects.all()
    return render(request, 'horaire_messe.html', context={'horaire_messe':horaire_messe})
def infos_pratique(request):
    return render(request, 'infos_pratique.html')
def aller_au_kt(request):
    return render(request, 'aller_au_kt.html')
def histoire(request):
    return render(request, 'histoire.html')
def coquille(request):
    return render(request, 'coquille.html')
def liens_utils(request):
    return render(request, 'liens_utils.html')
def eveil_a_la_foi(request):
    return render(request, 'eveil_a_la_foi.html')
def cathechisme_du_primaire(request):
    return render(request, 'cathechisme_du_primaire.html')
def cathechisme_6è_5è(request):
    return render(request, 'cathechisme_6è_5è.html')
def communion(request):
    return render(request, 'communion.html')
def aumonerie_jeunes(request):
    return render(request, 'aumonerie_jeunes.html')
def parcours_confirmation(request):
    return render(request, 'parcours_confirmation.html')
def pour_aller_loin(request):
    return render(request, 'pour_aller_loin.html')
def vivre_en_eglise(request):
    return render(request, 'vivre_en_eglise.html')
def guide_scouts(request):
    return render(request, 'guide_scouts.html')
def communaute_religieuse(request):
    return render(request, 'communaute_religieuse.html')
def prier_celebrer(request):
    return render(request, 'prier_celebrer.html')
def equipe_animation_liturgique(request):
    return render(request, 'equipe_animation_liturgique.html')
def equipe_animation_paroissiale(request):
    return render(request, 'equipe_animation_paroissiale.html')
def chorale(request):
    return render(request, 'chorale.html')
def pour_en_aider(request):
    return render(request, 'pour_en_aider.html')
def conseil_economique_paroissiale(request):
    return render(request, 'conseil_economique_paroissiale.html')
def dernier_de_eglise(request):
    return render(request, 'dernier_de_eglise.html')
def secours_catholique(request):
    return render(request, 'secour_catholique.html')
def société_saint_vincent_paul(request):
    return render(request, 'société_saint_vincent_de_paul.html')
def CCFD(request):
    return render(request, 'CCFD.html')
def pour_sinformer(request):
    return render(request, 'pour_sinformer.html')
def chantier_cardinal(request):
    return render(request, 'chantier_cardinal.html')
def celebrer(request):
    return render(request, 'celebration_foi.html')
def bapteme(request):
    return render(request, 'bapteme.html')
def eucharistie(request):
    return render(request, 'eucharistie.html')
def confirmation(request):
    return render(request, 'confirmation.html')
def reconciliation(request):
    return render(request, 'reconciliation.html')
def mariage(request):
    return render(request, 'mariage.html')
def sacrement_malade(request):
    return render(request, 'sacrement_malade.html')
def funéraille(request):
    return render(request, 'funéraille.html')
def calendrier(request):
    return render(request, 'calendrier.html')
def prier(request):
    return render(request, 'prier.html')
def chapelet(request):
    return render(request, 'chapelet.html')
def adoration(request):
    return render(request, 'adoration.html')
def equipe_pastorale(request):
    return render(request, 'equipe_pastorale.html')

def galerie(request):
    cathegorie1= Eglise_jacques_christophe.objects.all()
    cathegorie2= Accueil.objects.all()
    cathegorie3= Jeune_18_35.objects.all()
    cathegorie4= Sacre_coeur_bois_gaumont.objects.all()
    cathegorie5 =Les_soeurs.objects.all()
    cathegorie6=Sainte_anne.objects.all()

    context={
        'cathegorie1': cathegorie1,
        'cathegorie2': cathegorie2,
        'cathegorie3': cathegorie3,
        'cathegorie4': cathegorie4,
        'cathegorie5': cathegorie5,
        'cathegorie6': cathegorie6
    }
    return render(request, 'galerie.html' ,context)

