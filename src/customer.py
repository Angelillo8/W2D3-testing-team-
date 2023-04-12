class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkenness = 0

    def buy_drink(self, drink_to_buy):
        self.decrease_wallet(drink_to_buy)
        self.drunkenness += drink_to_buy.alcohol_level

    def decrease_wallet(self, object_to_buy):
        self.wallet -= object_to_buy.price
    
    def buy_food(self, food):
        self.decrease_wallet(food)
        self.drunkenness -= food.rejuvenation_level
