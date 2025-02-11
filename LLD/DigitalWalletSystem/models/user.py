from sortedcontainers import SortedList


class User:
    def __init__(self,name,contact,country,card,amt,account):
        self.id = None
        self.name = name
        self.contact = contact
        self.country = country
        self.amount = amt
        self.cards = card
        self.bank_accounts = account
        self.transactions = dict() #based on timing


    def getId(self): return self.id
    def setId(self,id): self.id = id
    def getName(self): return self.name
    def getContact(self): return self.contact
    def getCountry(self): return self.country
    def getAmount(self): return self.amount
    def debit(self,amt): self.amount -= amt
    def credit(self,amt): self.amount += amt

    def add_Transaction(self,tx):
        self.transactions[tx.getID()] = tx

    def viewTransactionHistory(self):
        for key,val in self.transactions.items():
            print(f"\nTransactionNo : {key}\nDetails:\nTarget: {val.getTarget().getName()}\t Source: {val.getSource().getName()}\t Amount: {val.getAmount()}")