from django.urls import path
from .views import *

app_name = 'IHA'
urlpatterns = [
    path('', index, name='index'),
    path('iha-list/', iha_list, name='iha_list'),
    path('iha-create/', add_new_iha, name='add_new_iha'),
    path('iha-update/<int:id>', update_iha, name='update_iha'),
    path('iha-delete/<int:id>', delete_iha, name='delete_iha'),
    path('add-new-category/', add_new_category, name='add_new_category'),

]