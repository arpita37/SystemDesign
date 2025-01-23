from ParkingLotDesign.ParkingSpot.spot import Spot
from ParkingLotDesign.Payment.vehicleToPriceEnum import VehicleToPrice
from ParkingLotDesign.Vehicle.vehicleTypes import VehicleTypes
from ParkingLotDesign2.Models.Spots.spotTypeEnum import SpotType
from typing import List


class Levels:
    def __init__(self, numberOfSlots: int, floornumber : int):
        self.numberOFSlots = numberOfSlots
        self.floornumber = floornumber
        print(f"For each type of vehicle {self.numberOFSlots} slots will be created in level {self.floornumber}")
        self.spots : List[Spot] = []
        for item1,item2 in zip(VehicleTypes, VehicleToPrice):
            self.spots.extend([Spot(i, item1.name, item2.value) for i in range(numberOfSlots)])

    def getSpot(self, type):
        for spot in self.spots:
            if spot.getSpotType() == type:
                return spot
        print( f"\nNo slot is avaialble on {self.getFloorNumber()} for {type} type vehicle")
        return None


    def displayAvailability(self):
        print( f"\nFor {self.floornumber} floor below spots are available:")
        print(f"\nSpotID\tSpotType")
        for spot in self.spots:
            if spot.getOccupancyStatus() == False:
                print(f"\n{spot.getSpotId()}\t{spot.getSpotType()}")





