from Utils.Payments.payment import Payment


class PaymentUpi(Payment):
    def __init__(self):
        super().__init__("UPI")