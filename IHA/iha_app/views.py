"""
    * Yazar : Oktay SAKARYA
    * Tarih : 25.11.2022 21:39 
    * Proje : IHA Proje Bitimine 01 gün 12 saat 34 dakika 56 saniye
    
? iha_app/views.py
? Bu dosyada projenin ana kismi olan viewlar tanimlanir.
? Bu viewlarin url tanimlamalari iha_app/urls.py dosyasinda yapilmistir.
? Taskta yer alan update, delete, create gibi islemler burada yapilmistir.
"""


# Django dil ayarları için kullanıcak
from django.utils.translation import gettext_lazy as _
# User Modeli için
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.conf import settings


# Model Class
from .models import *
# Form Class
from .forms import *

# İha ekleme için kullanılacak 
# view fonksiyonu
@user_passes_test(lambda u: u.is_active and (u.is_authenticated),login_url="user_app:login_")
def add_new_iha(request):
    category = Category.objects.all().count()
    if category == 0:
        messages.info(request,_('Önce kategori ekleyiniz'))
        return redirect('IHA:add_new_category')
    if request.method == "POST":
        form = IhaForm(request.POST, request.FILES) # Formu oluşturur ve POST ile gelen verileri alır
        if form.is_valid():          # Formun geçerliliğini kontrol eder
            form.save()              # Formu kaydeder
            messages.success(request,_('İHA Başarıyla Eklendi')) # İHA başarıyla eklendi mesajı
            return redirect('IHA:index') # Ana sayfaya yönlendirir
    else:
        form = IhaForm()                # Get isteği geldiğinde formu oluşturur
    return render(request, 'iha/add_new_iha.html', {'form': form}) # Template render eder ve Formu gönderir

@user_passes_test(lambda u: u.is_active and (u.is_authenticated),login_url="user_app:login_")
def update_iha(request, id):
    iha = get_object_or_404(IHA, id=id)
    form = IhaForm(request.POST or None,request.FILES or None, instance=iha)
    if form.is_valid():
        form.save()
        messages.success(request,_('İHA Başarıyla Güncellendi'))
        return redirect('IHA:index')
    return render(request, 'iha/update_iha.html', {'form': form})

@user_passes_test(lambda u: u.is_active and (u.is_authenticated),login_url="user_app:login_")
def delete_iha(request, id):
    iha = get_object_or_404(IHA, id=id)
    iha.delete()
    messages.success(request,_('İHA Başarıyla Silindi'))
    return redirect('IHA:index')

@user_passes_test(lambda u: u.is_active and (u.is_authenticated),login_url="user_app:login_")
def iha_list(request):
    iha_list = IHA.objects.all()
    query = request.GET.get("q",None) # Filterelem için arama formuna gelen query değerini alır
    page = request.GET.get('p',1)     # Sayfalama için gelen sayfa değerini alır
    if query:                         # Eğer query değeri varsa
        iha_list = iha_list.filter(   # İHA listesini filtreler
            Q(device_id__icontains=query) |
            Q(device_type__icontains=query) |
            Q(category__title__icontains=query) |
            Q(device_name__icontains=query) |
            Q(device_status__icontains=query)
        ).distinct()
    paginator = Paginator(iha_list,settings.PAGINATION_NUMBER) # Show 25 contacts per page
    iha_list = paginator.page(number=page)                     # Sayfalama işlemi
    page_range = paginator.get_elided_page_range(number=page)   
    context = {
        'iha_list': iha_list,
        'paginator': paginator,
        'page_range': page_range,
    }
    return render(request, 'iha/iha_list.html',context)

@user_passes_test(lambda u: u.is_active and (u.is_authenticated),login_url="user_app:login_")
def index(request):
    categories = Category.objects.filter(status=True)
    context = {
        'categories': categories,
    }
    return render(request, 'homePage/index.html',context)

@user_passes_test(lambda u: u.is_active and (u.is_authenticated),login_url="user_app:login_")
def add_new_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST, request.FILES) # Formu oluşturur ve POST ile gelen verileri alır
        if form.is_valid():
            form.save()
            messages.success(request,_('Kategori Başarıyla Eklendi'))
            return redirect('IHA:index')
    else:
        form = AddCategoryForm()
    return render(request, 'iha/add_category.html', {'form': form})