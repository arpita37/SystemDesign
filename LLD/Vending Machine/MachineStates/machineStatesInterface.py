import abc

from PaymentTypes.coins import Coins
from PaymentTypes.notes import Notes
from Products.prouctsInterface import Product


class MachineStates(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return( hasattr(__subclass,"select_product") and
                callable(__subclass.select_product) and
                hasattr(__subclass, "insert_coin") and
                callable(__subclass.insert_coin) and
                hasattr(__subclass, "insert_note") and
                callable(__subclass.insert_note) and
                hasattr(__subclass, "dispense_product") and
                callable(__subclass.dispense_product) and
                hasattr(__subclass, "return_change") and
                callable(__subclass.return_change)
                )

    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abc.abstractmethod
    def select_product(self, product : Product):
        raise NotImplementedError

    @abc.abstractmethod
    def insert_coin(self, coin: Coins):
        raise NotImplementedError

    @abc.abstractmethod
    def insert_note(self, note : Notes):
        raise NotImplementedError

    @abc.abstractmethod
    def dispense_product(self):
        raise NotImplementedError

    @abc.abstractmethod
    def return_change(self):
        raise NotImplementedError