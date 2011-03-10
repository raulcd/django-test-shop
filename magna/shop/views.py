from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from shop.forms import CreateOwnerForm
from django.core.urlresolvers import reverse

def create_shop(request):
    # TODO: Error control
    # View if the method is POST and the form is valid has data attached
    if request.method == 'POST':
        form = CreateOwnerForm(request.POST)
        if form.is_valid():
            # We need to do something with the data
            return HttpResponseRedirect(reverse('shop.views.thanks'))
    else:
        # The methos is not POST and is not correct
        form = CreateOwnerForm()
    # The method is not correct or the Form is not valid. We show the form
    return render_to_response('shop/create_shop.html', { 'form' : form })

def thanks(request):
    return render_to_response('shop/thanks.html', {})
