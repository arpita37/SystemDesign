from CoffeeTypes.coffee import Coffees
from CoffeeTypes.coffeeInterface import CoffeeInterface
from typing import List

class Esprresso(CoffeeInterface):
    def __init__(self, ingredients : List):
        super().__init__(Coffees.ESPRESSO.name, 200, ingredients)


