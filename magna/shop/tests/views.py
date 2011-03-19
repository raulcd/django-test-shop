#-*- coding: utf-8 -*-
from django.utils import unittest
from django.test import TestCase
from django.test.client import Client


class CreateShopTestCase(TestCase):

    def test_01_submit_form_without_data(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)
        response = self.client.post('/register/', {})
        self.assertContains(response, 'This field is required', status_code=200,
                            count=4)

    def test_02_submit_form_with_correct_data(self):
        response = self.client.post('/register/', {'store_name' : 'mystore',
                                               'password1' : 'apasswd',
                                               'password2' : 'apasswd',
                                               'email' : 'mymail@mymail.com' })
        self.assertContains(response, 'This field is required', count = 0,
                            status_code = 302)

    def test_03_submit_form_with_incorrect_email(self):
        response = self.client.post('/register/', {'store_name' : 'mystore',
                                               'password1' : 'apasswd',
                                               'password2' : 'apasswd',
                                               'email' : 'mymailmymail.com' })
        self.assertContains(response, 'Enter a valid e-mail address', count=1, status_code=200)
        self.assertContains(response, 'This field is required', count=0, status_code=200)

    def test_04_submit_form_with_incorrect_shop_store(self):
        response = self.client.post('/register/', {'store_name' : 'mystore has to fail',
                                               'password1' : 'apasswd',
                                               'password2' : 'apasswd',
                                               'email ': 'mymail@mymail.com' })
        self.assertContains(response, 'This field is required', count=0)
        self.assertContains(response, 'The shop name can only contain characters from a to z in lowercase', count=1)

    def test_05_get_thanks_template(self):
        response = self.client.get('/shop/thanks/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/thanks.html')

    def test_06_submit_form_with_already_existing_email(self):
        response = self.client.post('/register/', {'store_name' : 'mystore',
                                               'password1' : 'apasswd',
                                               'password2' : 'apasswd',
                                               'email' : 'mymail@mymail.com' })
        self.assertContains(response, 'This field is required', count = 0, status_code = 302)
        response = self.client.post('/register/', {'store_name' : 'newstore',
                                               'password1' : 'apasswd',
                                               'password2' : 'apasswd',
                                               'email' : 'mymail@mymail.com'})
        self.assertContains(response, u'This email address is already in use. Please supply a different email address.', count=1, status_code=200)
        self.assertContains(response, 'This field is required', count=0, status_code=200)

    def test_07_submit_form_with_already_existing_storename(self):
        response = self.client.post('/register/', {'store_name' : 'mystore',
                                               'password1' : 'apasswd',
                                               'password2' : 'apasswd',
                                               'email' : 'mymail@mymail.com'})
        self.assertEquals(response.status_code, 302)
        response = self.client.post('/register/', {'store_name' : 'mystore',
                                               'password1' : 'apasswd',
                                               'password2' : 'apasswd',
                                               'email' : 'myothermail@mymail.com'})
        self.assertContains(response, u'This email address is already in use. Please supply a different email address.', count=0, status_code=200)
        self.assertContains(response, 'The shop name already exists', count = 1, status_code =200)

    def test_08_submit_form_with_incorrect_passwords(self):
        response = self.client.post('/register/', {'store_name' : 'mystore',
                                               'password1' : 'apasswd',
                                               'password2' : 'anotherpasswd',
                                               'email' : 'mymail@mymail.com'})
        self.assertContains(response, u'You must type the same password', count=1, status_code=200)



