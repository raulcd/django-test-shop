# -*- coding: utf-8 -*-
from shop.models.shop_model import Shop
from shop.models.owner_account_model import OwnerAccount
from django.utils import unittest
from django.core.exceptions import ValidationError


class ShopTestCase(unittest.TestCase):
    def create_fixtures(self):
        self.owneraccount = OwnerAccount()
        self.owneraccount.first_name = "FirstName"
        self.owneraccount.last_name = "LastName"
        self.owneraccount.email = "myemail@myemail.com"
        self.owneraccount.save()
        self.shop = Shop()
        self.shop.owner = self.owneraccount
        self.shop.name = 'myshopname'
        self.shop.save()

    def test_01_create_shop_is_correct(self):
        self.create_fixtures()
        ret = Shop.objects.all()
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0].name, 'myshopname')
