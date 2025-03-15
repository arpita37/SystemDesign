from Models.Vehicles.vehicle import Vehicle
from Models.Vehicles.vehicleTypes import VehicleTypes

class Wheeler2(Vehicle):
    def __init__(self,no):
        super().__init__(no,VehicleTypes.WheelerType2)