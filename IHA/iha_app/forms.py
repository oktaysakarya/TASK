from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import *

# ? iha_app/forms.py
# ? Bu dosyada projenin ana kismi olan formlar tanimlanir.
# ? Bu formlar ekleme, guncelleme gibi islemler icin kullanilir.
# ? Djangonun ModelForm sinifini kullanarak formu olusturduk.

class IhaForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = '__all__'
        # Modelden Gelen defult labelları degistirdik
        labels = {
            'category': _('Kategori'),
            'device_name': _('Cihaz Adı'),
            'device_model': _('Cihaz Modeli'),
            'device_serial_number': _('Cihaz Seri Numarası'),
            'device_id': _('Cihaz ID'),
            'device_type': _('Cihaz Tipi'),
            'device_status': _('Cihaz Durumu'),
            'device_image': _('Cihaz Resmi'),
            'device_weight': _('Cihaz Ağırlığı'),
            'device_ammo_capacity': _('Cihazın Mermi Kapasitesi'),
            'device_fuel_capacity': _('Cihazın Yakıt Kapasitesi'),
            'device_battery_capacity': _('Cihazın Pil Kapasitesi'),
            'device_flying_range': _('Cihazın Uçuş Menzili'),
            'device_flying_speed': _('Cihazın Uçuş Hızı'),
            'device_flying_altitude': _('Cihazın Uçuş Yüksekliği'),
        }
    # formdan yapılan istekleri database kaydetmeden önce burada kontrol ediyoruz.
    # serial number kolonu unique olduğu için aynı serial number ile kayıt yapılamaz.
    # Bunun için clean_device_serial_number fonksiyonunu override ettik.
    def clean_device_serial_number(self):
        device_serial_number = self.cleaned_data.get('device_serial_number')
        if device_serial_number != self.instance.device_serial_number: # Güncelleme yapılırken device_serial_number değişmemişse
            if IHA.objects.filter(device_serial_number=device_serial_number).exists(): # Kayıt İşleminde device_serial_number zaten varsa
                raise ValidationError(_('Bu Seri Numaraya Sahip Cihaz Zaten Var'))
        return device_serial_number
    # device id kolonu unique olduğu için aynı device id ile kayıt yapılamaz.
    # Bunun için clean_device_id fonksiyonunu override ettik.
    def clean_device_id(self):
        device_id = self.cleaned_data.get('device_id')
        if device_id != self.instance.device_id: # Güncelleme yapılırken device_id değişmemişse
            if IHA.objects.filter(device_id=device_id).exists(): # Kayıt İşleminde device_id zaten varsa
                raise ValidationError(_('Bu ID Numarasına Sahip Cihaz Zaten Var')) 
        return device_id
    
    
    
    

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'parent': _('Üst Kategori'),
            'title': _('Kategori Adı'),
            'keywords': _('Anahtar Kelimeler'),
            'description': _('Kategori Açıklaması'),
            'image': _('Kategori Resmi'),
            'status': _('Kategori Durumu'),
        }
        exclude = ('slug',)
    def clean_category_name(self):
        category_name = self.cleaned_data.get('title')
        if category_name != self.instance.title: # Güncelleme yapılırken category_name değişmemişse
            if Category.objects.filter(title=category_name).exists(): # Kayıt İşleminde category_name zaten varsa
                raise ValidationError(_('Bu Kategori Zaten Var'))
        return category_name