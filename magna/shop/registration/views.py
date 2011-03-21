from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from registration.models import RegistrationProfile
from shop.registration.forms import RegistrationShopForm

__author__ = 'raulcd'

def register(request, template_name = 'registration/registration_form.html'):
    if request.method == 'POST':
        form = RegistrationShopForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # success_url needs to be dynamically generated here; setting a
            # a default value using reverse() will cause circular-import
            # problems with the default URLConf for this application, which
            # imports this file.
            return HttpResponseRedirect(reverse('registration_complete'))
    else:
        form = RegistrationShopForm()

    context = RequestContext(request)
    return render_to_response(template_name,
                              {'form': form},
                              context_instance=context)

def activate(request, activation_key):
    activation_key = activation_key.lower() # Normalize before trying anything with it.
    account = RegistrationProfile.objects.activate_user(activation_key)
    return render_to_response('shop/thanks.html',
                              { 'account': account,
                                'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS})
    #TODO Activation account when new account is setted

def register_complete(request):
    return render_to_response('shop/thanks.html')
  