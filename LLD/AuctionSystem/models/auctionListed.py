import uuid
from datetime import date,datetime
from models.auctionStatus import AuctionStatus

class AcutionItem:
    def __init__(self,name,description,start_price,duration):
        self.id = self.generateUniqueId(name)
        self.name = name
        self.desc = description
        self.price = start_price
        self.final_price = start_price
        self.date = datetime.today()
        self.duration : int = duration
        self.bids = dict()
        self.status = AuctionStatus.ACTIVE
        self.highestBidder = None

    def getId(self): return self.id
    def getName(self): return self.name
    def getDescription(self): return self.desc
    def getStartPrice(self): return self.price
    def getFinalPrice(self): return self.final_price
    def getStartDate(self): return self.date
    def getDuration(self): return self.duration
    def getBids(self): return self.bids
    def getStatus(self): return self.status

    def updateStatus(self):
        self.status = AuctionStatus.CLOSED
        try:
            print(f"{self.highestBidder.getName()} is winner")
            self.notifyBidders()
        except Exception as e:
            raise ValueError(f"No bid done on this auction with id {self.id}")

    def updateBids(self,bid):
        id = bid.getId()
        self.bids[id] = bid

    def updateFinalPrice(self,amount):
        self.final_price = max(self.final_price,amount)

    def updateHigestBidder(self,user):
        self.highestBidder = user

    def generateUniqueId(self,name):
        return f"{uuid.uuid4().hex[:8]}_{name}_{date.today().strftime('%H_%m_%s')}"

    def notifyBidders(self):
        print(len(self.bids.values()))
        for bid in self.bids.values():
            print(f"Notified user {bid.getBidder().getName()} that bid is closed!!!")