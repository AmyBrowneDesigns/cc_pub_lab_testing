class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.customer_drinks = []


    def reduce_wallet(self, amount):
        self.wallet -= amount
    
    def add_drink_to_customer(self, beverage):
        self.customer_drinks.append(beverage)
    
        
 