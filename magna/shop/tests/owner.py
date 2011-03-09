# -*- coding: utf-8 -*-
from shop.models.owner_account_model import OwnerAccount
from django.utils import unittest

class OwnerTestCase(unittest.TestCase):
    def create_fixtures(self):
        self.owneraccount = OwnerAccount()
        self.owneraccount.first_name = "Raúl"
        self.owneraccount.last_name = "Cumplido Domínguez"
        self.owneraccount.save()

    def test_01_unicode_returns_proper_stuff(self):
        self.create_fixtures()
        ret = self.owneraccount.__unicode__()
        self.assertEqual(ret, self.owneraccount.first_name())
