from ParkingLotDesign.Vehicle.vehicleInterface import Vehicle
from ParkingLotDesign.Vehicle.vehicleTypes import VehicleTypes


class MotorCycle(Vehicle):
    def __init__(self, number : int, type: str):
        super().__init__(number, type)