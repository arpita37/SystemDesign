class CoffeeInterface:
    def __init__(self, name : str, price : float, ingredients : dict):
        self.name = name
        self.price = price
        self.dingredients = ingredients

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getIngredients(self):
        return self.dingredients

