from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('user',UserViewSet, basename='UserViewSet')
router.register('category',CategoryViewSet, basename='CategoryViewSet')
router.register('iha',IHAViewSet, basename='IHAViewSet')
urlpatterns = [
    path('',include(router.urls), name='api'),
]