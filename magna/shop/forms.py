# -*- coding: utf-8 -*-
from django import forms

'''
Classes for forms. At first CreateOwnerForm is needed
'''
class CreateOwnerForm(forms.Form):
    store_name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
