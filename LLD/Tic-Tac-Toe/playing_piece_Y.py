from piecetype import PieceType
from playing_piece import PlayingPiece

class PlayingPieceY(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.Y)