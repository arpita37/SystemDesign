from DesignPatterns.StrategyPattern.drivestrategies.driveStrategyInterface import DriveStrategy


class NormalDriveStrategy(DriveStrategy):
    def __init__(self):
        super().__init__()

    def Drive(self):
        print(f'This is for normal drive Strategy')