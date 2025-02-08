import abc

class Piece:
    def __init__(self,start : int,end: int ):
        self.start = start
        self.end = end

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end