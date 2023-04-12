import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Fish n Chips", 12.50, 60)
    
    def test_food_has_name(self):
        self.assertEqual("Fish n Chips", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(12.50, self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(60, self.food.rejuvenation_level)