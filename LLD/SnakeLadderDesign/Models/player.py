class Player:
    def __init__(self,name):
        self.name = name
        self.currPos = 0

    def getName(self): return self.name
    def getPos(self): return self.currPos
    def updatePos(self,pos): self.currPos += pos
    def resetPos(self,pos): self.currPos = pos