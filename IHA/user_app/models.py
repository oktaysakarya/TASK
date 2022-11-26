from django.db import models
from django.contrib.auth.models import  User 
# Create your models here.

class UserCustomModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    user_phone = models.CharField(max_length=50, blank=True, null=True)
    user_country = models.CharField(max_length=50, blank=True, null=True)
    user_city = models.CharField(max_length=50, blank=True, null=True)
    user_address = models.CharField(max_length=50, blank=True, null=True)
    user_postal_code = models.CharField(max_length=50, blank=True, null=True)
    user_company = models.CharField(max_length=50, blank=True, null=True)
    created_user = models.DateTimeField("Kullanıcı oluşturma Tarihi",auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'
        ordering = ['-created_user']

class FaturaModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_fatura')
    fatura_no = models.CharField(max_length=50, blank=True, null=True)
    fatura_tutar = models.CharField(max_length=50, blank=True, null=True)
    fatura_durum = models.CharField(max_length=50, blank=True, null=True)
    created_fatura = models.DateTimeField("Fatura oluşturma Tarihi",auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = 'Fatura'
        verbose_name_plural = 'Fatura'
        ordering = ['-created_fatura']