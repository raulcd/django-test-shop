# -*- coding: utf-8 -*-
from django import forms
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
        if not re.match(r'^[a-z]+$', data):
            raise forms.ValidationError("The shop name can only contain characters from a to z in lowercase")
        return data
