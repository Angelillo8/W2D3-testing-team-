class Pub:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

    def increase_till(self, drink_to_sell):
        self.till += drink_to_sell.price
    
    def sell_drink(self, drink_to_sell, customer):
        if self.check_age(customer) == True:
            if self.check_drunkenness(customer) == False:
                self.increase_till(drink_to_sell)
                customer.buy_drink(drink_to_sell)
            else:
                return "Ye are too drunk already, mate! Sorry..."
        else:
            return "Ye are too young, mate! Sorry..."

    def check_age(self, customer):
        return customer.age >= 18
    
    def check_drunkenness(self, customer):
        return customer.drunkenness >= 125
    
    def sell_food(self, food_to_sell, customer):
        customer.buy_food(food_to_sell)
        self.increase_till(food_to_sell)
