from DesignPatterns.StrategyPattern.Vehicle import Vehicle
from DesignPatterns.StrategyPattern.drivestrategies.specialDriveStrategy import SpecialDriveStrategy


class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStrategy())

    def Drive(self):
        super().Drive()