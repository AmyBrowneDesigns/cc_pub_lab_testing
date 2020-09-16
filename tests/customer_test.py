import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("Jenken", 50.00)


    def test_customer(self):
        self.assertEqual("Jenken", self.customer.name)