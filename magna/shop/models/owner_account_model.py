# -*- coding: utf-8 -*-
'''
All information for owners of shops is in this models file
'''

from django.db import models
from shop.models import Shop

class OwnerAccount(models.Model):
    '''
    The OwnerAccount for the specified Shop. It has a ForeignKey for a Shop.
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    shop = models.ForeignKey(Shop)

    class Meta:
        app_label = 'shop'
