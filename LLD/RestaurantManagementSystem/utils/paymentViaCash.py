from utils.paymentInterface import PaymentInterface


class PaymentViaCash(PaymentInterface):
    def __init__(self, txId,amount):
        super().__init__(txId, amount)

    def executeTransaction(self):
        print(f"Payment of Rs.{self.amount}successful through cash")