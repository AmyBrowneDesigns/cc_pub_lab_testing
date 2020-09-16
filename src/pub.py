class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drinks = []
        

    def add_drink(self, beverage):
        self.drinks.append(beverage)



    def increase_pub_till(self, amount):
        self.cash += amount



    