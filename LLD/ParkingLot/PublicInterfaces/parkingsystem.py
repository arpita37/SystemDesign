import logging

from Models.Vehicles.vehicle import Vehicle
from PublicInterfaces.entrance import EntraceGate
from PublicInterfaces.exitGate import ExitGate
from Utils.Payments.payment import Payment
from Utils.Payments.paymentCard import PaymentCard
from Utils.Payments.paymentUPI import PaymentUpi

logging.basicConfig(level=logging.INFO)
from threading import Lock

class ParkingSystem:
    _instance = None

    def __new__(cls, w2, w3, w4, w6):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.w2 = w2
            cls._instance.w3 = w3
            cls._instance.w4 = w4
            cls._instance.w6 = w6
            cls._instance.log = logging.getLogger("ParkingSystem")
            cls._instance.lock =Lock()
            cls._instance.entrance = EntraceGate(w2,w3,w4,w6)
            cls._instance.exitG = ExitGate(w2,w3,w4,w6)
        else:
            print("This is a singleton class")
        return cls._instance

    def bookSpot(self,vh:Vehicle):
        val = self.entrance.BookSpot(vh)
        if not val:
            self.log.warning("No spot found")
            return
        self.log.info(f"SpotId : {val.getId()}, Floor : {val.getFloor()}")

    def freeSpot(self,vh):
        if not vh.getSpot():
            self.log.warning(f"The vehicle with no {vh.getNo()} is not parked yet")
            return
        val = self.exitG.calculatePrice(vh)
        self.log.info(f"Vehicle {vh.getNo()} have to pay {val}")
        method = input("How do you want to pay/\n1.Cash\n2.Card\n3.UPI")
        obj = None
        match method:
            case "UPI":
                obj = PaymentUpi()
            case "CARD":
                obj = PaymentCard()
            case _:
                obj = Payment()
        obj.pay(val,self.log)
        self.exitG.freeSpot(vh)
        self.log.info(f"Spot {vh.getTicket().getSpot().getId()} is free now")