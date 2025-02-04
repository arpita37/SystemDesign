import abc


class Transaction(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return()

    def __init__(self, id, account, amount):
        self.id = id
        self.account = account
        self.amount = amount

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError