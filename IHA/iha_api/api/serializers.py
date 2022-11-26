"""
    ! ------------------ Projenin Api kismi için gerekli olan serializerlar ------------------
    * Yazar : Oktay SAKARYA
    * Tarih : 25.11.2022 21:39 
    * Proje : IHA Bitimine 01 gün 12 saat 34 dakika 56 saniye
    
Projede kullanilacak olan serializerlar burada tanimlanir.
Rest framework Model Serializer kullanilmistir.
User modeli için UserSerializer, 
UserCustomModel için UserCustomSerializer, 
IHA için IHASerializer, Category için CategorySerializer, tanimlanmiştir.
    ----------------------------------------------------------------------------------------
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from user_app.models import UserCustomModel
from iha_app.models import IHA,Category, Images


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','is_active','last_login','date_joined']
        read_only_fields = ['email','is_active','last_login','date_joined']

class UserCustomSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only = True)
    class Meta:
        model = UserCustomModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IHASerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    class Meta:
        model = IHA
        fields = '__all__'