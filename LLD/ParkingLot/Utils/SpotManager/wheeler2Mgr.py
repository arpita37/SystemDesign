from Utils.ParkingStratgey.neatToEnt import NearToEntranceStrategy
from Utils.SpotManager.parkingSpotManager import ParkingspotManager


class Wheeler2Mgr(ParkingspotManager):
    def __init__(self,spots):
        super().__init__(spots,NearToEntranceStrategy())
