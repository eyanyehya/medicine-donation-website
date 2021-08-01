from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from django.urls import reverse
import geocoder

# token
mapbox_access_token = 'pk.eyJ1IjoiZXlhbnllaHlhIiwiYSI6ImNrcm5uem9kOTB5cW0yc252M3AxN2drNzMifQ.IIwBFoL3ox2l3rOwsvZe_w'


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=200, default='', null=True, blank=True)

    def __str__(self):
        return self.first_name
