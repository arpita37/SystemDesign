from Handlers.paymentInterface import Payment


class UPIPayment(Payment):
    def __init__(self, car):
        super().__init__(car)

    def pay(self, startDate, endDate):
        print("This is a payment through UPI")
        value = self.car.getPrice()*(super().days_between(startDate, endDate))
        print(f"Payment of Rs. {value} done")
        return value