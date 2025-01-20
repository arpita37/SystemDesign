from DesignPatterns.StrategyPattern.drivestrategies.driveStrategyInterface import DriveStrategy


class SpecialDriveStrategy(DriveStrategy):
    def __init__(self):
        super().__init__()

    def Drive(self):
        print(f'This is for special drive Strategy')