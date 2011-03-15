from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^shop/$', 'shop.views.create_shop'),
    url(r'^shop/thanks/$', 'shop.views.thanks'),
    url(r'^register/$', 'shop.registration.views.register',
        {'template_name': 'registration/registration_form.html'},
        name='registration_register'),
    url(r'^activate/(?P<activation_key>\w+)/$',
                           'shop.registration.views.activate',
                           name='registration_activate'),
    url(r'^register/complete/$', 'shop.registration.views.register_complete', name = 'registration_complete')
    #(r'^accounts/', include('registration.urls')),

    # Examples:
    # url(r'^$', 'magna.views.home', name='home'),
    # url(r'^magna/', include('magna.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
