from django import forms
from django.forms import ModelForm, fields
from .models import Product


class ProductsAdd(forms.ModelForm):
    class Meta:
       model = Product
       exclude = ('is_featured','created_on','farmer')
       
