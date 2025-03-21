from DesignPatterns.DecoratorPattern.BasePizaa.pizzaAbsClass import PizzaClass
from DesignPatterns.DecoratorPattern.Toppings.toppinsAbsClass import Toppins


class CheeseToppins(Toppins):
    def __init__(self, pizza : PizzaClass):
        super().__init__()
        self.pizzaObj = pizza

    def displayCost(self):
        return self.pizzaObj.displayCost() + 50