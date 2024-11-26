from playing_piece import PlayingPiece
import piecetype

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(piecetype.PieceType.X)