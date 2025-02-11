import time

from models.account import Account
from models.card import Card
from models.user import User
from publicInterfaces.digitalWallet import DigitalWallet


class Demo:
    @staticmethod
    def run():
        obj = DigitalWallet()
        obj.getInstance()

        acc1 = Account(123456,"Savings")
        c1 = Card(12345,"Debit",acc1)
        user1 = User("Arpita","8017829520","India",c1,100000,acc1)
        acc2 = Account(1234567, "Current")
        c2 = Card(1234, "Credit", acc2)
        user2 = User("Kingshuk","kbose@gmail.com","USA",c2,10000000,acc2)
        acc3 = Account(19672, "Current")
        c3 = Card(78913, "Credit", acc3)
        user3 = User("adi", "akar@gmail.com", "India", c2, 1003, acc2)

        obj.showHistory(user1)
        obj.createUser(user1)
        obj.createUser(user2)
        obj.showUser()
        obj.makePayment(user1,user2,10000)
        obj.makePayment(user1, user2, 20000)
        time.sleep(1)
        obj.showHistory(user1)
        time.sleep(1)
        obj.makePayment(user2,user3,1000000000)


if __name__ == "__main__":
    Demo.run()
