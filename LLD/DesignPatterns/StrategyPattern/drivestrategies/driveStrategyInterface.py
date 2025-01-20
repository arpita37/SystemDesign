import abc


class DriveStrategy(metaclass=abc.ABCMeta):
    classmethod
    def __subclasshook__(cls, __subclass):
        return(hasattr(__subclass,'Drive') and
               callable(__subclass.Drive))

    @abc.abstractmethod
    def Drive(self):
        raise NotImplementedError

