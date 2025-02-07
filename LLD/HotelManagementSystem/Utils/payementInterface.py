import abc
from Models.contract import Contract


class Payemnt(metaclass=abc.ABCMeta):
    def __subclasshook__(cls, __subclass):
        return( hasattr(__subclass,"processPayment") and
                callable(__subclass.processPayment))

    def __init__(self,ct : Contract):
        self.ct = ct

    @abc.abstractmethod
    def processPayment(self):
        raise NotImplementedError