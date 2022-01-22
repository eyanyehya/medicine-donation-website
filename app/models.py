from datetime import datetime
from django.db import models
from django import forms
from django.urls import reverse
import geocoder
from django.conf import settings
from django import forms
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

# token
google_maps_access_token = 'AIzaSyDONGu-q34eWXxxV_eS4wpaT5RpB4kHyZk'


# Create your models here.
class MedicinePost(models.Model):
    medicine_name = models.CharField(max_length=200, default='')
    medicine_quantity = models.IntegerField()
    # expiry_date = models.DateField('Expiry Date', blank=True, null=True)
    # expiry_date = models.CharField(max_length=200, default='')
    expiry_date = models.CharField('Expiry Date', blank=True, null=True, max_length=200)
    post_date_time = models.DateTimeField(default=datetime.now, blank=True)
    # medicine_image = models.ImageField(upload_to='images/', blank=False)
    medicine_image = CloudinaryField('image')
    phone_number = PhoneNumberField(null=False, blank=False)
    extra_info = models.TextField(null=True, blank=True)


    POST_CHOICES = (
        ('', 'Select Post Type'),
        ('Donate', 'Donation'),
        ('Receive', 'Request')
    )
    post_type = models.CharField(max_length=20, choices=POST_CHOICES)

    widgets = {
        'post_type': forms.Select(attrs={'class': 'bootstrap-select'}),
    }

    # MAPBOX STUFF
    address = models.TextField(default="")
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.google(self.address, key=google_maps_access_token)
        g = g.latlng  # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(MedicinePost, self).save(*args, **kwargs)

    # author = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, default='')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )

    def __str__(self):
        return self.medicine_name

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
