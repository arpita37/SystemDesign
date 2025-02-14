import datetime

class Bid:
    def __init__(self, bid_id, bidder, amount):
        self.id = bid_id
        self.bidder = bidder
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def getId(self):
        return self.id

    def getAmount(self):
        return self.amount

    def getBidder(self):
        return self.bidder