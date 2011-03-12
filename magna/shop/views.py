from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from shop.forms import CreateOwnerForm
from shop.models.owner_account_model import OwnerAccount
from shop.models.shop_model import Shop
from django.core.urlresolvers import reverse

def create_shop(request):
    # View if the method is POST and the form is valid has data attached
    if request.method == 'POST':
        form = CreateOwnerForm(request.POST)
        if form.is_valid():
            owner = OwnerAccount()
            owner.first_name = form.cleaned_data['first_name']
            owner.last_name = form.cleaned_data['last_name']
            owner.email = form.cleaned_data['email']
            owner.save()
            shop = Shop()
            shop.owner = owner
            shop.name = form.cleaned_data['store_name']
            shop.save()
            # We need to do something with the data
            return HttpResponseRedirect(reverse('shop.views.thanks'))
    else:
        # The methos is not POST and is not correct
        form = CreateOwnerForm()
    # The method is not correct or the Form is not valid. We show the form
    return render_to_response('shop/create_shop.html', { 'form' : form })

def thanks(request):
    return render_to_response('shop/thanks.html', {})
