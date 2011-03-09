# -*- coding: utf-8 -*-
'''
All information for owners of shops is in this models file
'''

from django.db import models

class OwnerAccount(models.Model):
    '''
    The OwnerAccount with all data for the owner.
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_name

    class Meta:
        app_label = 'shop'
