from models.status import Status

class Transaction:
    def __init__(self,id,amount,method):
        self.id = id
        self.amount = amount
        self.method = method
        self.status = Status.PENDING

    def getId(self): return self.id
    def getAmount(self): return self.amount
    def getMethod(self): return self.method
    def getStatus(self): return self.status
    def updateStatus(self,st): self.status = st
    def execute(self):
        pass