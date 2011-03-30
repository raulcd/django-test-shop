__author__ = 'raulcd'

class PaymentBase:
    '''
    PaymentBase is the base class for the payments.
    '''

    def __init__(self, properties):
        for prop in properties:
            self.__dict__[prop] = properties[prop]
  