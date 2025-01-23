class Vehicle:
    def __init__(self, number : int, type: str):
        self.number = number
        self.spot = None
        self.type = type
        self.floor = None

    def setSpot(self, spot):
        self.spot = spot

    def setFloor(self, floor):
        self.floor = floor

    def getFloor(self):
        return self.floor

    def getSpot(self):
        return self.spot

    def getType(self):
        return self.type

    def getCarNumber(self):
        return self.number
