import abc
from Models.Spot.spotStatus import SpotStatus
from Utils.ParkingStratgey.strategy import Strategy


class ParkingspotManager:
    def __init__(self,spots : dict,st=Strategy()):
        self.spotList = spots
        self.parkingStrategy = st

    def addParkingSpot(self,spot):
        if spot.getId() not in self.spotList:
            self.spotList[spot.getId()] = spot

    def removeParkingSpot(self,spot):
        if spot.getId() in self.spotList:
            self.spotList.pop(spot.getId())

    def parkVehicle(self,spotId,vh):
        self.spotList[spotId].parkVehicle(vh)

    def unparkVehicle(self,spotId):
        self.spotList[spotId].unparkVehicle()

    def findSpot(self):
        self.parkingStrategy.gtetstratgey()
        for key,val in self.spotList.items():
            if val.getStatus() == SpotStatus.FREE:
                return key
        return None
