# -*- coding: utf-8 -*-
from shop.models.owner_account_model import OwnerAccount
from django.utils import unittest
from django.core.exceptions import ValidationError

class OwnerTestCase(unittest.TestCase):
    def create_fixtures(self):
        self.owneraccount = OwnerAccount()
        self.owneraccount.first_name = "Raúl"
        self.owneraccount.last_name = "Cumplido Domínguez"
        self.owneraccount.email = "raulcumplido@gmail.com"
        self.owneraccount.save()

    def test_01_unicode_returns_proper_stuff(self):
        self.create_fixtures()
        ret = self.owneraccount.__unicode__()
        self.assertEqual(ret, self.owneraccount.first_name)

    def test_02_create_owner_account_with_wrong_email(self):
        self.owneraccount_2 = OwnerAccount()
        self.owneraccount_2.first_name = "Raúl"
        self.owneraccount_2.last_name = "Cumplido Domínguez"
        self.owneraccount_2.email = "raulcd"
        with self.assertRaises(ValidationError):
            self.owneraccount_2.full_clean()
