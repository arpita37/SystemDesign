from Models.Spot.parkingSpot import ParkingSpot

class ParkingSpotWheeler6(ParkingSpot):
    def __init__(self,id,floor):
        super().__init__(id,floor,400)