from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe
from django.utils.text import slugify
# Create your models here.
class Category(MPTTModel):
    STATUS = (
        ('True', 'Aktif'),
        ('False','Pasif'),
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):                           
        full_path = [self.title]           
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
    
    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(Category, self).save(*args, **kwargs)

    def get_uniqe_slug(self):
        slug = slugify(self.title + "-" + self.keywords).replace("ı", "i")
        uniqe_slug = slug
        counter = 1
        while Category.objects.filter(slug=uniqe_slug).exists():
            uniqe_slug = "{}-{}".format(slug, counter)
            counter += 1
        return uniqe_slug

class IHA(models.Model):
    STATE=(
        ('Available','Müsait'),
        ('Unavailable','Kullanım Dışı'),
        ('Faulted','Hatalı')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_iha") #many to one relation with Category
    device_serial_number = models.CharField(max_length=50, unique=True)
    device_id = models.CharField(max_length=50, unique=True)
    device_name = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50)
    device_status = models.CharField(
                    default='Available',
                    max_length=50,
                    choices=STATE,
                    verbose_name='Durum',
                    null=True,
                    blank=True
                    )
    device_image = models.ImageField("Cihazın Resmini Yükleyin",upload_to='images/iha', blank=True, null=True)
    device_weight = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0), MaxValueValidator(99999.0)],
    )
    device_ammo_capacity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)],
        default=0
    )
    device_ammo_level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0
    )
    device_fuel_capacity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)],
        default=0
    )
    device_fuel_level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0
    )
    # Battery pack capacity
    device_battery_capacity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999)],
        default=0
    )
    # Battery pack level
    device_battery_level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0
    )
    # iha flying range
    device_flying_range = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(99999.0)],
        default=0
    )
    # iha flying speed
    device_flying_speed = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(99999.0)],
        default=0
    )
    # iha flying altitude
    device_flying_altitude = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(99999.0)],
        default=0
    )
    created_iha = models.DateTimeField("Eklenme Tarihi",auto_now_add= True,blank=True)

    def __str__(self):
        return f"IHA: {self.device_id} {self.device_name} {self.device_type}"    
    def image_tag(self):
        if self.device_image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.device_image.url))
        else:
            return ""
    class Meta:
        verbose_name_plural = 'IHA'
        ordering = ['-created_iha']

class Images(models.Model):
    product=models.ForeignKey(IHA,on_delete=models.CASCADE, related_name="images")
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/iha')
    def __str__(self):
        return self.title
    