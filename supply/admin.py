from django.contrib import admin
from .models import  PurchaseOrder, Payment

admin.site.register(PurchaseOrder)
admin.site.register(Payment)