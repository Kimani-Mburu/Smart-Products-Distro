from django.contrib import admin
from .models import OtherCharge, Order, Order_item, Order_other_charge, PurchaseOrder, Payment


admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(OtherCharge)
admin.site.register(Order_other_charge)
admin.site.register(Payment)
admin.site.register(PurchaseOrder)