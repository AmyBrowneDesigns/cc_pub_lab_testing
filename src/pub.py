class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drinks = []



    def increase_pub_till(self, amount):
        self.cash += amount