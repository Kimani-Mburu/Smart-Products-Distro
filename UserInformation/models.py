from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
# Create your models here.
class Farmer(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    national_id = models.IntegerField(null = False, blank = False)
    phone_no = PhoneNumberField(blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
# Vendors profile

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    national_id = models.IntegerField(null = False, blank = False)
    phone_no = PhoneNumberField(blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

