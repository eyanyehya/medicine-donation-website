from crispy_forms.bootstrap import PrependedText
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import HiddenInput

from .models import CustomUser
from django.utils.safestring import mark_safe

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django.contrib.auth.models import User
from app import models


class CustomUserCreationForm(UserCreationForm):
    # password1 = forms.CharField(
    #     label="Password",
    #     widget=forms.PasswordInput(
    #         attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    # )
    # password2 = forms.CharField(
    #     label="Confirm password",
    #     widget=forms.PasswordInput(
    #         attrs={'class': 'form-control', 'type': 'password', 'align': 'center', 'placeholder': 'password'}),
    # )
    terms_check = forms.BooleanField(required=True, label=mark_safe('I have read and agree to Medonations <a '
                                                                    'href="/terms" '
                                                                    'target="_blank">Terms Of Service</a>'))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        help_texts = {
            'username': "Letters, digits and @/./+/-/_ only."
        }
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'terms_check', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Phone Number'}),
        }

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        Field('terms_check', type="hidden")
        self.fields['username'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['email'].label = ""
        self.fields['phone_number'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""








        # self.fields['username'].widget = HiddenInput()
        # self.helper = FormHelper()
        # self.helper.layout.

        # self.helper.form_show_labels = False

    # class Meta(UserCreationForm.Meta):
    #     model = CustomUser
    #     fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password')
    #     widgets = {
    #         'username': forms.TextInput(attrs={'placeholder': 'Username'}),
    #         'password': forms.PasswordInput(),
    #         'first_name': forms.TextInput(attrs={'label': 'First Name'}),
    #         'last_name': forms.TextInput(attrs={'label': 'Last Name'}),
    #         'email': forms.TextInput(attrs={'placeholder': 'Email'}),
    #         'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
    #     }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
