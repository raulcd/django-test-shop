# -*- coding: utf-8 -*-
from django.db import models
from shop.models.owner_account_model import OwnerAccount


class Shop(models.Model):
    name = models.CharField(max_length=30, unique=True)
    owner = models.ForeignKey(OwnerAccount)

    class Meta:
        app_label = 'shop'
