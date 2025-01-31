import CoffeeTypes.coffee
from CoffeeTypes.coffee import Coffees
from CoffeeTypes.coffeeInterface import CoffeeInterface
from typing import List


class Capuccino(CoffeeInterface):
    def __init__(self, ingredients: List):
        super().__init__(Coffees.CAPUCCINO.name, 100, ingredients)