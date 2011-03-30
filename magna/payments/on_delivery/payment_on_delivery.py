from payments import payment_backend


class PaymentOnDelivery(payment_backend.PaymentBase):

    def pay(self):
        try:
            return self.cost
        except AttributeError:
            return False
  