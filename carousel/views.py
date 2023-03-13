from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.shortcuts import render
from .forms import CarouselForm,Article_egliseForm,Article_paroissialeForm,Article_paroissiale_pdfForm,Article_paroissiale_wordForm,Article_paroissiale_pdf_wordForm
from .models import Carousel ,Article_eglise,Article_paroissiale,Article_paroissiale_pdf,Article_paroissiale_word,Article_paroissiale_pdf_word
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse


class DeleteCarousel(LoginRequiredMixin,DeleteView):
    model = Carousel
    success_url = "/"

class AddCarousel(LoginRequiredMixin,CreateView):
    model= Carousel
    form_class = CarouselForm
    template_name="add-carousel.html"
    success_url = "/"

class UpdateCarousel(LoginRequiredMixin,UpdateView):
    model=Carousel
    form_class=CarouselForm
    template_name='carousel/carousel_form.html'
    success_url='/'

class DeleteArticle_eglise(LoginRequiredMixin,DeleteView):
    model = Article_eglise
    success_url = "/actualites_eglise"

class AddArticle_eglise(LoginRequiredMixin,CreateView):
    model= Article_eglise
    form_class = Article_egliseForm
    template_name="add-article_eglise.html"
    success_url = "/actualites_eglise"

class UpdateArticle_eglise(LoginRequiredMixin,UpdateView):
    model=Article_eglise
    form_class=Article_egliseForm
    template_name='carousel/article_eglise_form.html'
    success_url='/actualites_eglise'

class DeleteArticle_paroissiale(LoginRequiredMixin,DeleteView):
    model = Article_paroissiale
    success_url = "/actualites_paroissiale"

class AddArticle_paroissiale(LoginRequiredMixin,CreateView):
    model= Article_paroissiale
    form_class = Article_paroissialeForm
    template_name="add-article_paroissiale.html"
    success_url = "/actualites_paroissiale"

class UpdateArticle_paroissiale(LoginRequiredMixin,UpdateView):
    model=Article_paroissiale
    form_class=Article_paroissialeForm
    template_name='carousel/article_paroissiale_form.html'
    success_url='/actualites_paroissiale'
class DeleteArticle_paroissiale_word(LoginRequiredMixin,DeleteView):
    model = Article_paroissiale_word
    success_url = "/actualites_paroissiale"

class AddArticle_paroissiale_word(LoginRequiredMixin,CreateView):
    model= Article_paroissiale_word
    form_class = Article_paroissiale_wordForm
    template_name="add-article_paroissiale_word.html"
    success_url = "/actualites_paroissiale"

class UpdateArticle_paroissiale_word(LoginRequiredMixin,UpdateView):
    model=Article_paroissiale_word
    form_class=Article_paroissiale_wordForm
    template_name='carousel/article_paroissiale_word_form.html'
    success_url='/actualites_paroissiale'
class DeleteArticle_paroissiale_pdf(LoginRequiredMixin,DeleteView):
    model = Article_paroissiale_pdf
    success_url = "/actualites_paroissiale"

class AddArticle_paroissiale_pdf(LoginRequiredMixin,CreateView):
    model= Article_paroissiale_pdf
    form_class = Article_paroissiale_pdfForm
    template_name="add-article_paroissiale_pdf.html"
    success_url = "/actualites_paroissiale"

class UpdateArticle_paroissiale_pdf(LoginRequiredMixin,UpdateView):
    model=Article_paroissiale_pdf
    form_class=Article_paroissiale_pdfForm
    template_name='carousel/article_paroissiale_pdf_form.html'
    success_url='/actualites_paroissiale'
class DeleteArticle_paroissiale_pdf_word(LoginRequiredMixin,DeleteView):
    model = Article_paroissiale_pdf_word
    success_url = "/actualites_paroissiale"

class AddArticle_paroissiale_pdf_word(LoginRequiredMixin,CreateView):
    model= Article_paroissiale_pdf_word
    form_class = Article_paroissiale_pdf_wordForm
    template_name="add-article_paroissiale_pdf_word.html"
    success_url = "/actualites_paroissiale"

class UpdateArticle_paroissiale_pdf_word(LoginRequiredMixin,UpdateView):
    model=Article_paroissiale_pdf_word
    form_class=Article_paroissiale_pdf_wordForm
    template_name='carousel/article_paroissiale_pdf_word_form.html'
    success_url='/actualites_paroissiale'