from django.contrib import admin
from django.urls import path, include
from . import views

app_name="app_auth"
urlpatterns = [
   
    path('page_modification_paroisse-saint_jacques_saint-chistophe',views.login_applifoot ,name='loginappli'),
    path('logout',views.logout_appli ,name='logout'),
   
]
