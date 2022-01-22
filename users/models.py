from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from datetime import datetime
from django.urls import reverse
import geocoder

# token


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    # terms_check = models.BooleanField("I have read the Terms & Conditions", default=False, blank=False)

    def __str__(self):
        return self.first_name
