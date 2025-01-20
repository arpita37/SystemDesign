import abc

from DesignPatterns.DecoratorPattern.BasePizaa.pizzaAbsClass import PizzaClass


class Toppins(PizzaClass):
    def __subclasshook__(cls, __subclass):
        return()

    def __init__(self,):
        super().__init__()

    @abc.abstractmethod
    def displayCost(self):
        raise NotImplementedError