from logging import Logger

from Handlers.payViaCard import CardPayment
from Handlers.payViaUPI import UPIPayment
from Models.car import Car
from collections import defaultdict
from sortedcontainers import SortedList

from Models.contract import Contract


class CarHandler:
    def __init__(self):
        self.cars : dict[Car] = dict()
        self.reservedCars = defaultdict(SortedList)

    def addCar(self, c:Car, log : Logger):
        carNo = c.getCarNo()
        if carNo not in self.cars:
            self.cars[carNo] = c
            log.info(f"Car no {carNo} has been added to the inventory")
            return
        log.info(f"Car no {carNo} already exists in the inventory")

    def browse(self, log : Logger):
        log.info("CARNO\tTYPE\tMAKE\tMODEL\tYEAR\tPRICE")
        for key,val in self.cars.items():
            log.info(f"{val.getCarNo()}\t{val.getType()}\t{val.getMake()}\t{val.getModel()}\t{val.getYear()}\t{val.getPrice()}")


    def isAvailable(self, id, startDate, endDate):
        if id not in self.cars:
            print(f"Car with id {id} does not exist, please enter a valid car id")
            return False
        li = self.reservedCars[id]
        if len(li) == 0:
            return True
        idx = 0
        start = end = False
        for s,e in li:
            if ( s >= startDate and s <= endDate ) or (e >= startDate and e <= endDate):
                return False
        return True

    def reserve(self, carId, start_date, end_date, log : Logger):
        if carId not in self.cars:
            log.info(f"Car with id {carId} does not exist, please enter a valid car id")
            return
        val = self.isAvailable(carId, start_date, end_date)
        if val:
            self.reservedCars[carId].add((start_date,end_date))
            log.info(f"Car has been booked")
            return True
        log.info(f"Car with {carId} not available in this period, please select another date")
        return False

    def payViaUPI(self, ct:Contract, carId, startDate, endDate):
        obj = UPIPayment(self.cars[carId])
        ct.price = obj.pay(startDate, endDate)

    def payViaCard(self, ct:Contract, carId, startDate, endDate):
        obj = CardPayment(self.cars[carId])
        ct.price = obj.pay(startDate, endDate)

    def unreserveCar(self, carId, contract):
        self.reservedCars[carId].remove((contract.bookedFrom, contract.bookTill))






