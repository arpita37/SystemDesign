from DesignPatterns.StrategyPattern.Vehicle import Vehicle
from DesignPatterns.StrategyPattern.drivestrategies.normalDriveStrategy import NormalDriveStrategy


class GoodsVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())

    def Drive(self):
        super().drive()
