import abc


class ProductStockInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass,"addOberserves") and
                callable(__subclass.addObservers) and
                hasattr(__subclass,"removeObservers") and
                callable(__subclass.removeObservers) and
                hasattr(__subclass,"notifyObservers") and
                callable(__subclass.notifyObservers) and
                hasattr(__subclass,"setData") and
                callable(__subclass.setData) )

    @abc.abstractmethod
    def addOberserves(self ):
        raise NotImplementedError

    @abc.abstractmethod
    def removeObservers(self):
        raise NotImplementedError

    @abc.abstractmethod
    def notifyObservers(self):
        raise NotImplementedError


    @abc.abstractmethod
    def setData(self):
        raise NotImplementedError