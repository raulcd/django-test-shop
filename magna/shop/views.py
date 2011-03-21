from datetime import timedelta
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from shop.models.shop_model import Shop


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