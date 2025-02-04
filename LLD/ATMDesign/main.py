from Handlers.cashDispenser import Dispenser
from Models.account import Account
from Models.bankingSystem import BankingSystem
from PublicInterfaces.atm import ATM


class ATMDemo:
    @staticmethod
    def run():
        #banking System
        bs = BankingSystem()
        account1 = Account(12345, 100000)
        account2 = Account(23456, 900000)
        bs.createAccount(account1)
        bs.createAccount(account2)

        #cash dispenser
        cd = Dispenser(100000000)

        #ATM
        atmObj = ATM(bs, cd)
        atmObj.showBalance(12345)
        atmObj.showBalance(123456)

        atmObj.withDrawBalance(123456,100000)
        atmObj.withDrawBalance(12345, 10000)

        atmObj.depositBalance(23456,30000)


if __name__ == "__main__":
    ATMDemo.run()