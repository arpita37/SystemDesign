import time
import uuid
from threading import Lock
import logging
from datetime import datetime

from overrides import overrides

from models.menuItem import Menuitem
from models.order import Order
from models.paymentMethods import PaymentMethod
from models.reservation import Reservation
from models.status import Status
from utils.menuHandler import MenuHandler
from utils.paymentViaCard import PaymentViaCard
from utils.paymentViaCash import PaymentViaCash
from utils.paymentViaUPI import PaymentViaUPI
from utils.reservationHandler import ReservationHandler
from utils.staffHandler import StaffHandler

logging.basicConfig(level = logging.INFO)
from utils.inventoryHandler import InventoryHandler

class RestaurantManagement:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = InventoryHandler()
            cls._instance.log = logging.getLogger("RestaurantManagement")
            cls._instance.resHandler = ReservationHandler()
            cls._instance.staffhandler = StaffHandler()
            cls._instance.menuHandler = MenuHandler()
            cls._instance.orderList = dict()

        return cls._instance

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            RestaurantManagement()
        return cls._instance

    #operations on Menu
    def addMenu(self, menu):
        self.menuHandler.addMenu(menu,self.log)

    def updateItemPrice(self, menu, newPrice):
        self.menuHandler.updatePrice(menu,newPrice, self.log)

    def updateStatus(self, menu, val):
        self.menuHandler.updateStatus(menu,val,self.log)

    def showMenu(self):
        self.menuHandler.showMenu()

    #operations on staffs
    def addStaff(self, st):
        self.staffhandler.addStaff(st,self.log)

    def updateRating(self,st, val):
        self.staffhandler.updateRating(st,val,self.log)


    #handle reservations
    def addReservation(self,name, contact, size,time):
        with self._lock:
            res = Reservation(self._generateId(),name, contact, size,time)
            self.resHandler.addReservation(res,self.log)
            return res.id

    def updateResTime(self,resId,newTime):
        with self._lock:
            self.resHandler.updateResTiming(resId,newTime,self.log)

    def candelReservation(self,resId):
        with self._lock:
            self.resHandler.cancelReservation(resId, self.log)

    #order management
    def order(self):
        with self._lock:
            try:
                self.log.info("Please select item Id and quantity from the below menu")
                self.menuHandler.showMenu()
                d = dict()
                while(True):
                    inp = input()
                    if inp == "":
                        break
                    id,quantity = list(map(int,inp.strip().split(" ")))
                    if id not in self.menuHandler.menuItems or not self.menuHandler.menuItems[id].is_available():
                        self.log.info("Sorry! Item in not available at the moment, please choose another")
                    d[id] = d.get(id,0)+quantity
                self.log.info("You chose the following items")
                self.showItems(d)
                curr = Order(self._generateId(),d)
                self.notifyKitchen(curr.getId())
                curr.updateStatus(Status.PREPARING)
                self.log.info(f"Order {id} is being prepared!!")
                time.sleep(5)
                curr.updateStatus(Status.READY)
                self.log.info(f"Order {id} is prepared, please proceed for payment!!")
                amount = self.calculateAmount(d)
                self.log.info(f"USer has to pay {amount}")
                txId = self.processPayment(curr.getId(),amount)
                if txId != None:
                    self.dispenseOrder(curr.getId())
                    curr.updateStatus(Status.COMPLETED)
                    return
                self.log.info("Transaction unsucessful, reverting!!!")
                self.revertTransaction(txId)
                curr.updateStatus(Status.CANCELLED)
            except Exception as e:
                raise e

    def processPayment(self,id,amount):
        try:
            self.log.info("Please choose a payment method\n1.Cash\2.Card\3.UPI")
            inp = input()
            txId = self._generateTxId(id)
            match inp.upper():
                case PaymentMethod.CARD.value:
                    obj = PaymentViaCard(txId,amount)
                case PaymentMethod.UPI.value:
                    obj = PaymentViaUPI(txId, amount)
                case _ :
                    obj = PaymentViaCash(txId, amount)
            return txId
        except Exception as e:
            raise e

    def notifyKitchen(self,id):
        self.log.info(f"Order {id} is sent to kitchen!!")

    def dispenseOrder(self,id):
        self.log.info(f"Order {id} is delivered")

    def revertTransaction(self,txId):
        self.log.info(f"Transaction {txId} reverted")

    def calculateAmount(self,curr):
        total = 0
        for key,val in curr.items():
            total += (self.menuHandler.menuItems[key].getPrice()*val)
        return total

    def _generateId(self):
        return f"{uuid.uuid4().hex[:5]}_{datetime.today()}"

    def _generateTxId(self, id):
        return f"{uuid.uuid4().hex[:5]}_{id}"

    def showItems(self,d):
        for key,val in d.items():
            self.log.info(f"Name : {self.menuHandler.menuItems[key].getName()}, Quantity : {val}")