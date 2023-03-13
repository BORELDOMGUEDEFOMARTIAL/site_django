from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


app_name="annonces"
urlpatterns = [
   
    path('update-horaire_messe/<int:pk>',UpdateHoraire_messe.as_view(),name="update-horaire_messe"),
     path('update-annonce/<int:pk>',UpdateAnnonce.as_view(),name="update-annonce"),
     path('delete-annonce/<int:pk>',DeleteAnnonce.as_view(),name="delete-annonce"),
     path('add-annonce', AddAnnonce.as_view() ,name="ajouter-annonce"),
]

