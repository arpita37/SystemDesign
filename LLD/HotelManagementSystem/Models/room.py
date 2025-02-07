from threading import Lock

from Models.reservationStatus import ReservationStatus
from Models.roomTypes import Roomtype
from Models.typeToPrice import TypeToPrice

class Room:
    def __init__(self, no, floorNo, type : Roomtype):
        self.no = no
        self.floorNo = floorNo
        self.type = type
        self.capacity = None
        self.price = TypeToPrice().getPrice(type)
        self.status = ReservationStatus.AVIALABLE
        self.lock = Lock()

    def setCapacity(self): self.capacity = self.type.value
    def getNo(self): return self.no
    def getFloor(self): return self.floorNo
    def getType(self): return self.type
    def getCapacity(self): return self.capacity
    def getPrice(self): return self.price
    def getStatus(self): return self.status
    def updateStatus(self, st):
        if self.status != st:
            self.status = st

    def checkIn(self):
        with self.lock:
            if self.status != ReservationStatus.AVIALABLE:
                raise Exception("Room is not available")
            self.status = ReservationStatus.OCCUPIED

    def checkOut(self):
        with self.lock:
            self.status = ReservationStatus.AVIALABLE

