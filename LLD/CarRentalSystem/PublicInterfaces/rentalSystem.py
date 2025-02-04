from threading import Lock
import logging
from pygments.lexer import default
from Handlers.carHandler import CarHandler
from Handlers.payViaUPI import UPIPayment
from Models.contract import Contract
from Models.user import User

logging.basicConfig(level=logging.INFO)

class RentalSystem:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            cls._instance = super().__new__(cls)
            cls._instance.cars = CarHandler()
            cls._instance.users = dict()
            cls._instance.log = logging.getLogger("CarRentalSystem")
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance:
            print("The class is a singleton class")
        return cls._instance

    def add_cars(self, car):
        self.cars.addCar(car, self.log)

    def addUser(self, user : User):
        id = user.getId()
        if id not in self.users:
            self.users[id] = user
            self.log.info(f"User with {id} has been added")
            return

        self.log.info(f"User with {id} already exists")

    def browseCars(self):
        self.cars.browse(self.log)

    def reserveCar(self, user : User, carId :int, startDate, endDate):
        with self._lock:
            val = self.cars.isAvailable(carId, startDate, endDate)
            if not val:
                self.log.info(f"Car with {carId} not available in this period, please select another date")
                return
            val = self.cars.reserve(carId, startDate, endDate, self.log)
            if not val:
                self.log.warning("Could not reserve car due to some failure")
                return
            ct = Contract(carId,startDate,endDate,user.getId())
            res = self.payment(ct, carId, startDate, endDate)
            if not res:
                self.cancelReservation(carId,ct)
                self.log.warning("Could not reserve car due to payment failure")
                return
            return ct

    def payment(self, ct : Contract, carId, startDate, endDate):
        self.log.info("Please enter the payment method as string prompted-\n1.Card\n2.UPI")
        method = input()
        match method:
            case "Card":
                ct.payemnt = "Card"
                self.cars.payViaCard(ct, carId, startDate, endDate)
                return True
            case "UPI":
                ct.payemnt = "UPI"
                self.cars.payViaUPI(ct, carId, startDate, endDate)
                return True
            case _:
                self.log(f"Wrong payment method selected, reverting the changes")
                return False

    def cancelReservation(self, carId :int, contract):
        self.cars.unreserveCar(carId, contract)
        self.log.info(f"Payment of Rs. {contract.price} returned")

    def returnCar(self, carId, contract):
        self.cars.unreserveCar(carId, contract)










