from django.shortcuts import render_to_response


def thanks(request):
    return render_to_response('shop/thanks.html', {})
