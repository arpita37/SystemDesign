from Models.Spot.spotStatus import SpotStatus
from Models.Vehicles.vehicle import Vehicle

class ParkingSpot:
    def __init__(self,id,floor,price=100):
        self.id = id
        self.floor = floor
        self.vehicle = None
        self.price = price
        self.status = SpotStatus.FREE

    def getId(self): return self.id
    def getFloor(self): return self.floor
    def getVehicle(self): return self.vehicle
    def getPrice(self): return self.price
    def getStatus(self): return self.status
    def setStatus(self,st): self.status = st

    def parkVehicle(self, vehicle:Vehicle):
        self.vehicle = self.vehicle
        self.setStatus(SpotStatus.OCCUPIED)

    def unparkVehicle(self):
        self.vehicle = None
        self.setStatus(SpotStatus.FREE)