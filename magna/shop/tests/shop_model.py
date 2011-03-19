# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from shop.models.shop_model import Shop
from django.utils import unittest
from django.core.exceptions import ValidationError


class ShopTestCase(unittest.TestCase):
    def create_fixtures(self):
        self.user = User()
        self.user.username =  "myemail@myemail.com"
        self.user.password = 'my_pass'
        self.user.save()
        self.shop = Shop()
        self.shop.owner = self.user
        self.shop.name = 'myshopname'
        self.shop.save()

    def test_01_create_shop_is_correct(self):
        self.create_fixtures()
        ret = Shop.objects.all()
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0].name, 'myshopname')
