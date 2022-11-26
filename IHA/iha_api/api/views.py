"""
    ! ------------------ Projenin Api kismi için gerekli olan viewset ------------------
    * Yazar : Oktay SAKARYA
    * Tarih : 25.11.2022 21:39 
    * Proje : IHA Bitimine 01 gün 12 saat 34 dakika 56 saniye
    

# Rest framework GenericViewSet kullanilmistir.
# APi için gerekli olan viewsetler burada tanimlanir.
# Her bir viewset için gerekli olan serializer, queryset, permission, authentication tanimlanir.
# Bu viewsetlerin url tanimlamalari IHA/iha_api/api/urls.py dosyasinda yapilmistir.
! Bütün viewsetler permissionlari is_authenticated olup, authentication olarak ise TokenAuthentication kullanilmistir.
! Bütün viewsetler mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
! mixins.UpdateModelMixin, mixins.DestroyModelMixin mixinslerden kalilitim almaktadir.
! GET, POST, PUT, PATCH, DELETE methodlari kullanilabilir.
   ----------------------------------------------------------------------------------------
"""

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import status
# Serializers
from .serializers import *
# Models
from user_app.models import *
from iha_app.models import *

class UserViewSet(
    mixins.RetrieveModelMixin, # GET
    mixins.UpdateModelMixin,   # PUT, PATCH
    mixins.ListModelMixin,     # GET
    mixins.DestroyModelMixin,  # DELETE
    mixins.CreateModelMixin,   # POST
    GenericViewSet             # GenericViewSet
    ):
    lookup_field = 'id'
    queryset = UserCustomModel.objects.all()
    serializer_class = UserCustomSerializer # ! Her bir viewset için gerekli olan serializer class tanimlanir.
    permission_classes = [IsAuthenticated] # ! Her bir viewset için gerekli olan permission tanimlanir.
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:  # ! Eger kullanici admin ise tum userlari getirir.
            return super().get_queryset(*args, **kwargs).all()
        elif self.request.user.is_active and not self.request.user.is_superuser: # ! Eger kullanici admin degilse sadece kendisini getirir.
            return super().get_queryset(*args, **kwargs).filter(
                user = self.request.user
            ) 
        return None 

class IHAViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    lookup_field = 'device_id'
    queryset = IHA.objects.all()
    serializer_class = IHASerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    lookup_field = 'title'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]