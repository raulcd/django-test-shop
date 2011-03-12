# -*- coding: utf-8 -*-
from django import forms
from shop.models.owner_account_model import OwnerAccount
from shop.models.shop_model import Shop
import re

'''
Classes for forms. At first CreateOwnerForm is needed
'''
class CreateOwnerForm(forms.Form):
    store_name = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    def clean_store_name(self):
        data = self.cleaned_data['store_name']
        if Shop.objects.filter(name=data):
            raise forms.ValidationError("The shop name already exists")
        if not re.match(r'^[a-z]+$', data):
            raise forms.ValidationError("The shop name can only contain characters from a to z in lowercase")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        owner = OwnerAccount()
        owner.first_name = self.cleaned_data['first_name']
        owner.last_name =  self.cleaned_data['last_name']
        owner.email = data
        owner.validate_unique()
        return data
