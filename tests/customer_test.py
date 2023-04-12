import unittest
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Cuddie Waddle", 50, 19)
        self.customer2 = Customer("Liz Barton", 550, 45)
        self.drink1 = Drink("Scottish Ale", 4.75, 5)
        self.drink2 = Drink("Wine", 6.50, 15)
        self.drink3 = Drink("Vodka", 6, 42)
        self.food1 = Food("Crisps", 2.50, 10)
    
    def test_customer_has_name(self):
        self.assertEqual("Cuddie Waddle", self.customer1.name)

    def test_customer_has_cash(self):
        self.assertEqual(550, self.customer2.wallet)

    def test_customer_can_decrease_wallet(self):
        self.customer1.decrease_wallet(self.drink1)
        self.assertEqual(45.25, self.customer1.wallet)

    def test_customer_has_age(self):
        self.assertEqual(19, self.customer1.age)

    def test_customer_buy_drink(self):
        self.customer2.buy_drink(self.drink2)
        self.assertEqual(15, self.customer2.drunkenness)
        self.assertEqual(543.50, self.customer2.wallet)
        self.customer2.buy_drink(self.drink3)
        self.customer2.buy_drink(self.drink3)
        self.assertEqual(99, self.customer2.drunkenness)
        self.assertEqual(531.50, self.customer2.wallet)
    
    def test_customer_buy_food(self):
        self.customer2.buy_drink(self.drink2)
        self.assertEqual(15, self.customer2.drunkenness)
        self.assertEqual(543.50, self.customer2.wallet)
        self.customer2.buy_food(self.food1)
        self.assertEqual(5, self.customer2.drunkenness)
        self.assertEqual(541.00, self.customer2.wallet)