import abc


class LogProcessor(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return(hasattr(__subclass, "nextLogProcessor") and
               hasattr(__subclass, "log") and
               callable((__subclass.log)))

    def __init__(self,nextLogProcessor):
        self.nextLogProcessor = nextLogProcessor

    def log(self, level, message):
        if level != None:
            self.nextLogProcessor.log(level, message)
