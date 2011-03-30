from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    url(r'^on_delivery/', include('payments.on_delivery.urls')),
)