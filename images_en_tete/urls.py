from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *


app_name="images_en_tete"
urlpatterns = [
   
    path('update-article/<int:pk>',UpdateArticle.as_view(),name="update-article"),

]



