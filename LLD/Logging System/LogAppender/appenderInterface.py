import abc

class LogAppender(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass,"appendLog") and
                callable(__subclass.appendLog))

    @abc.abstractmethod
    def appendLog(self):
        raise NotImplementedError

