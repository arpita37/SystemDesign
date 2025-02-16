from models.menuItem import Menuitem
from models.status import Status
from typing import Dict
from datetime import datetime

class Order:
    def __init__(self,id,menuitems):
        self.id = id
        self.items : Dict[Menuitem] = menuitems
        self.status = Status.PENDING
        self.amount = 0.0
        self.time = datetime.today()

    def getId(self): return self.id
    def getItems(self):
        print("MENUID\tITEM_NAME\tQUANTITY\tAMOUNT")
        for key, val in self.items.items():
            print(f"{key.getId()}\t{key.getName()}\t{val}\t{key.getPrice()}")

    def getStatus(self): return self.status
    def getAmount(self):
        for key,val in self.items.items():
            self.amount += key.getPrice()

    def updateStatus(self,st): self.status = st

