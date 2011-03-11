#-*- coding: utf-8 -*-
from django.utils import unittest
from django.test import TestCase
from shop.views import create_shop
from django.test.client import Client
from shop.forms import CreateOwnerForm


class CreateShopTestCase(TestCase):

    def test_01_submit_form_without_data(self):
        response = self.client.get('/shop/')
        self.assertEquals(response.status_code, 200)
        response = self.client.post('/shop/', {})
        self.assertContains(response, 'This field is required', status_code=200,
                            count=4)

    def test_02_submit_form_with_correct_data(self):
        response = self.client.post('/shop/', {'store_name' : 'mystore',
                                               'first_name' : 'My name',
                                               'last_name' : 'My Last Name',
                                               'email' : 'mymail@mymail.com' })
        self.assertContains(response, 'This field is required', count = 0,
                            status_code = 302)

    def test_03_submit_form_with_incorrect_emai(self):
        response = self.client.post('/shop/', {'store_name' : 'mystore',
                                               'first_name' : 'My name',
                                               'last_name' : 'My Last Name',
                                               'email' : 'mymailmymail.com' })
        self.assertContains(response, 'Enter a valid e-mail address', count=1, status_code=200)
        self.assertContains(response, 'This field is required', count=0, status_code=200)

    def test_04_submit_form_with_incorrect_shop_store(self):
        response = self.client.post('/shop/', {'store_name' : 'mystore has to fail',
                                               'first_name' : 'My name',
                                               'last_name' : 'My Last Name',
                                               'email ': 'mymail@mymail.com' })
        self.assertContains(response, 'This field is required', count=0)
        self.assertContains(response, 'The shop name can only contain characters from a to z in lowercase', count=1)

    def test_05_get_thanks_template(self):
        response = self.client.get('/shop/thanks/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/thanks.html')
