class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drinks = []
        

    def add_drink(self, beverage):
        self.drinks.append(beverage)


    def check_drink_stock(self):
        return len(self.drinks)


    def increase_pub_till(self, amount):
        self.cash += amount

    def sell_drink_to_customer(self, beverage):
        for drink in self.drinks:
            if drink.name == beverage.name:
                self.drinks.remove(beverage)
                customer.add_drink_to_customer(beverage)

        #add drink to cust list



    