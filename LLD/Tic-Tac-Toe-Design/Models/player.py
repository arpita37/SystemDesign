from Utils.playerPieceInterface import PlayerPiece

class Player:
    def __init__(self, name, piece: PlayerPiece):
        self.name = name
        self.piece = piece

    def getName(self):
        return self.name

    def getPiece(self):
        return self.piece.getPiece()
