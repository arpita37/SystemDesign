import abc


class ObserverInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass, "update") and
                callable(__subclass.update))

    @classmethod
    def __init__(self,name :str) -> None:
        self.username = name

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError