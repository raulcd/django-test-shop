from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth import views as auth_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from shop.registration.forms import MyAuthenticationForm

urlpatterns = patterns('',
    url(r'^shop/thanks/$', 'shop.views.thanks'),
    url(r'^register/$', 'shop.registration.views.register',
        {'template_name': 'registration/registration_form.html'},
        name='registration_register'),
    url(r'^activate/(?P<activation_key>\w+)/$',
                           'shop.registration.views.activate',
                           name='registration_activate'),
    url(r'^register/complete/$', 'shop.registration.views.register_complete', name = 'registration_complete'),
    url(r'^admin/$', 'shop.views.logged', name='admin_login'),
    url(r'^accounts/login/$',
                           auth_views.login,
                           {'template_name': 'registration/login.html',
                            'authentication_form' : MyAuthenticationForm},
                           name='auth_login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}),
    url(r'^payment/', include('payments.urls')),
    url(r'^products/view/', 'shop.views.show_configured_products', name = 'show_products'),
    url(r'^products/add/', 'shop.views.add_products', name = 'add_products'),
    #(r'^accounts/', include('registration.urls')),

    # Examples:
    # url(r'^$', 'magna.views.home', name='home'),
    # url(r'^magna/', include('magna.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
