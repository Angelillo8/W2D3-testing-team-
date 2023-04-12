import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Single malt whisky", 8.5, 45)

    def test_drink_has_name(self):
        self.assertEqual("Single malt whisky", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(8.5, self.drink.price)