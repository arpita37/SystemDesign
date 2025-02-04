import abc
from datetime import datetime


class Payment(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return

    def __init__(self, car):
        self.car = car

    def days_between(self,s,e):
        d1 = datetime.strptime(s,"%Y-%m-%d")
        d2 = datetime.strptime(e,"%Y-%m-%d")
        return abs((d2-d1).days)

    @abc.abstractmethod
    def pay(self):
        raise NotImplementedError