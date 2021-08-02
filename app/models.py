from datetime import datetime
from django.db import models
from django.urls import reverse
import geocoder
from django.conf import settings

# token
mapbox_access_token = 'pk.eyJ1IjoiZXlhbnllaHlhIiwiYSI6ImNrcm5uem9kOTB5cW0yc252M3AxN2drNzMifQ.IIwBFoL3ox2l3rOwsvZe_w'


# Create your models here.
class HaveMedicinePost(models.Model):
    medicine_name = models.CharField(max_length=200, default='')
    medicine_quantity = models.IntegerField()
    expiry_date = models.DateField()
    post_date_time = models.DateTimeField(default=datetime.now, blank=True)
    medicine_image = models.ImageField(upload_to='.static/images', blank=True, null=True)


    # MAPBOX STUFF
    address = models.TextField(default='')
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(HaveMedicinePost, self).save(*args, **kwargs)

    author = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, default='')

    def __str__(self):
        return self.medicine_name


class NeedMedicinePost(models.Model):
    medicine_name = models.CharField(max_length=200, default='')
    medicine_quantity = models.IntegerField()
    post_date_time = models.DateTimeField(default=datetime.now, blank=True)

    # MAPBOX STUFF
    address = models.TextField(default='')
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(NeedMedicinePost, self).save(*args, **kwargs)

    author = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, default='')

    def __str__(self):
        return self.medicine_name
