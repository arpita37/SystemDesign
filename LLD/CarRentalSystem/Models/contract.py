from datetime import datetime

class Contract:
    def __init__(self, id, b1 : datetime, b2 : datetime, userId, paymethod=None, price=None):
        self.carNo = id
        self.bookedFrom = b1
        self.bookTill = b2
        self.user = userId
        self.payemnt = paymethod
        self.price = price