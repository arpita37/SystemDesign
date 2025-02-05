import abc
from Models.pieceType import PieceType


class PlayerPiece(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return ()

    def __init__(self, piece : PieceType):
        self.piece = piece

    def getPiece(self):
        return self.piece