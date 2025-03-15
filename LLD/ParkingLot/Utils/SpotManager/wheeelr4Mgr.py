from Utils.ParkingStratgey.nearToElev import NearToElevatorStrategy
from Utils.SpotManager.parkingSpotManager import ParkingspotManager


class Wheeler4Mgr(ParkingspotManager):
    def __init__(self,spots):
        super().__init__(spots,NearToElevatorStrategy())