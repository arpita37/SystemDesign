from DesignPatterns.StrategyPattern.Vehicle import Vehicle
from DesignPatterns.StrategyPattern.drivestrategies.specialDriveStrategy import SpecialDriveStrategy


class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDriveStrategy())

    def Drive(self):
        super().Drive()