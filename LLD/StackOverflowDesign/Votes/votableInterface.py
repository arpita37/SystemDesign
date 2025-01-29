import abc

from Votes.vote import Vote


class Votable(metaclass=abc.ABCMeta):
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass, "addVote") and
                callable((__subclass.addVote)) and
                hasattr(__subclass, "deleteVote") and
                callable(__subclass.deleteVote))

    @abc.abstractmethod
    def addVote(self, vote:Vote):
        raise NotImplementedError

    @abc.abstractmethod
    def deleteVote(self, vote: Vote):
        raise NotImplementedError