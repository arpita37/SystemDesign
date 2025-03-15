from Utils.ParkingStratgey.strategy import Strategy


class NearToElevatorStrategy(Strategy):
    def __init__(self):
        super().__init__()

    def gtetstratgey(self):
        # implement code
        return f"Finding spot using near to elevator stratgey"