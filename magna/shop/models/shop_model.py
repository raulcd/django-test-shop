# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User)

    class Meta:
        app_label = 'shop'
