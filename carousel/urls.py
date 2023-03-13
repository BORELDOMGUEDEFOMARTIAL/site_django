from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


app_name="carousel"
urlpatterns = [
   
     path('delete-carousel<int:pk>',DeleteCarousel.as_view(),name="delete-carousel"),
     path('add-carousel', AddCarousel.as_view() ,name="ajouter-carousel"),
      path('update-carousel/<int:pk>', UpdateCarousel.as_view() ,name="update-carousel"),
       path('delete-article_eglise<int:pk>',DeleteArticle_eglise.as_view(),name="delete-article_eglise"),
     path('add-article_eglise', AddArticle_eglise.as_view() ,name="ajouter-article_eglise"),
      path('update-article_eglise/<int:pk>', UpdateArticle_eglise.as_view() ,name="update-article_eglise"),
          path('delete-article_paroissiale<int:pk>',DeleteArticle_paroissiale.as_view(),name="delete-article_paroissiale"),
     path('add-article_paroissiale', AddArticle_paroissiale.as_view() ,name="ajouter-article_paroissiale"),
      path('update-article_paroissiale/<int:pk>', UpdateArticle_paroissiale.as_view() ,name="update-article_paroissiale"),
          path('delete-article_paroissiale_word<int:pk>',DeleteArticle_paroissiale_word.as_view(),name="delete-article_paroissiale_word"),
     path('add-article_paroissiale_word', AddArticle_paroissiale_word.as_view() ,name="ajouter-article_paroissiale_word"),
      path('update-article_paroissiale_word/<int:pk>', UpdateArticle_paroissiale_word.as_view() ,name="update-article_paroissiale_word"),
       path('delete-article_paroissiale_pdf<int:pk>',DeleteArticle_paroissiale_pdf.as_view(),name="delete-article_paroissiale_pdf"),
     path('add-article_paroissiale_pdf', AddArticle_paroissiale_pdf.as_view() ,name="ajouter-article_paroissiale_pdf"),
      path('update-article_paroissiale_pdf/<int:pk>', UpdateArticle_paroissiale_pdf.as_view() ,name="update-article_paroissiale_pdf"),
            path('delete-article_paroissiale_pdf_word<int:pk>',DeleteArticle_paroissiale_pdf_word.as_view(),name="delete-article_paroissiale_pdf_word"),
     path('add-article_paroissiale_pdf_word', AddArticle_paroissiale_pdf_word.as_view() ,name="ajouter-article_paroissiale_pdf_word"),
      path('update-article_paroissiale_pdf_word/<int:pk>', UpdateArticle_paroissiale_pdf_word.as_view() ,name="update-article_paroissiale_pdf_word"),
       



]

