from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
# Django Password Reset için kullanılır
from django.contrib.auth import views as auth_views 
urlpatterns = [
    # Django dil secenekleri için /tr/ veya /en/ gibi bir url ekler
    path('i18n/', include('django.conf.urls.i18n')),
    # Admin paneli için
    path('admin/', admin.site.urls),
    # Api urls
    path('api/', include("iha_api.api.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    
    # Pass Reset
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='pass_reset/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="pass_reset/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='pass_reset/password_reset_complete.html'), name='password_reset_complete'),
    
    # My apps urls
    path('user/', include('user_app.urls')),
    path('', include('iha_app.urls')),
]

