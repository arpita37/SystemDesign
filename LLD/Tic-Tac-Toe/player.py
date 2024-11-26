from playing_piece import PlayingPiece
class Player:
    def __init__(self, name:str, piece) -> None:
        self.name = name
        self.piece = piece

    def setName(self,name) -> None:
        self.name = name

    def setPiece(self, piece: PlayingPiece) -> None:
        self.piece = piece

    def getName(self) -> str:
        return self.name
    
    def getPiece(self) -> PlayingPiece:
        return self.piece
    