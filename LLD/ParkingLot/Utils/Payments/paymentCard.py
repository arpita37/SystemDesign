from Utils.Payments.payment import Payment


class PaymentCard(Payment):
    def __init__(self):
        super().__init__("CARD")