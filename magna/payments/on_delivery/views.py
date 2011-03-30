from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms
from django.db import IntegrityError
from shop.models.shop_model import Shop
from payments.models import PaymentTypes, ShopPaymentTypes, PaymentProperties

ON_DELIVERY_NAME = "PAYMENT_ON_DELIVERY"

def payment(request):
    '''
    Do all what you need to do for on_delivery_payment
    '''
    return HttpResponse("This is my payment for payment_on_delivery stuff")

@login_required()
def configure(request, template_name='configure/on_delivery.html'):
    if request.method == 'POST':
        form = PaymentOnDeliveryForm(request.POST)
        if form.is_valid():
            shop = Shop.objects.get(owner=request.user)
            new_payment = form.save(shop)
            return HttpResponseRedirect(reverse('on_delivery_configure_complete'))
    else:
        form = PaymentOnDeliveryForm()
        shop = Shop.objects.get(owner=request.user)
        payment_type = PaymentTypes.objects.get(name=ON_DELIVERY_NAME)
        shop_payment_type = ShopPaymentTypes.objects.get(shop=shop, payment_type=payment_type)
        if shop_payment_type:
            payment_properties = PaymentProperties.objects.get(shop_payment_type=shop_payment_type)
            form.cost = payment_properties.value

    context = RequestContext(request)
    return render_to_response(template_name,
                              {'form': form},
                              context_instance=context)

def configure_complete(request):
    return HttpResponse("The configuration was successful")


class PaymentOnDeliveryForm(forms.Form):
    cost = forms.CharField(max_length=30)

    def clean_cost(self):
        data = self.cleaned_data['cost']
        try:
            i = float(data)
        except ValueError:
            raise forms.ValidationError(u'The cost should be a number')
        return data

    def save(self, shop):
        payment_type = PaymentTypes.objects.get(name=ON_DELIVERY_NAME)
        shop_payment_type = ShopPaymentTypes.objects.get(shop=shop, payment_type=payment_type)
        if not shop_payment_type:
            shop_payment_type = ShopPaymentTypes(shop=shop, payment_type=payment_type)
            shop_payment_type.save()
            payment_properties = PaymentProperties(shop_payment_type=shop_payment_type, key='cost', value=self.cleaned_data['cost'])
        else:
            payment_properties = PaymentProperties.objects.get(shop_payment_type=shop_payment_type)
            payment_properties.value=self.cleaned_data['cost']
        payment_properties.save()