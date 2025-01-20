import abc


class PizzaClass(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return ()

    @abc.abstractmethod
    def displayCost(self):
        raise NotImplementedError