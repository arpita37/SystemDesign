import abc

class PaymentInterface(metaclass=abc.ABCMeta):
    def __subclasshook__(cls, __subclass):
        return ()

    def __init__(self,txId,amount):
        self.txId = txId
        self.amount = amount

    @abc.abstractmethod
    def executeTransaction(self):
        raise  NotImplementedError