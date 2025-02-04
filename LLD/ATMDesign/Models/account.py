class Account:
    def __init__(self, number, balance):
        self.accountNo = number
        self.balance = balance

    def getAccountNo(self):
        return self.accountNo

    def getBalance(self):
        return self.balance

    def credit(self, amount):
        self.balance += amount

    def debit(self,amount):
        self.balance -= amount