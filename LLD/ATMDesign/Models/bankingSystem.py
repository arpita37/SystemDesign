from Models.account import Account


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def createAccount(self, account : Account):
        if account.getAccountNo() not in self.accounts:
            self.accounts[account.getAccountNo()] = account
            return True
        return False

    def getAccount(self, accountNo):
        if accountNo not in self.accounts:
            return None
        return self.accounts[accountNo]

    def processTransaction(self, transaction):
        transaction.execute()


