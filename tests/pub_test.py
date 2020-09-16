import unittest
from src.pub import Pub 
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.drink = Drink ("water", 5.00)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)


    def test_increase_pub_till(self):
        self.pub.increase_pub_till(self.drink.price)
        self.assertEqual(105.00, self.pub.cash)
    
    # def test_reduce_wallet(self):
    #     self.customer.reduce_wallet(self.drink.price)
    #     self.assertEqual(45.00, self.customer.wallet)