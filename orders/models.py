from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
from django.db.models.deletion import CASCADE
from datetime import date, datetime

from UserInformation.models import Customer
from products.models import Product


class OtherCharge(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    rate = models.FloatField(default='0')
    
    def __str__(self):
        return self.name
 
   
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateTimeField(default=datetime.now)
    reference_no = models.CharField(max_length=12, null=True, blank=True)
    vendor_id = models.ForeignKey(Customer, on_delete=CASCADE)
    delivery_address = models.CharField(max_length=30, verbose_name='Delivery Address')
    
    def save(self, *args, **kwargs):
        if self.reference_no is None:
            uuid = str(uuid4())

            ref_no = uuid.split('-')[0].upper()
            self.reference_no = ref_no
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.reference_no)
    
class Order_item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=CASCADE)
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    total_cost = models.FloatField()
    
    def __str__(self):
        return f"{self.order_id}"
    
class OrderOtherCharge(models.Model):
    order_id = models.ForeignKey(Order, on_delete=CASCADE)
    other_Charges = models.ForeignKey(OtherCharge, on_delete=CASCADE)
    order_charges_total_price = models.IntegerField()
    
    def save(self, rate, *args, **kwargs):
        total = str(rate)  
        self.order_charges_total_price = total
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_charges_total_price

STATUS = (
    ('Shipped','Shipped'), ('Canceled','Canceled'), ('On-route','On-route'),('Delivered','Delivered'))        
class PurchaseOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=CASCADE, related_name='purchase_orders')
    other_Charges = models.ForeignKey(OrderOtherCharge, on_delete=CASCADE)
    date = models.DateField(default=date.today)
    total_value = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS)
    
    def __str__(self):
        return f'{self.id}, {self.total_value}'
