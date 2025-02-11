import time
from datetime import datetime
import uuid
from threading import Lock
import logging
logging.basicConfig(level=logging.INFO)

from models.paymentMethod import PaymentMethod
from models.paymentStatus import Paymentstatus
from models.transaction import Transaction
from utils.transactionViaAccount import TransactionViaAccount
from utils.transactionViaCrad import TransactionViaCard
from utils.userHandler import UserHandler

class DigitalWallet:
    _instance = None

    def __new__(cls):
        cls._instance = super().__new__(cls)
        cls._instance.userHandler = UserHandler()
        cls._instance.lock = Lock()
        cls._instance.log = logging.getLogger("DigitalWalletSystem")
        return cls._instance

    def getInstance(cls):
        if not cls._instance:
            print("\nThis is a singleton class, only one instance allowed!!!!")
        return cls._instance

    def createUser(self, user):
        self.userHandler.createUser(user, self.log)

    def showUser(self):
        self.userHandler.showUser()

    def removeUser(self, user):
        self.userHandler.removeUser(user, self.log)

    def showHistory(self, userId):
        self.userHandler.showHistory(userId,self.log)

    def chekcBalance(self,userId):
        return self.userHandler.checkBalance(userId,self.log)

    def makePayment(self,user1, user2, amount):
        with self.lock:
            id1 = user1.getId() #source
            id2 = user2.getId() #destination
            if not self.userHandler.userExists(id1):
                self.log.warning(f"Payment can't be processed for user {id1}, please open an account first")
            else:
                val = "False"
                if not self.userHandler.userExists(id2):
                    self.log.warning(f"Do you want to send money to external user?\nYES\nNO")
                    val = input()
                else:
                    val = "YES"
                if val.upper() == "YES":
                    tx = Transaction(self._generateTrasactionID(),user2,user1,amount)
                    bal = self.chekcBalance(id1)
                    if bal >= amount:
                        self.log.info(f"Please neter payment method - 1. Card 2. Account")
                        method = input()
                        res = True
                        if method.upper() == PaymentMethod.CARD.value:
                            tx.setPaymentMethod(PaymentMethod.CARD)
                            obj = TransactionViaCard(tx,user1,user2,amount)
                            res = obj.execute()
                            if res:
                                tx.setStatus(Paymentstatus.SUCCESSFUL)
                            else:
                                tx.setStatus(Paymentstatus.CANCELLED)
                        elif method.upper() == PaymentMethod.ACCOUNT.value:
                            tx.setPaymentMethod(PaymentMethod.ACCOUNT)
                            obj = TransactionViaAccount(tx, user1, user2, amount)
                            res = obj.execute()
                            if res:
                                tx.setStatus(Paymentstatus.SUCCESSFUL)
                            else:
                                tx.setStatus(Paymentstatus.CANCELLED)
                        else:
                            print(f"\nUnknown payment method, transaction cancelled!!")
                            tx.setStatus(Paymentstatus.CANCELLED)
                    else:
                        self.log.info("Insufficient balance")
                        tx.setStatus(Paymentstatus.CANCELLED)
                    user1.add_Transaction(tx)
                    user2.add_Transaction(tx)
                else:
                    self.log.info("User not proceeding with transaction")

            self.log.info(f"\nBalance in {user1.getName()}'s account : {user1.getAmount()}")
            self.log.info(f"\nBalance in {user2.getName()}'s account : {user2.getAmount()}")

    def _generateTrasactionID(self):
        return f"{uuid.uuid4().hex[:8]}_{datetime.today().strftime('%Y_%m_%d %H:%M:%S')}"