import logging
import threading
from datetime import datetime

from Handlers.depositTransaction import DepositTrasaction
from Handlers.withDrawTransaction import WithDrawTrasaction

logging.basicConfig(level=logging.INFO)
class ATM:
    def __init__(self, bs, cd):
        self.bankingSystem = bs
        self.dispenser = cd
        self.transactionId = 0
        self.lock = threading.Lock()
        self.log = logging.getLogger("ATM")

    def authenticate_User(self, accountInfo):
        pass

    def showBalance(self, accountId):
        if accountId not in self.bankingSystem.accounts:
            self.log.warning(f"AccountID {accountId} does not exist")
            return
        amount = self.bankingSystem.getAccount(accountId).getBalance()
        self.log.info(f"AccountID {accountId} : {amount}")

    def withDrawBalance(self, accountId, amount):
        account = self.bankingSystem.getAccount(accountId)
        try:
            self.authenticate_User(account)
            tx = WithDrawTrasaction(self._generate_transactionId(), account, amount)
            with self.lock:
                bal = account.getBalance()
                if bal > amount:
                    self.bankingSystem.processTransaction(tx)
                    val = self.dispenser.dispense_Cash(amount)
                    if not val:
                        self.log.warning("Reverting trasaction due to insufficient balance")
                        tx2 = DepositTrasaction(tx.id, account, amount)
                        self.bankingSystem.processTransaction(tx2)
                    else:
                        self.log.info(f"Dispensed cash {amount}")
                else:
                    self.log.warning("No sufficient balance in the account")
        except Exception as e:
            self.log.warning(f"Account {accountId} does not exist")

    def depositBalance(self, accountId, amount):
        account = self.bankingSystem.getAccount(accountId)
        try:
            self.authenticate_User(account)
            tx = DepositTrasaction(self._generate_transactionId(),account,amount)
            self.bankingSystem.processTransaction(tx)
            self.log.info("Deposit trsaction completed")
        except Exception as e:
            self.log.warning(f"Account {accountId} does not exist")

    def _generate_transactionId(self):
        with self.lock:
            s = f"{self.transactionId}-{datetime.today().strftime('%Y-%m-%d %H-%M-%S')}"
            self.transactionId += 1
            return s
