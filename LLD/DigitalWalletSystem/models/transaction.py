from models.paymentStatus import Paymentstatus

class Transaction:
    def __init__(self,id,target,source,amount,paidVia=None):
        self.id = id
        self.target = target
        self.source = source
        self.amount = amount
        self.status = Paymentstatus.INITIATED

    def getID(self): return self.id
    def getTarget(self): return self.target
    def getSource(self): return self.source
    def getAmount(self): return self.amount
    def getMethod(self): return self.paidVia
    def setPaymentMethod(self,method): self.paidVia = method
    def setStatus(self,st): self.status = st