from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

# Model Class
from .models import *

# Kullanıcı ekleme için kullanılacak Django Model Form Class
class UserCustomForm(forms.ModelForm):
    """
    Model Haricinde alanlar eklemek için kullanilmiştir
    Name, Surname, Email, Password1, Password2 alanlari User modelinde mevcut 
    """
    name = forms.CharField(max_length=30, label= _("İsim Girin") ,help_text='')
    surname = forms.CharField(max_length=30, label= _("Soyisim Girin") ,help_text='')
    email = forms.EmailField(max_length=100,label= _("Email adresiniz"), help_text='')
    password1 = forms.CharField(label=_('Parola'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Paralo Doğrulama"), widget=forms.PasswordInput, help_text=' ')

    class Meta:
        model = UserCustomModel
        fields = ('name', 'surname','email','user_phone','password1', 'password2',)
        read_only_fields = ('created_user',)
        # Model deki alanlarin label ve help_text degerlerini degistirmek icin
        labels = {
            'username': _('Kullanıcı Adı'),
            'email': _('E-Posta'),
            'password1': _('Şifre'),
            'password2': _('Şifre Doğrulama'),
            'user_phone': _('Telefon'),
            'user_country': _('Ülke'),
            'user_city': _('Şehir'),
            'user_address': _('Adres'),
            'user_postal_code': _('Posta Kodu'),
            'user_company': _('Şirket'),
        }
    # formdan yapılan istekleri database kaydetmeden önce burada kontrol ediyoruz.
    # Email alanı aynı zamanda username alanı olduğu için bu alanı kontrol ediyoruz.
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError(_("Bu mail adresi zaten kullanılmakta..."))
        return data
    # password1 ve password2 alanlarının aynı olup olmadığını kontrol ediyoruz.
    # password1 ve password2 alanlarının uyuşmadığı taktirde kullanıcıya hata mesajı dondürür.
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Parolalar uyuşmuyor..."))
        if len(password1) < 5:
            raise ValidationError(_("Parola en az 5 karakter olmalı..."))
        return password2

    def save(self,commit=True):
        instance = super(UserCustomForm, self).save(commit=False)
        if commit:
            # 
            user = User.objects.create_user(
                username=self.cleaned_data['email'],
                email=self.cleaned_data['email'],
                first_name = self.cleaned_data['name'],
                last_name = self.cleaned_data['surname'],
                password=self.cleaned_data['password1'],
                is_active = True,
                is_staff = False,
                is_superuser = False,
            )
            instance.user = user
            instance.user_phone = self.cleaned_data['user_phone']
            instance.save()
        return instance