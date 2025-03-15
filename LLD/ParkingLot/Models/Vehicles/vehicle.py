from Models.Vehicles.vehicleTypes import VehicleTypes


class Vehicle:
    def __init__(self,number,type:VehicleTypes):
        self.no = number
        self.type = type
        self.ticket = None
        self.spot = None

    def getNo(self): return self.no
    def getType(self): return self.type
    def getTicket(self): return self.ticket
    def setTicket(self,tick): self.ticket = tick
    def setSpot(self,sp): self.spot = sp
    def getSpot(self): return self.spot