from django import forms
from .models import MedicinePost


class MedicineForm(forms.ModelForm):
    class Meta:
        model = MedicinePost
        fields = ['address', 'medicine_name', 'medicine_quantity', 'expiry_date', 'medicine_image', 'post_type']
