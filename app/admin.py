from django.contrib import admin
from .models import HaveMedicinePost, NeedMedicinePost


# Register your models here.
admin.site.register(HaveMedicinePost)
admin.site.register(NeedMedicinePost)

