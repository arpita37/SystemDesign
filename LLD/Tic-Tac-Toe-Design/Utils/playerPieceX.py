from Models.pieceType import PieceType
from Utils.playerPieceInterface import PlayerPiece


class PlayerPieceX(PlayerPiece):
    def __init__(self):
        super().__init__(PieceType.X)