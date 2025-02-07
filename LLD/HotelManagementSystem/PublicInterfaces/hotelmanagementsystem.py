import uuid
from threading import Lock

from Models.contract import Contract
from Models.guest import Guest
from Models.paymentType import PayemntType
from Models.reservationStatus import ReservationStatus
from Models.room import Room
from Utils.paymentByCard import CardPayment
from Utils.paymentByCash import CashPayment
from Utils.reservation import Reservations
import logging
logging.basicConfig(level = logging.INFO)
class HotelManageMentsystem:
    _instance = None

    def __new__(cls):
        cls._instance = super().__new__(cls)
        cls._instance.reservations = Reservations()
        cls._instance.rooms = dict()
        cls._instance.guests = dict()
        cls._instance.lock = Lock()
        cls._instance.log = logging.getLogger("HotelManagement")
        return cls._instance

    def getInstance(cls):
        return cls._instance

    def addRoom(self, room):
        self.rooms[room.getNo()] = room

    def showRooms(self):
        print("\nNUMBER\tFLOOR\tTYPE\tPRICE")
        for id,room in self.rooms.items():
            print(f"{room.getNo()}\t{room.getFloor()}\t{room.getType()}\t{room.getPrice()}\n")

    def _checkAvailability(self, roomNo, d1, d2):
        with self.lock:
            flag = True
            for id,ct in self.reservations.getReservations().items():
                if ct.getRoom().getNo() == roomNo:
                    if ct.getCheckinDate() >= d1 or ct.getCheckoutDate() <= d2:
                        flag = False
            return flag

    def checkAvailability(self, roomNo, d1, d2):
        if self._checkAvailability(roomNo, d1, d2):
            self.log.info(f"Room is available between {d1} and {d2}")
        else:
            self.log.info(f"Room is not available between {d1} and {d2}")

    def bookroom(self, roomNo, d1, d2, guest : Guest):
        if self._checkAvailability(roomNo, d1, d2):
            r = self.rooms[roomNo]
            resId = self.generateReservationId()
            reservation = Contract(resId,r,d1,d2,guest)
            self.reservations.addReservation(reservation)
            self.guests[guest.getId()] = reservation
        return None

    def checkin(self, roomNo, guest):
        with self.lock:
            try:
                r = self.rooms[roomNo]
                r.checkIn()
                self.log.info("Checkin successful")
            except Exception as e:
                self.log.warning(f"Some error occured : \n{e}")

    def checkout(self, roomNo, guest):
        with self.lock:
            if guest.getId() in self.guests:
                ct = self.guests[guest.getId()]
                if ct.getRoom().getNo() == roomNo:
                    r = self.rooms[roomNo]
                    if r.getStatus() == ReservationStatus.OCCUPIED:
                        print("How do you want to pay?")
                        mode = input()
                        pay = None
                        match mode.upper():
                            case PayemntType.CARD.name:
                                pay = CardPayment(ct)
                            case PayemntType.CASH.name:
                                pay = CashPayment(ct)
                            case _:
                                pay = CashPayment(ct)
                        msg = pay.processPayment()
                        self.log.info(msg)
                        res = ct.getContractId()
                        self.reservations.cancelReservation(res)
                        self.log.info("Checkout succesful")
                    else:
                        raise ValueError ("The room is not checked in yet")
                else:
                    raise ValueError (f"The guest with id {guest.getId()} has different booking for room {ct.getRoom().getNo()}")
            else:
                raise ValueError (f"The guest with id {guest.getId()} has no booking")

    def generateReservationId(self):
        return f"RES{uuid.uuid4().hex[:8].upper()}"
