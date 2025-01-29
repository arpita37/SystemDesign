import abc

from Comments.comment import Comment


class Commentable(metaclass=abc.ABCMeta):
    def __subclasshook__(cls, __subclass):
        return ( hasattr(__subclass, "addComment") and
                 callable((__subclass.addComment)) and
                 hasattr(__subclass, "deleteComment") and
                 callable(__subclass.deleteComment))

    @abc.abstractmethod
    def addComment(self, cmt: Comment):
        raise NotImplementedError

    @abc.abstractmethod
    def deleteComment(self, cmt: Comment):
        raise NotImplementedError