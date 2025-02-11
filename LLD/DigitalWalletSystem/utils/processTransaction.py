import abc

class ProcessTransaction(metaclass=abc.ABCMeta):
    def __init__(self,tx,src,dest,amt):
        self.tx = tx
        self.src = src
        self.dest = dest
        self.amount = amt

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError

    @abc.abstractmethod
    def authenticate(self):
        raise NotImplementedError

