"""
    * Yazar : Oktay SAKARYA
    * Tarih : 25.11.2022 21:39 
    * Proje : IHA Proje Bitimine 01 gün 12 saat 34 dakika 56 saniye
    
? user_app/views.py
? Bu dosyada projenin kullanici ekleme login logout işlemleri için yazildi.
? Bu viewlarin url tanimlamalari user_app/urls.py dosyasinda yapilmistir.
?.
"""

# Django dil ayarları için kullanıcak
from django.utils.translation import gettext_lazy as _
# User Modeli için
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

# Model Class
from .models import *
# Form Class
from .forms import *

# Kullanıcı girişi için kullanılacak
def login_(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                login(request,user)
                messages.success(request,_('Giriş Başarılı'))
            except:
                messages.error(request,_('Birşeyler ters gitti! (Docker tarafında migrate işlminin oldugundan emin olun)'))
            return redirect("IHA:index")
        else:
            messages.error(request,_('Geçersiz Kimlik'))
            return redirect('user_app:login_')
    return render(request,"login/login.html")

# Kullanıcı oturumunu kapatmak için kullanılacak
def logout_(request):
    logout(request) 
    messages.success(request,_('Çıkış Başarılı'))
    return redirect('user_app:login_')  

# Kullanıcı ekleme için kullanılacak
def register(request):
    if request.method == "POST":
        form = UserCustomForm(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                login(request, user.user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request,_('Kayıt Başarılı'))
            except:
                messages.error(request,_('Birşeyler ters gitti! (Docker tarafında migrate işlminin oldugundan emin olun)'))
            return redirect('IHA:index')
    else:
        form = UserCustomForm()
    return render(request, 'register/register.html', {'form': form})