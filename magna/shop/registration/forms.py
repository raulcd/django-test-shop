import re
from django.contrib.auth.models import User
from registration.models import RegistrationProfile
from django import forms
from shop.models.shop_model import Shop

__author__ = 'raulcd'

class RegistrationShopForm(forms.Form):
    '''
        This form will be used to create a new registration for a shop. As we just need an email, password and shop name to register. We
        override the RegistrationForm from django-registration (they have a user name also)
       '''
    store_name = forms.CharField(max_length=30)
    email = forms.EmailField(label=(u'Your email address'))
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=(u'Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=(u'Password (again)'))

    def clean_store_name(self):
        data = self.cleaned_data['store_name']
        if Shop.objects.filter(name=data):
            raise forms.ValidationError(u'The shop name already exists')
        if not re.match(r'^[a-z]+$', data):
            raise forms.ValidationError(u'The shop name can only contain characters from a to z in lowercase')
        return data

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(
                (u'This email address is already in use. Please supply a different email address.'))
        return self.cleaned_data['email']

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError((u'You must type the same password'))
        return self.cleaned_data

    def save(self, profile_callback=None):
        """
        This method is overrided from the registrationForm in django-registration.
        It Create the new ``User`` and ``RegistrationProfile``, and
        returns the ``User``.

        This is essentially a light wrapper around
        ``RegistrationProfile.objects.create_inactive_user()``,
        feeding it the form data and a profile callback (see the
        documentation on ``create_inactive_user()`` for details) if
        supplied.

        """
        new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['email'],
                                                                    password=self.cleaned_data['password1'],
                                                                    email=self.cleaned_data['email'],
                                                                    profile_callback=profile_callback)
        shop = Shop()
        shop.name = self.cleaned_data['store_name']
        shop.owner = new_user
        shop.save()
        return new_user
