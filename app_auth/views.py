from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import*
# Create your views here.

def login_applifoot(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"authentification échouée")
                return render(request,'login.html', {'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            return render (request, 'login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form})
    
    
def logout_appli(request):
    logout(request)
    return redirect("app_auth:loginappli")
