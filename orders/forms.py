from django import forms
from django.forms import ModelForm,fields

from .models import Order

class DeliverAddress(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('delivery_address',)