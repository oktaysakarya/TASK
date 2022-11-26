from django.contrib import admin

# Register your models here.
from django.contrib.auth.models  import  Group
from .models import *
from user_app.models import *

admin.site.site_header = "IHA Admin Paneli"
admin.site.site_title  = "IHA Admin Paneli"
admin.site.index_title = "IHA Admin Paneli"

admin.site.unregister(Group)  # Admin panelinden Group modelini kaldırıyoruz.

admin.site.register(UserCustomModel)
admin.site.register(Category)
admin.site.register(IHA)
admin.site.register(Images)