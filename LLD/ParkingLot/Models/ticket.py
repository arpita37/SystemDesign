class Ticket:
    def __init__(self,TXnID,entryTime,vehicle,spot):
        self.txnID = TXnID
        self.entryTime = entryTime
        self.vehicle = vehicle
        self.spot = spot

    def getTxnId(self): return self.txnID
    def getEntrytime(self): return self.entryTime
    def getVehicle(self): return self.vehicle
    def getSpot(self): return self.spot