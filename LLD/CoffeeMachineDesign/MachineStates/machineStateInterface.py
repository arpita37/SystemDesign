import abc


class MachineStates(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return( hasattr(__subclass,"ready") and
                callable(__subclass.ready) and
                hasattr(__subclass,"pay") and
                callable(__subclass.pay) and
                hasattr(__subclass,"dispense") and
                callable(__subclass.dispense) and
                hasattr(__subclass,"returnChange") and
                callable(__subclass.returnChange))

    def __init__(self, cm):
        self.machine = cm

    @abc.abstractmethod
    def selectProduct(self):
        raise NotImplementedError


    @abc.abstractmethod
    def pay(self):
        raise NotImplementedError

    @abc.abstractmethod
    def dispense(self):
        raise NotImplementedError

    @abc.abstractmethod
    def returnChange(self):
        raise NotImplementedError