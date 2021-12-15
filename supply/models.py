from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.shortcuts import reverse
from django.utils import timezone
from datetime import date, datetime
from django.utils.text import slugify
from django.contrib.auth.models import User


from uuid import uuid4

from UserInformation.models import Customer
from orders.models import Order, OtherCharge
from products.models import Product






   
STATUS = (
    ('Shipped','Shipped'), ('Canceled','Canceled'), ('On-route','On-route'),('Delivered','Delivered'))        
class PurchaseOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=CASCADE)
    other_Charges = models.ForeignKey(OtherCharge, on_delete=CASCADE)
    date = models.DateField(default=date.today)
    total_value = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS)
    
    def __str__(self):
        return f'{self.id}, {self.total_value}'

PAY = (('M-pesa','M-pesa'),('Cash','Cash'))
class Payment(models.Model):
    mode = models.CharField(max_length=10, choices=PAY)
    total_amount = models.FloatField()
    order_id = models.ForeignKey(Order, on_delete=CASCADE)
    ref = models.CharField(max_length=10)
    
    def save(self, *args, **kwargs):
        if self.ref is None:
            uuid = str(uuid4())

            ref_no = uuid.split('-')[0].upper()
            self.ref = ref_no
            super().save(*args, **kwargs)