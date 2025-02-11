class Card:
    def __init__(self,no,type,acc):
        self.no = no
        self.associatedAccount = acc
        self.type = type

    def gteNumber(self): return self.no
    def getType(self): return self.type
    def getAccount(self): return self.associatedAccount