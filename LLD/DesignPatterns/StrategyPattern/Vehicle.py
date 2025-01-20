from DesignPatterns.StrategyPattern.drivestrategies.driveStrategyInterface import DriveStrategy


class Vehicle:
    def __init__(self, driveObj : DriveStrategy) -> None:
        self.driverObject = driveObj

    def Drive(self):
        self.driverObject.Drive()