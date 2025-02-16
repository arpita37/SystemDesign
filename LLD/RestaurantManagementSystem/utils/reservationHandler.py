from models.status import Status


class ReservationHandler:
    def __init__(self):
        self.reservations = dict()

    def addReservation(self,res,log):
        try:
            self.reservations[res.getId()] = res
            log.info(f"Reservation for {res.getName()} successful on {res.getTime()}")
        except Exception as e:
            raise e

    def updateResTiming(self,resId,t,log):
        try:
            obj = self.reservations[resId]
            if obj.getStauts() == Status.CANCELLED:
                log.info(f"Reservation cancelled, can't be updated!!")
                return
            obj.bookingTime = t
        except Exception as e:
            raise ValueError("Reservation doesn't exist")

    def cancelReservation(self,resId,log):
        try:
            obj = self.reservations[resId]
            obj.updateStaus(Status.CANCELLED)
            log.info(f"Reservation cancelled!!")
        except Exception as e:
            raise ValueError("Reservation doesn't exist")