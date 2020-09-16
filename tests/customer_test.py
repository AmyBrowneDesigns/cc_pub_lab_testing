import unittest 
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Jenken", 50.00)
        self.drink = Drink("water", 5.00)


    def test_customer_name(self):
        self.assertEqual("Jenken", self.customer.name)

    def test_wallet_amount(self):
        self.assertEqual(50.00, self.customer.wallet)


    def test_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink.price)
        self.assertEqual(45.00, self.customer.wallet)