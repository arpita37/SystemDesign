import abc
from tkinter.font import names


class Product(metaclass=abc.ABCMeta):
    def __subclasshook__(cls, __subclass):
        return

    def __init__(self,name : str,price : int):
        self.name = name
        self.price = price

    def getProductName(self):
        return self.name

    def getProductPrice(self):
        return self.price