from typing import Dict
from Models.contract import Contract
from Models.reservationStatus import ReservationStatus


class Reservations:
    def __init__(self):
        self.reservations = dict()

    def getReservations(self):
        return self.reservations

    def addReservation(self, contract : Contract):
        try:
            self.reservations[contract.getContractId()] = contract
        except Exception as e:
            print(f"Something went wrong\n{e}")

    def updateReservation(self, id, d1, d2):
        try:
            ct : Contract = self.reservations[id]
            ct.updateCheckinDate(d1)
            ct.updateCheckoutDate(d2)
        except Exception as e:
            print(f"Something went wrong\n{e}")

    def cancelReservation(self, id):
        try:
            ct : Contract = self.reservations[id]
            ct.getRoom().updateStatus(ReservationStatus.AVIALABLE)
            del self.reservations[id]
        except Exception as e:
            print(f"Something went wrong\n{e}")