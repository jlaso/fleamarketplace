from django.db import models
import datetime

class Sheriff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    nick = models.CharField(max_length=10)
    #market =
    schedule = models.CharField(max_length=30)

class Market(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Product(models.Model):
    CONDITION = (
        ('new', 'New'),
        ('needs', 'needs repair'),
        ('good', 'good'),
    )
    market = models.ForeignKey(Market)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    condition = models.CharField(max_length=5, choices=CONDITION)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    sold = models.DateTimeField(default=None, null=True, blank=True)