import abc

#Can be extended a sper requirement, follows LSP
class PlayerPieceInterface(metaclass=abc.ABCMeta):
    def __init__(self, type):
        self.pieceType = type

    def getPieceType(self): return self.pieceType