from django.db import models
from shop.models.shop_model import Shop

class PaymentTypes(models.Model):
    '''
    Different type of possible payments
    '''
    name = models.CharField(max_length=100)
    shops = models.ManyToManyField(Shop, through="ShopPaymentTypes")


class ShopPaymentTypes(models.Model):
    shop = models.ForeignKey(Shop)
    payment_type = models.ForeignKey(PaymentTypes)

    class Meta:
        unique_together = ("shop", "payment_type")


class PaymentProperties(models.Model):
    '''
    Base class to have properties for the shop payments
    '''
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=200)
    shop_payment_type = models.ForeignKey(ShopPaymentTypes)


