import abc
from multiprocessing.dummy import freeze_support
from sortedcontainers import SortedSet

class ParkingSpots(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass):
        return ()

    def __init__(self, type: str, number: int, fee: int, freespots : SortedSet(), spotList : [] ):
        self.spotList = spotList
        self.parkingFee = fee
        self.freeSpots = self.calculateFreeSpots(spotList)
        self.occupiedSpots = SortedSet()

    def calculateFreeSpots(self, list_of_spots) -> SortedSet:
        return SortedSet(list_of_spots)
    @abc.abstractmethod
    def getType(self):
        return self.type

    def getFloorNumber(self):
        return self.floo

