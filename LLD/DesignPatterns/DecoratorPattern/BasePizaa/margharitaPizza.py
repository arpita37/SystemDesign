from DesignPatterns.DecoratorPattern.BasePizaa.pizzaAbsClass import PizzaClass


class MargharitaPizza(PizzaClass):
    def __init__(self):
        super().__init__()

    def displayCost(self) -> int:
        return 200