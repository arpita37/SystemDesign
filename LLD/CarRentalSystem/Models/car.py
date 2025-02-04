import random
from datetime import datetime
from Models.status import Status
from Models.types import Types


class Car:
    def __init__(self, id,type : Types, make  :str, model : str, year : str, price : int):
        self.carNo = id
        self.type = type
        self.make = make
        self.model = model
        self.year = year
        self.pricePerDay = price
        self.bookedFrom = None
        self.bookedTill = None

    def getCarNo(self):
        return self.carNo

    def getType(self):
        return self.type

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getPrice(self):
        return self.pricePerDay

    def getBookingStartDay(self):
        return self.bookedFrom

    def getBokingEndDay(self):
        return self.bookedTill

    def setBookingStartDay(self, d : datetime):
        self.bookedFrom = d

    def setBokingEndDay(self, d : datetime):
        self.bookedTill = d