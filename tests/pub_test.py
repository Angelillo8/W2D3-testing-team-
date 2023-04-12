import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Davie Herderson", 12.35, 17)
        self.customer2 = Customer("Sally McPherson", 76, 25)
        self.customer3 = Customer("Johnny Urquart", 250, 30)

        drinks = [Drink("Tennents", 4.50, 4), Drink("Ale", 5.50, 10), 
                  Drink("Gin", 6.75, 35), Drink("Wine", 6.75, 15),
                  Drink("Whisky", 6.75, 45)]
        
        self.food1 = Food("Crisps", 2.50, 10)
        self.food2 = Food("Bacon roll", 8, 35)
        self.food3 = Food("Fish n' Chips", 12.50, 50)

        self.pub = Pub("Eagle and Fox", 550.00, drinks)

    def test_pub_has_name(self):
        self.assertEqual("Eagle and Fox", self.pub.name)

    def test_pub_has_drink(self):
        self.assertEqual(5, len(self.pub.drinks))
    
    def test_increase_till(self):
        self.pub.increase_till(self.pub.drinks[1])
        self.assertEqual(555.50, self.pub.till)

    def test_check_over_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer2))
    
    def test_check_under_age(self):
        self.assertEqual(False, self.pub.check_age(self.customer1))

    # @unittest.skip("Delete this line to run the test")
    def test_sell_drink_under_age(self):
        self.assertEqual("Ye are too young, mate! Sorry...", self.pub.sell_drink(self.pub.drinks[0], self.customer1))
        self.assertEqual(550.00, self.pub.till)
        self.assertEqual(12.35, self.customer1.wallet)

    def test_sell_drink(self):
        self.pub.sell_drink(self.pub.drinks[0], self.customer2)
        self.assertEqual(554.50, self.pub.till)
        self.assertEqual(71.5, self.customer2.wallet)
        self.assertEqual(4, self.customer2.drunkenness)
        self.pub.sell_drink(self.pub.drinks[4], self.customer2)
        self.pub.sell_drink(self.pub.drinks[4], self.customer2)
        self.assertEqual(568.00, self.pub.till)
        self.assertEqual(58, self.customer2.wallet)
        self.assertEqual(94, self.customer2.drunkenness)
    
    def test_sell_drink_customer_drunk(self):
        self.pub.sell_drink(self.pub.drinks[2], self.customer3)
        self.pub.sell_drink(self.pub.drinks[2], self.customer3)
        self.pub.sell_drink(self.pub.drinks[2], self.customer3)
        self.assertEqual(570.25, self.pub.till)
        self.assertEqual(229.75, self.customer3.wallet)
        self.assertEqual(105, self.customer3.drunkenness)
        self.pub.sell_drink(self.pub.drinks[2], self.customer3)
        self.assertEqual(577.0, self.pub.till)
        self.assertEqual(223.0, self.customer3.wallet)
        self.assertEqual(140, self.customer3.drunkenness)
        self.assertEqual("Ye are too drunk already, mate! Sorry...",self.pub.sell_drink(self.pub.drinks[2], self.customer3))
        self.assertEqual(577.0, self.pub.till)
        self.assertEqual(223.0, self.customer3.wallet)
        
