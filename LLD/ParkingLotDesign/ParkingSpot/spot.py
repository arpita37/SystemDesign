from ParkingLotDesign.Vehicle.vehicleInterface import Vehicle
from ParkingLotDesign.Vehicle.vehicleTypes import VehicleTypes


class Spot:
    def __init__(self, num, type=VehicleTypes.CAR, fee=100 ):
        self.spotId = num
        self.spotType = type
        self.fee = fee
        self.is_Occupied = False
        self.car = None

    def getSpotType(self):
        return self.spotType

    def getSpotId(self):
        return self.spotId

    def getFee(self):
        return self.fee

    def getOccupancyStatus(self):
        return self.is_Occupied

    def getCarStatus(self):
        return self.car

    def occupySpot(self, type : str, vehicle : Vehicle):
        if self.is_Occupied == False and vehicle.getType() == self.getSpotType():
            self.is_Occupied = True
            self.car = vehicle
            print( f"Spot {self.spotId} has been occupied by car number {vehicle.getCarNumber()}")
            return self.getSpotId()
        elif self.is_Occupied:
            print(f"Spot {self.spotId} is lready occupied")
        else:
            print( f"Invalid car type {vehicle.getType()} for spot type {self.getSpotType()}")
        return None


    def releaseSpot(self):
        self.is_Occupied = False
        self.car = None
        print( f"Spot {self.spotId} is available now" )
        return True
