from Models.pieceTypes import PieceTypes
from Models.playerPieceInterface import PlayerPieceInterface


class PlayerPieceY(PlayerPieceInterface):
    def __init__(self):
        super().__init__(PieceTypes.Y)