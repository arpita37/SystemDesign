from Handlers.paymentInterface import Payment


class CardPayment(Payment):
    def __init__(self, car):
        super().__init__(car)

    def pay(self, startDate, endDate):
        print("This is a payment through card")
        value = self.car.getPrice()
        days = super().days_between(startDate, endDate)
        value = value*days
        print(f"Payment of Rs. {value} done")
        return value