from CoffeeTypes.coffee import Coffees
from CoffeeTypes.coffeeInterface import CoffeeInterface
from typing import List


class Latte(CoffeeInterface):
    def __init__(self, ingredients: List):
        super().__init__(Coffees.LATTE.name, 300, ingredients)
