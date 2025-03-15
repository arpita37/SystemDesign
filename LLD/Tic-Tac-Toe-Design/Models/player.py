class Player:
    def __init__(self, id, name, playerPiece):
        self.id = id
        self.name = name
        self.piece = playerPiece

    def getId(self): return self.id
    def getName(self): return self.name
    def getPiece(self): return self.piece