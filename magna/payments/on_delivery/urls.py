
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    url(r'^pay/$', 'payments.on_delivery.views.payment'),
    url(r'^configure/$', 'payments.on_delivery.views.configure'),
    url(r'^configure/succeed/$', 'payments.on_delivery.views.configure_complete', name = 'on_delivery_configure_complete'),
)