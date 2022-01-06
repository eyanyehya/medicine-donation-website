from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset
from django import forms

from .models import MedicinePost


class DateInput(forms.DateInput):
    input_type = 'date'


class MedicineForm(forms.ModelForm):
    class Meta:
        model = MedicinePost
        fields = ('address', 'medicine_name', 'medicine_quantity', 'expiry_date', 'medicine_image', 'post_type',
                  'phone_number', 'extra_info')
        widgets = {'expiry_date': DateInput(attrs={'placeholder': 'Expiry Date'}),
                   'extra_info': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'placeholder': 'Write any extra '
                                                                                             'information (Optional) '}),
                   'medicine_name': forms.TextInput(attrs={'placeholder': 'Medicine Name'}),
                   'medicine_quantity': forms.NumberInput(attrs={'placeholder': 'Medicine Quantity'}),
                   'phone_number': forms.NumberInput(attrs={'placeholder': 'Phone Number'}),
                   'medicine_image': forms.FileInput(attrs={'placeholder': 'IS THIS WOKRING'}),
                   }

    _placeholders = {
        'fieldname': 'fieldname placeholder',
    }

    def __init__(self, *args, **kwargs):
        super(MedicineForm, self).__init__(*args, **kwargs)
        self.fields['extra_info'].label = "Extra Info (Optional)"
        self.fields['expiry_date'].label = "Expiry Date (If Donating)"
        self.fields['address'].required = True

        self.helper = FormHelper()
        self.helper.form_show_labels = False


class EditPostForm(forms.ModelForm):
    medicine_name = forms.CharField()

    class Meta:
        model = MedicinePost
        fields = ('address', 'medicine_name', 'medicine_quantity', 'expiry_date', 'medicine_image', 'post_type',
                  'phone_number', 'extra_info')

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
