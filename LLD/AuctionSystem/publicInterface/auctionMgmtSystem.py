import datetime
from threading import Lock
import logging

from models.auctionListed import AcutionItem
from models.auctionStatus import AuctionStatus

logging.basicConfig(level=logging.INFO)
class AuctionSystem:
    _instance = None

    def __new__(cls):
        cls._instance = super().__new__(cls)
        cls._instance.users = dict()
        cls._instance.auctions = dict()
        cls._instance.lock = Lock()
        cls._instance.log = logging.getLogger("AuctionMgmtsystem")
        return cls._instance

    def get_instance(cls):
        if not cls._instance:
            AuctionSystem()
        return cls._instance

    def addUser(self, usr):
        id = usr.getId()
        if id in self.users:
            self.log.info(f"The user with id {id} already exists in the system!!!")
            return
        self.users[id] = usr
        self.log.info(f"The user {id} added successfully!!!")

    def showUser(self):
        if not self.users:
            self.log.info("No user found")
            return
        self.log.info("\n-------Listing all users below ------")
        for item in self.users.values():
            self.log.info(f"\nUsername: {item.getName()}")

    def listAuctionItem(self,item : AcutionItem):
        id = item.getId()
        if id in self.auctions:
            self.log.info(f"The auction with id {id} already exists in the system!!!")
            return
        self.auctions[item.getId()] = item
        self.log.info(f"The auctionitem with {id} added successfully!!!")

    def showAuctionList(self,items=None):
        if not items:
            items = self.auctions
        self.log.info(f"\nName\tPRICE\tStatus")
        for key,val in items.items():
            self.log.info(f"\n{val.getName()}\t{val.getFinalPrice()}\t{val.getStatus()}")

    def searchWithName(self,st):
        matches = dict()
        for key,val in self.auctions.items():
            if st in val.getName():
                matches[key] = val

        self.showAuctionList(items=matches)

    def listBid(self,bidInfo,item):
        itemId = item.getId()
        if itemId not in self.auctions:
            self.log.info("\nItem not found")
            return
        item = self.auctions[itemId]
        with self.lock:
            if item.getStartDate()+datetime.timedelta(item.getDuration()) > datetime.datetime.today():
                item.updateBids(bidInfo)
                item.updateFinalPrice(bidInfo.getAmount())
                item.updateHigestBidder(bidInfo.getBidder())
            else:
                self.log.info(f"No more bid allowed on item {itemId}")

    def findWinner(self,item):
        id = item.getId()
        with self.lock:
            if id not in self.auctions:
                self.log.info("Wrong auction id!!!")
                return
            item = self.auctions[id]
            item.updateStatus()


