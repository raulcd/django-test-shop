# -*- coding: utf-8 -*-
from shop.models.shop_model import Shop

__author__ = 'raulcd'

from django.db import models

class Product(models.Model):
    """
    Product data. Main model for items in the stores
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    shop = models.ForeignKey(Shop)
    
    class Meta:
        app_label = 'shop'