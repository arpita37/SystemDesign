from Models.contract import Contract
from Utils.payementInterface import Payemnt


class CardPayment(Payemnt):
    def __init__(self, ct:Contract):
        super().__init__(ct)

    def processPayment(self):
        start = self.ct.getCheckinDate()
        end = self.ct.getCheckoutDate()
        delta = (end-start)
        total_price = delta.days * self.ct.getRoom().getPrice()
        return f"Payemnt of Rs. {total_price} successful for duration {start} - {end} in card"