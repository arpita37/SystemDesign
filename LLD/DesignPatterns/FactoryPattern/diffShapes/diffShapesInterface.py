import abc


class DiffShapes(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return

    @classmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def draw(self):
        raise NotImplementedError