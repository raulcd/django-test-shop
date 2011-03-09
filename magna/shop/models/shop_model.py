# -*- coding: utf-8 -*-
from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        app_label = 'shop'
