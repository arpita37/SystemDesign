from Models.pieceTypes import PieceTypes
from Models.playerPieceInterface import PlayerPieceInterface


class PlayerPieceX(PlayerPieceInterface):
    def __init__(self):
        super().__init__(PieceTypes.X)