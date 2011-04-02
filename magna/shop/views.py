from datetime import timedelta
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from shop.models.shop_model import Shop
from shop.models.product_model import  Product
from shop.forms import ProductForm


def thanks(request):
    return render_to_response('shop/thanks.html', {})

@login_required()
def logged(request):
    if not request.user.is_active:
        last_activation_date = request.user.date_joined + timedelta(settings.ACCOUNT_ACTIVATION_DAYS)
        return HttpResponse("This is a logged page. You have until %s/%s/%s to activate your account. Your store is %s" %
                            (last_activation_date.day, last_activation_date.month, last_activation_date.year, Shop.objects.get(owner__id=request.user.id).name))
    else:
        return HttpResponse("This is a logged page. You are already an active user.")


@login_required()
def add_products(request, template_name='shop/add_products.html'):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('show_products'))
    else:
        form = ProductForm()
        
    context = RequestContext(request)
    return render_to_response(template_name,
                              {'form': form},
                              context_instance=context)

@login_required()
def show_configured_products(request):
    request.session.set_expiry(0)
    products = Product.objects.filter(shop__owner__id=request.user.id)
    return render_to_response('shop/products.html', {'products' : products})