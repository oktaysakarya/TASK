from django.urls import path
from .views import *

app_name = 'user_app' 
urlpatterns = [
    path('login/', login_, name='login_'),
    path('logout/', logout_, name='logout'),
    path('register/', register, name='register'),
]