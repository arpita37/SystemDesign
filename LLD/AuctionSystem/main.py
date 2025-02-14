import time

from models.auctionListed import AcutionItem
from models.bid import Bid
from models.user import User
from publicInterface.auctionMgmtSystem import AuctionSystem


class Demo:
    @staticmethod
    def run():
        obj = AuctionSystem()
        obj.get_instance()
        u1 = User("Arpita","arpitabasak@gmail.com")
        u2 = User("Kingshuk","kobse@gmail.com")
        obj.showUser()
        obj.addUser(u1)
        obj.addUser(u2)
        obj.showUser()

        item1 = AcutionItem("ART","A beautoful picture of horse",100000,2)
        obj.listAuctionItem(item1)
        time.sleep(1)
        bid1 = Bid(1,u1,1000022)
        obj.listBid(bid1,item1)
        time.sleep(1)
        bid2 = Bid(1,u2,10000000)
        obj.listBid(bid2, item1)
        time.sleep(1)
        obj.findWinner(item1)

if __name__ == "__main__":
    Demo.run()
