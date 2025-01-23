from typing import List

from ParkingLotDesign.ParkingLevels.parkingLevel import Levels
from ParkingLotDesign.Vehicle.vehicleInterface import Vehicle


class ParkingLot:
    _instance = None

    def __askForLevels(self):
        print("How many levels do you want?")
        levels = int(input())
        print("How many spots do you want epr level?")
        spots = int(input())
        self.addLevels(levels, spots)

    def __init__(self):
        if self._instance == None:
            ParkingLot._instance = self
            self.levels: List[Levels] = []
            self.__askForLevels()
        else:
            print( f"\nParkinglot is a singleton class, can't create another object of it")


    def addLevels(self, levels, slots):
        for floor in range(levels):
            temp = Levels(slots , floor)
            self.levels.append(temp)


    def parkVehicle(self,vehicle : Vehicle):
        status = False
        for level in range(len(self.levels)):
            spot = self.levels[level].getSpot(vehicle.getType())
            if spot != None:
                result = spot.occupySpot(vehicle.getType(), vehicle)
                if result != None:
                    vehicle.setSpot(result)
                    vehicle.setFloor(level)
                    status = True
                    break
        if status:
            print( f"\nSpot booked at {level} floor for vehicle number {vehicle.getCarNumber()}")
        else:
            print(f"\nSORRY! No vacancy! Spot could not be booked for vehicle number {vehicle.getCarNumber()}")

    def unparkVehicle(self, vehicle : Vehicle):
        floor = vehicle.getFloor()
        if floor >= 0 and floor < len(self.levels):
            try:
                spot = vehicle.getSpot()
                self.levels[floor][spot].releaseSpot()
            except:
                print(f"\nSome exception occured\n")
        else:
            print( f"\nWrong floor number assigned to {vehicle.getCarNumber()}. This floor is not part of this parking lot")


    def displayAvailability(self):
        for level in self.levels:
            level.displayAvailability()

