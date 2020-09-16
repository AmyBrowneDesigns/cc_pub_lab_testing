import unittest
from src.pub import Pub 
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.drink = Drink ("water", 5.00)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_add_drink(self):
        beverage_1 = Drink ("wine", 30.00)
        beverage_2 = Drink ("beer", 10.00)
        beverage_3 = Drink ("whiskey", 50.00)
        self.pub.add_drink(beverage_3)
        self.pub.add_drink(beverage_1)
        self.pub.add_drink(beverage_2)
        self.assertEqual(3, len(self.pub.drinks))

    def test_check_drink_stock(self):
        self.assertEqual(0, len(self.pub.drinks))

    def test_increase_pub_till(self):
        self.pub.increase_pub_till(self.drink.price)
        self.assertEqual(105.00, self.pub.cash)


    #def test_add_drink_to_customer(self):



    #def test_sell_drink_to_customer(self):

    
    # def test_reduce_wallet(self):
    #     self.customer.reduce_wallet(self.drink.price)
    #     self.assertEqual(45.00, self.customer.wallet)