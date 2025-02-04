from Handlers.transactionInterface import Transaction


class WithDrawTrasaction(Transaction):
    def __init__(self, id, account, amount):
        super().__init__(id, account, amount)

    def execute(self):
        self.account.debit(self.amount)