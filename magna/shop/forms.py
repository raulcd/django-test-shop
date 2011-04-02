import re
from django import forms
from shop.models.product_model import Product
from shop.models.shop_model import Shop


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=12, decimal_places=2)

    def clean_name(self):
        data = self.cleaned_data['name']
        #TODO modify regular expression to match also uppercase spaces and other symbols
        if not re.match(r'^[a-z]+$', data):
            raise forms.ValidationError(u'The name of the products can only contain characters from a to z in lowercase')
        return data

    def save(self, user):
        new_product = Product()
        new_product.name = self.cleaned_data['name']
        new_product.description = self.cleaned_data['description']
        new_product.price = self.cleaned_data['price']
        new_product.shop = Shop.objects.get(owner__id=user.id)
        new_product.save()
        return new_product