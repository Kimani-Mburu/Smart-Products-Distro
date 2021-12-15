from django.contrib import admin
from .models import OtherCharge, Order, Order_item, OrderOtherCharge, PurchaseOrder


admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(OtherCharge)
admin.site.register(PurchaseOrder)
admin.site.register(OrderOtherCharge)