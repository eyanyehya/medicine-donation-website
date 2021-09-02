from datetime import datetime
from django.db import models
from django.urls import reverse
import geocoder
from django.conf import settings
from django import forms
from django.contrib.auth import get_user_model

# token
google_maps_access_token = 'AIzaSyDONGu-q34eWXxxV_eS4wpaT5RpB4kHyZk'


# Create your models here.
class MedicinePost(models.Model):
    medicine_name = models.CharField(max_length=200, default='')
    medicine_quantity = models.IntegerField()
    expiry_date = models.DateField('Expiry Date', blank=True, null=True)
    post_date_time = models.DateTimeField(default=datetime.now, blank=True)
    medicine_image = models.ImageField(upload_to='images/', default='/logo.png', blank=True, null=True)
    phone_number = models.CharField(max_length=200, default='')

    POST_CHOICES = (
        ('Donate', 'Donate'),
        ('Receive', 'Receive')
    )
    post_type = models.CharField(max_length=20, choices=POST_CHOICES, default="JANUARY")

    widgets = {
        'post_type': forms.Select(attrs={'class': 'bootstrap-select'}),
    }

    # MAPBOX STUFF
    address = models.TextField(default='')
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
